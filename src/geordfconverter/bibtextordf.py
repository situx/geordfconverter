class BibTexToRDF:

    refnotfound=[]
    

    @staticmethod
    def bibtexToRDF(g,entries,ns,nsont,publishers,issuers,creatormode=None):
        typeToURI={"report":"http://purl.org/ontology/bibo/Report","incollection":"http://purl.org/ontology/bibo/Collection","inbook":"http://purl.org/ontology/bibo/BookSection","inproceedings":"http://purl.org/ontology/bibo/Proceedings","article":"http://purl.org/ontology/bibo/Article","book":"http://purl.org/ontology/bibo/Book","phdthesis":"http://purl.org/ontology/bibo/Thesis","misc":"http://purl.org/ontology/bibo/Document"}
        bibmap={}
        dsuri=None
        for entry in entries:
            bibmap[str(entry["ID"])[0:str(entry["ID"]).rfind("_")].replace("_"," ").strip()]=ns+"bib_"+str(entry["ID"])
            g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"),URIRef(str(typeToURI[entry["ENTRYTYPE"]]))))
            if creatormode!=None:
               g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("http://www.w3.org/ns/dcat#Dataset")))
               dsuri=ns+"bib_"+str(entry["ID"])
            else:
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef(str(typeToURI[entry["ENTRYTYPE"]]))))
            g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/dc/elements/1.1/title"), Literal(str(entry["title"]).replace("\"","'"),lang="en"))) 
            if "issn" in entry:
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/issn"), Literal(str(entry["issn"]),datatype="http://www.w3.org/2001/XMLSchema#string")))
            if "eissn" in entry:
                g.add((URIRef(ns+"bib_"+str(entry["ID"]), URIRef("http://purl.org/ontology/bibo/eissn"), Literal(str(entry["eissn"]),datatype="http://www.w3.org/2001/XMLSchema#string"))))
            if "isbn" in entry:
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/isbn"), Literal(str(entry["isbn"]),datatype="http://www.w3.org/2001/XMLSchema#string")))              
            if "number" in entry:
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/number"), Literal(str(entry["number"]),datatype="http://www.w3.org/2001/XMLSchema#integer")))
            if "volume" in entry:
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/volume"), Literal(str(entry["volume"]),datatype="http://www.w3.org/2001/XMLSchema#string")))
            if "publisher" in entry:
                if str(entry["publisher"]) in publishers:
                    g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/dc/terms/publisher"), URIRef(publishers[str(entry["publisher"])])))
                    g.add((URIRef(publishers[str(entry["publisher"])]), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("http://xmlns.com/foaf/0.1/Organization")))
                    g.add((URIRef(publishers[str(entry["publisher"])]), URIRef("http://www.w3.org/2000/01/rdf-schema#label"), Literal(str(entry["publisher"]),lang="en")))
                else:
                    g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/dc/terms/publisher"), Literal(str(entry["publisher"]))))
            if "journal" in entry:
                if entry["journal"] in issuers:
                    g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/issuer"), URIRef(issuers[str(entry["journal"])])))
                    g.add((URIRef(issuers[str(entry["journal"])]), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("http://purl.org/ontology/bibo/Journal")))
                    g.add((URIRef(issuers[str(entry["journal"])]),URIRef("http://www.w3.org/2000/01/rdf-schema#label"), Literal(str(entry["journal"]),lang="en")))
                else:
                    g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/issuer"), Literal(str(entry["journal"]))))
            if "pages" in entry:
                if "--" in entry["pages"]:
                    pagestart=entry["pages"][0:entry["pages"].rfind("--")]
                    pageend=entry["pages"][entry["pages"].rfind("--")+2:]
                    g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/pageStart"), Literal(str(pagestart),datatype="http://www.w3.org/2001/XMLSchema#integer")))
                    g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/pageEnd"), Literal(str(pageend),datatype="http://www.w3.org/2001/XMLSchema#integer")))
            if "and" in entry["author"]:
                for author in entry["author"].split("and"):
                    if "," in author:
                        authoruri=str(author).replace(","," ").strip()
                        authoruri=authoruri.replace(" ","_")
                        authoruri=authoruri.replace("__","_")
                        authoruri=authoruri.strip()
                        g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("http://xmlns.com/foaf/0.1/Person")))
                        g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://www.w3.org/2000/01/rdf-schema#label"), Literal(str(author).strip(),lang="en")))
                        g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://xmlns.com/foaf/0.1/family_Name"), Literal(str(author)[0:str(author).rfind(',')].strip(),lang="en")))
                        g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://xmlns.com/foaf/0.1/firstName"), Literal(str(author)[str(author).rfind(',')+1:].strip(),lang="en")))
                        g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/dc/elements/1.1/creator"), URIRef(ns+"author_"+str(authoruri))))
            else:
                authoruri=str(entry["author"]).replace(","," ").strip()
                authoruri=authoruri.replace(" ","_")
                authoruri=authoruri.replace("__","_")
                authoruri=authoruri.strip()
                g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://www.w3.org/1999/02/22-rdf-syntax-ns#type"), URIRef("http://xmlns.com/foaf/0.1/Person")))
                g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://www.w3.org/2000/01/rdf-schema#label"), Literal(str(entry["author"]).strip(),lang="en")))
                g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://xmlns.com/foaf/0.1/family_Name"), Literal(str(entry["author"])[0:str(entry["author"]).rfind(',')].strip(),lang="en")))
                g.add((URIRef(ns+"author_"+str(authoruri)), URIRef("http://xmlns.com/foaf/0.1/firstName"), Literal(str(entry["author"])[str(entry["author"]).rfind(',')+1:].strip(),lang="en")))
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/dc/elements/1.1/creator"), URIRef(ns+"author_"+str(authoruri))))
            g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/dc/elements/1.1/created"), Literal(str(entry["year"]), datatype="http://www.w3.org/2001/XMLSchema#gYear")))
            if "doi" in entry:
                g.add((URIRef(ns+"bib_"+str(entry["ID"])), URIRef("http://purl.org/ontology/bibo/doi"), Literal(str(entry["doi"]).replace("\\_","_"),datatype="http://www.w3.org/2001/XMLSchema#string")))
    
        return {"triples":g,"bibmap":bibmap,"dsuri":dsuri}

    @staticmethod
    def processReference(g,bibmap,key,row,cururi):
        theval=str(row[key])
        if theval==None or theval=="" or theval=="nan":
            return g
        refs=str(row[key]).split(";")
        for cref in refs:
            ref=cref.strip()
            if "," in cref:
                ref=cref[0:cref.rfind(",")].strip()
            if ref in bibmap:
                g.add((URIRef(str(cururi)),URIRef("http://purl.org/dc/terms/isReferencedBy"), URIRef(str(bibmap[ref]))))
                gotref=True
            elif ref.startswith("http"):
                g.add((URIRef(str(cururi)), URIRef("http://purl.org/dc/terms/isReferencedBy"), Literal(str(ref).strip(),datatype="http://www.w3.org/2001/XMLSchema#anyURI")))
            else:
                #self.refnotfound.add(ref)
                g.add((URIRef(str(cururi)),URIRef("http://www.w3.org/2004/02/skos/core#note"), Literal(str(ref))))
                #print(row["DOC1_Papers"])
        if row[key] in bibmap:
            g.add((URIRef(str(cururi)), URIRef("http://purl.org/dc/terms/isReferencedBy"), URIRef(str(bibmap[row[key]]))))
            gotref=True
        elif ref.startswith("http"):
            g.add((URIRef(str(cururi)), URIRef("http://purl.org/dc/terms/isReferencedBy"), Literal(str(row[key]).strip(),datatype="http://www.w3.org/2001/XMLSchema#anyURI")))
        else:
            #self.refnotfound.add(row[key])
            g.add((URIRef(str(cururi)),URIRef("http://www.w3.org/2004/02/skos/core#note"), Literal(str(row[key]))))
        return g
