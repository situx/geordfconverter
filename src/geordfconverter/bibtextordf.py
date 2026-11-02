from rdflib import Literal, Namespace, URIRef
from rdflib.namespace import RDF, RDFS, SKOS, XSD

BIBO = Namespace("http://purl.org/ontology/bibo/")
DC = Namespace("http://purl.org/dc/elements/1.1/")
DCTERMS = Namespace("http://purl.org/dc/terms/")
DCAT = Namespace("http://www.w3.org/ns/dcat#")
FOAF = Namespace("http://xmlns.com/foaf/0.1/")

class BibTexToRDF:

    refnotfound=[]
    

    @staticmethod
    def bibtexToRDF(g,entries,ns,nsont,publishers,issuers,creatormode=None):
        typeToURI={"report":BIBO.Report,"incollection":BIBO.Collection,"inbook":BIBO.BookSection,"inproceedings":BIBO.Proceedings,"article":BIBO.Article,"book":BIBO.Book,"phdthesis":BIBO.Thesis,"misc":BIBO.Document}
        bibmap={}
        dsuri=None
        for entry in entries:
            biburi = f'{ns}bib_{entry["ID"]}'
            bibmap[str(entry["ID"])[0:str(entry["ID"]).rfind("_")].replace("_"," ").strip()]=biburi
            bibterm = URIRef(biburi)
            g.add((bibterm, RDF.type, typeToURI[entry["ENTRYTYPE"]]))
            if creatormode!=None:
               g.add((bibterm, RDF.type, DCAT.Dataset))
               dsuri=biburi
            g.add((bibterm, DC.title, Literal(str(entry["title"]).replace("\"","'"),lang="en")))
            if "issn" in entry:
                g.add((bibterm, BIBO.issn, Literal(str(entry["issn"]),datatype=XSD.string)))
            if "eissn" in entry:
                g.add((bibterm, BIBO.eissn, Literal(str(entry["eissn"]),datatype=XSD.string)))
            if "isbn" in entry:
                g.add((bibterm, BIBO.isbn, Literal(str(entry["isbn"]),datatype=XSD.string)))
            if "number" in entry:
                g.add((bibterm, BIBO.number, Literal(str(entry["number"]),datatype=XSD.integer)))
            if "volume" in entry:
                g.add((bibterm, BIBO.volume, Literal(str(entry["volume"]),datatype=XSD.string)))
            if "publisher" in entry:
                if str(entry["publisher"]) in publishers:
                    publisher = URIRef(publishers[str(entry["publisher"])])
                    g.add((bibterm, DCTERMS.publisher, publisher))
                    g.add((publisher, RDF.type, FOAF.Organization))
                    g.add((publisher, RDFS.label, Literal(str(entry["publisher"]),lang="en")))
                else:
                    g.add((bibterm, DCTERMS.publisher, Literal(str(entry["publisher"]))))
            if "journal" in entry:
                if entry["journal"] in issuers:
                    issuer = URIRef(issuers[str(entry["journal"])])
                    g.add((bibterm, BIBO.issuer, issuer))
                    g.add((issuer, RDF.type, BIBO.Journal))
                    g.add((issuer,RDFS.label, Literal(str(entry["journal"]),lang="en")))
                else:
                    g.add((bibterm, BIBO.issuer, Literal(str(entry["journal"]))))
            if "pages" in entry:
                if "--" in entry["pages"]:
                    pagestart=entry["pages"][0:entry["pages"].rfind("--")]
                    pageend=entry["pages"][entry["pages"].rfind("--")+2:]
                    g.add((bibterm, BIBO.pageStart, Literal(str(pagestart),datatype=XSD.integer)))
                    g.add((bibterm, BIBO.pageEnd, Literal(str(pageend),datatype=XSD.integer)))
            if "and" in entry["author"]:
                for author in entry["author"].split("and"):
                    if "," in author:
                        authoruri=str(author).replace(","," ").strip()
                        authoruri=authoruri.replace(" ","_")
                        authoruri=authoruri.replace("__","_")
                        authoruri=authoruri.strip()
                        authoriri = f"{ns}author_{authoruri}"
                        BibTexToRDF._add_author(g, bibterm, authoriri, author)
            else:
                authoruri=str(entry["author"]).replace(","," ").strip()
                authoruri=authoruri.replace(" ","_")
                authoruri=authoruri.replace("__","_")
                authoruri=authoruri.strip()
                authoriri = f"{ns}author_{authoruri}"
                BibTexToRDF._add_author(g, bibterm, authoriri, entry["author"])
            g.add((bibterm, DC.created, Literal(str(entry["year"]), datatype=XSD.gYear)))
            if "doi" in entry:
                g.add((bibterm, BIBO.doi, Literal(str(entry["doi"]).replace("\\_","_"),datatype=XSD.string)))
    
        return {"triples":g,"bibmap":bibmap,"dsuri":dsuri}

    @staticmethod
    def _add_author(graph, bibterm, authoriri, author):
        authorterm = URIRef(authoriri)
        author = str(author)
        graph.add((authorterm, RDF.type, FOAF.Person))
        graph.add((authorterm, RDFS.label, Literal(author.strip(),lang="en")))
        graph.add((authorterm, FOAF.family_Name, Literal(author[0:author.rfind(',')].strip(),lang="en")))
        graph.add((authorterm, FOAF.firstName, Literal(author[author.rfind(',')+1:].strip(),lang="en")))
        graph.add((bibterm, DC.creator, authorterm))

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
                g.add((URIRef(str(cururi)),DCTERMS.isReferencedBy, URIRef(str(bibmap[ref]))))
                gotref=True
            elif ref.startswith("http"):
                g.add((URIRef(str(cururi)), DCTERMS.isReferencedBy, Literal(str(ref).strip(),datatype=XSD.anyURI)))
            else:
                #self.refnotfound.add(ref)
                g.add((URIRef(str(cururi)),SKOS.note, Literal(str(ref))))
                #print(row["DOC1_Papers"])
        if row[key] in bibmap:
            g.add((URIRef(str(cururi)), DCTERMS.isReferencedBy, URIRef(str(bibmap[row[key]]))))
            gotref=True
        elif ref.startswith("http"):
            g.add((URIRef(str(cururi)), DCTERMS.isReferencedBy, Literal(str(row[key]).strip(),datatype=XSD.anyURI)))
        else:
            #self.refnotfound.add(row[key])
            g.add((URIRef(str(cururi)),SKOS.note, Literal(str(row[key]))))
        return g
