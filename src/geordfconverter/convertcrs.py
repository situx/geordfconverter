
from rdflib import Graph, URIRef, Literal
from rdflib.namespace import RDF, RDFS, OWL, XSD, DC, PROV, SKOS, GEO
from pyproj import CRS
from vocab.GEOCRS import GEOCRS

GEOEPSG="http://www.opengis.net/def/crs/EPSG/0/"
GEOCRSDATUM="http://www.opengis.net/ont/crs/datum/"
GEOCRSAXIS="http://www.opengis.net/ont/crs/cs/axis/"
GEOCRSISBODY="http://www.opengis.net/ont/crs/isbody/"
GEOCRSGEOD="http://www.opengis.net/ont/crs/geod/"
GEOCRSGRID="http://www.opengis.net/ont/crs/grid/"
GEOCRSAOU="http://www.opengis.net/ont/crs/areaofuse/"
GEOCRSOPERATION="http://www.opengis.net/ont/crs/operation/"
GEOCRSMERIDIAN="http://www.opengis.net/ont/crs/primeMeridian/"
OM="http://www.ontology-of-units-of-measure.org/resource/om-2/"

units = {}
units["m"] = OM+"meter"
units["metre"] = OM+"metre"
units["grad"] = OM+"degree"
units["degree"] = OM+"degree"
units["ft"] = OM+"foot"
units["us-ft"] = OM+"usfoot"
scope = {}
scope["geodesy"] = GEOCRS.Geodesy
scope["topographic mapping"] = GEOCRS.TopographicMap
scope["spatial referencing"] = GEOCRS.SpatialReferencing
scope["engineering survey"] = GEOCRS.EngineeringSurvey
scope["satellite survey"] = GEOCRS.SatelliteSurvey
scope["satellite navigation"] = GEOCRS.SatelliteNavigation
scope["coastal hydrography"] = GEOCRS.CoastalHydrography
scope["offshore engineering"] = GEOCRS.OffshoreEngineering
scope["hydrography"] = GEOCRS.Hydrography
scope["drilling"] = GEOCRS.Drilling
scope["nautical charting"] = GEOCRS.NauticalChart
scope["oil and gas exploration"] = GEOCRS.OilAndGasExploration
scope["cadastre"] = GEOCRS.CadastreMap
coordinatesystem = {}
coordinatesystem["ellipsoidal"] = GEOCRS.EllipsoidalCoordinateSystem
coordinatesystem["cartesian"] = GEOCRS.CartesianCoordinateSystem
coordinatesystem["vertical"] = GEOCRS.VerticalCoordinateSystem
coordinatesystem["ft"] = "om:foot"
coordinatesystem["us-ft"] = "om:usfoot"
spheroids = {}
spheroids["GRS80"] = GEOCRSGEOD+"GRS1980"
spheroids["GRS 80"] = GEOCRSGEOD+"GRS1980"
spheroids["GRS67"] = GEOCRSGEOD+"GRS67"
spheroids["GRS 1967"] = GEOCRSGEOD+"GRS67"
spheroids["GRS 1967 Modified"] = GEOCRSGEOD+"GRS67Modified"
spheroids["GRS 67"] = GEOCRSGEOD+"GRS67"
spheroids["GRS1980"] = GEOCRSGEOD+"GRS1980"
spheroids["GRS 1980"] = GEOCRSGEOD+"GRS1980"
spheroids["NWL 9D"] = GEOCRSGEOD+"NWL9D"
spheroids["PZ-90"] = GEOCRSGEOD+"PZ90"
spheroids["Airy 1830"] = GEOCRSGEOD+"Airy1830"
spheroids["Airy Modified 1849"] = GEOCRSGEOD+"AiryModified1849"
spheroids["intl"] = GEOCRSGEOD+"International1924"
spheroids["aust_SA"] = GEOCRSGEOD+"AustralianNationalSpheroid"
spheroids["Australian National Spheroid"] = GEOCRSGEOD+"AustralianNationalSpheroid"
spheroids["International 1924"] = GEOCRSGEOD+"International1924"
spheroids["clrk"] = GEOCRSGEOD+"Clarke1866"
spheroids["War Office"] = GEOCRSGEOD+"WarOffice"
spheroids["evrst30"] =  GEOCRSGEOD+"Everest1930"
spheroids["clrk66"] =  GEOCRSGEOD+"Clarke1866"
spheroids["Plessis 1817"] =  GEOCRSGEOD+"Plessis1817"
spheroids["Danish 1876"] =  GEOCRSGEOD+"Danish1876"
spheroids["Struve 1860"] =  GEOCRSGEOD+"Struve1860"
spheroids["IAG 1975"] =  GEOCRSGEOD+"IAG1975"
spheroids["Clarke 1866"] =  GEOCRSGEOD+"Clarke1866"
spheroids["Clarke 1858"] =  GEOCRSGEOD+"Clarke1858"
spheroids["Clarke 1880"] =  GEOCRSGEOD+"Clarke1880"
spheroids["Helmert 1906"] =  GEOCRSGEOD+"Helmert1906"
spheroids["Moon_2000_IAU_IAG"] =  GEOCRSGEOD+"Moon2000_IAU_IAG"
spheroids["CGCS2000"] =  GEOCRSGEOD+"CGCS2000"
spheroids["GSK-2011"] =  GEOCRSGEOD+"GSK2011"
spheroids["Zach 1812"] =  GEOCRSGEOD+"Zach1812"
spheroids["Hough 1960"] =  GEOCRSGEOD+"Hough1960"
spheroids["Hughes 1980"] =  GEOCRSGEOD+"Hughes1980"
spheroids["Indonesian National Spheroid"] =  GEOCRSGEOD+"IndonesianNationalSpheroid"
spheroids["clrk80"] =  GEOCRSGEOD+"Clarke1880RGS"
spheroids["Clarke 1880 (Arc)"] =  GEOCRSGEOD+"Clarke1880ARC"
spheroids["Clarke 1880 (RGS)"] =  GEOCRSGEOD+"Clarke1880RGS"
spheroids["Clarke 1880 (IGN)"] =  GEOCRSGEOD+"Clarke1880IGN"
spheroids["clrk80ign"] =  GEOCRSGEOD+"Clarke1880IGN"
spheroids["WGS66"] =  GEOCRSGEOD+"WGS66"
spheroids["WGS 66"] =  GEOCRSGEOD+"WGS66"
spheroids["WGS72"] =  GEOCRSGEOD+"WGS72"
spheroids["WGS 72"] =  GEOCRSGEOD+"WGS72"
spheroids["WGS84"] =  GEOCRSGEOD+"WGS84"
spheroids["WGS 84"] =  GEOCRSGEOD+"WGS84"
spheroids["Krassowsky 1940"] =  GEOCRSGEOD+"Krassowsky1940"
spheroids["krass"] =  GEOCRSGEOD+"Krassowsky1940"
spheroids["Bessel 1841"] =  GEOCRSGEOD+"Bessel1841"
spheroids["bessel"] =  GEOCRSGEOD+"Bessel1841"
spheroids["Bessel Modified"] =  GEOCRSGEOD+"BesselModified"
projections = {}
projections["tmerc"] = GEOCRS.TransverseMercatorProjection
projections["omerc"] = GEOCRS.ObliqueMercatorProjection
projections["merc"] = GEOCRS.MercatorProjection
projections["sinu"] = GEOCRS.SinusoidalProjection
projections["rpoly"] = GEOCRS.RectangularPolyconicProjection
projections["poly"] = GEOCRS.AmericanPolyconicProjection
projections["eqdc"] = GEOCRS.EquidistantConicProjection
projections["sterea"] = GEOCRS.ObliqueStereographicProjection
projections["cea"] = GEOCRS.CylindricalEqualArea
projections["aea"] = GEOCRS.AlbersEqualAreaProjection
projections["eqearth"] = GEOCRS.EqualEarthProjection
projections["natearth"] = GEOCRS.NaturalEarthProjection
projections["stere"] = GEOCRS.StereographicProjection
projections["cass"] = GEOCRS.CassiniProjection
projections["nell"] = GEOCRS.PseudoCylindricalProjection
projections["eck1"] = GEOCRS.PseudoCylindricalProjection
projections["eck2"] = GEOCRS.PseudoCylindricalProjection
projections["eck3"] = GEOCRS.PseudoCylindricalProjection
projections["eck4"] = GEOCRS.PseudoCylindricalProjection
projections["eck5"] = GEOCRS.PseudoCylindricalProjection
projections["eck6"] = GEOCRS.PseudoCylindricalProjection
projections["eqc"] = GEOCRS.EquidistantCylindricalProjection
projections["col_urban"] = GEOCRS.ColombiaUrbanProjection
projections["laea"] = GEOCRS.LambertAzimuthalEqualArea
projections["leac"] = GEOCRS.LambertEqualAreaConic
projections["labrd"] = GEOCRS.LabordeProjection
projections["lcc"] = GEOCRS.LambertConformalConicProjection
projections["gnom"] = GEOCRS.GnomonicProjection
projections["bonne"] = GEOCRS.BonneProjection
projections["moll"] = GEOCRS.MollweideProjection
projections["mill"] = GEOCRS.MillerProjection
projections["nicol"] = GEOCRS.NicolosiGlobularProjection
projections["collg"] = GEOCRS.CollignonProjection
projections["robin"] = GEOCRS.RobinsonProjection
projections["loxim"] = GEOCRS.LoximuthalProjection
projections["aitoff"] = GEOCRS.AitoffProjection
projections["ortho"] = GEOCRS.OrthographicProjection
projections["kav5"] = GEOCRS.PseudoCylindricalProjection
projections["tcea"] = GEOCRS.CylindricalProjection
projections["utm"] = GEOCRS.UniversalTransverseMercatorProjection
projections["krovak"] = GEOCRS.Krovak
projections["geocent"] = GEOCRS.Geocentric
projections["latlong"] = GEOCRS.LatLonProjection
projections["longlat"] = GEOCRS.LonLatProjection

class ConvertCRS:

	def __init__(self):
		self.ttlhead = "@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
		self.ttlhead += "@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
		self.ttlhead += "@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
		self.ttlhead += "@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
		self.ttlhead += "@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
		self.ttlhead += "@prefix prov: <http://www.w3.org/ns/prov-o/> .\n"
		self.ttlhead += "@prefix geoepsg: <http://www.opengis.net/def/crs/EPSG/0/> .\n"
		self.ttlhead += "@prefix geo: <http://www.opengis.net/ont/geosparql#> .\n"
		self.ttlhead += "@prefix geocrs: <http://www.opengis.net/ont/crs/> .\n"
		self.ttlhead += "@prefix geocrsdatum: <http://www.opengis.net/ont/crs/datum/> .\n"
		self.ttlhead += "@prefix geocrsisbody: <http://www.opengis.net/ont/crs/isbody/> .\n"
		self.ttlhead += "@prefix geocrsgrid: <http://www.opengis.net/ont/crs/grid/> .\n"
		self.ttlhead += "@prefix geocrsproj: <http://www.opengis.net/ont/crs/proj/> .\n"
		self.ttlhead += "@prefix geocrsaxis: <http://www.opengis.net/ont/crs/cs/axis/> .\n"
		self.ttlhead += "@prefix geocrsgeod: <http://www.opengis.net/ont/crs/geod/> .\n"
		self.ttlhead += "@prefix geocrsaou: <http://www.opengis.net/ont/crs/areaofuse/> .\n"
		self.ttlhead += "@prefix geocrsmeridian: <http://www.opengis.net/ont/crs/primeMeridian/> .\n"
		self.ttlhead += "@prefix geocrsoperation: <http://www.opengis.net/ont/crs/operation/> .\n"
		self.ttlhead += "@prefix geocs: <http://www.opengis.net/ont/crs/cs/> .\n"
		self.ttlhead += "@prefix dc: <http://purl.org/dc/elements/1.1/> .\n"
		self.ttlhead += "@prefix wd: <http://www.wikidata.org/entity/> .\n"
		self.ttlhead += "@prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .\n"

    @staticmethod
    def labelFromURI(uri,prefixlist=None):
        if not uri.startswith("http"):
            return uri
        if uri.endswith("#"):
            uri=uri[0:-1]
        if "#" in uri:
            prefix=uri[:uri.rfind("#")+1]
            if prefixlist is not None and prefix in prefixlist:
                return f'{prefixlist[prefix]}:{uri[uri.rfind("#") + 1:]}'
            return uri[uri.rfind("#") + 1:]
        if uri.endswith("/"):
            uri=uri[0:-1]
        if "/" in uri:
            prefix=uri[:uri.rfind("/")+1]
            if prefixlist is not None and prefix in prefixlist:
                return f'{prefixlist[prefix]}:{uri[uri.rfind("/") + 1:]}'
            return uri[uri.rfind("/") + 1:]
        return uri

	@staticmethod
	def addNamespaces(graph):
		graph.bind("rdf",RDF)
		graph.bind("rdfs",RDFS)
		graph.bind("owl",OWL)
		graph.bind("xsd",XSD)
		graph.bind("skos",SKOS)
		graph.bind("prov",PROV)
		graph.bind("geo", "http://www.opengis.net/ont/geosparql#")
		graph.bind("geocrs", "http://www.opengis.net/ont/crs/")
		graph.bind("geocrsdatum", "http://www.opengis.net/ont/crs/datum/")
		graph.bind("geocrsgrid", "http://www.opengis.net/ont/crs/grid/")
		graph.bind("geocrsisbody", "http://www.opengis.net/ont/crs/isbody/")
		graph.bind("geoepsg","http://www.opengis.net/def/crs/EPSG/0/")
		graph.bind("geocrsgrid","http://www.opengis.net/ont/crs/grid/")
		graph.bind("geocrsproj", "http://www.opengis.net/ont/crs/proj/")
		graph.bind("geocrsaxis", "http://www.opengis.net/ont/crs/cs/axis/")
		graph.bind("geocrsgeod", "http://www.opengis.net/ont/crs/geod/")
		graph.bind("geocrsaou", "http://www.opengis.net/ont/crs/areaofuse/")
		graph.bind("geocrsmeridian", "http://www.opengis.net/ont/crs/primeMeridian/")
		graph.bind("geocrsoperation", "http://www.opengis.net/ont/crs/operation/")
		graph.bind("geocs", "http://www.opengis.net/ont/crs/cs/")
		graph.bind("dc", "http://purl.org/dc/elements/1.1/")
		graph.bind("wd", "http://www.wikidata.org/entity/")
		graph.bind("om", "http://www.ontology-of-units-of-measure.org/resource/om-2/")
		return graph


	@staticmethod
	def convertCRSFromEPSG(epsgcode,ttl):
		if "EPSG:" in epsgcode:
			epsgcode=epsgcode.replace("EPSG:","")
		try:
			curcrs=CRS.from_epsg(int(epsgcode))
			print("EPSG: "+str(epsgcode))
			ttl+=ConvertCRS.crsToTTL(ttl, curcrs, epsgcode, 1, None)
		except:
			print("Could not parse EPSG code "+str(epsgcode))
		return ttl

	@staticmethod
	def convertCRSFromWKTStringSet(wkt,ttl, authcode=None):
		if authcode!=None and "EPSG:" in authcode:
			authcode=authcode.replace("EPSG:","")
		try:
			#print("WKT " + str(wkt), MESSAGE_CATEGORY, Qgis.Info)
			curcrs=CRS.from_wkt(wkt)
			print("Parsed WKT " + str(curcrs))
			if authcode!=None and authcode!="":
				res=ConvertCRS.crsToTTL(ttl, curcrs, authcode, 1, None)
			else:
				res=ConvertCRS.crsToTTL(ttl, curcrs, "WKT", 1, None)
			print("Parsed WKT Res " + str(res))
			ttl=res
		except:
			print("Could not parse WKT "+str(wkt))
		return ttl

	@staticmethod
	def convertCRSFromWKTString(wkt,ttl, authcode=None):
		set=ConvertCRS.convertCRSFromWKTStringSet(wkt,ttl, authcode)
		return "".join(set)

	@staticmethod
	def crsToTTL(ttl,curcrs,x,geodcounter,crsclass):
		epsgcode=str(x)
		csuri=URIRef(GEOEPSG + epsgcode + "_cs")
		crsuri=URIRef(GEOEPSG+str(x))
		wkt=curcrs.to_wkt().replace("\"","'").strip()
		if crsclass is not None:
			ttl.add((crsuri,RDF.type,URIRef(crsclass)))
		elif "Projected CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.ProjectedCRS))
		elif "Geographic 2D CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.GeographicCRS))
		elif "Geographic 3D CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.GeographicCRS))
		elif "Bound CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.BoundCRS))
		elif "Vertical CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.VerticalCRS))
		elif "Geocentric CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.GeocentricCRS))
		elif "Geographic 3D CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.GeographicCRS))
		elif "Compound CRS" in curcrs.type_name:
			ttl.add((crsuri, RDF.type, GEOCRS.CompoundCRS))
			for subcrs in curcrs.sub_crs_list:
				ttl.add((crsuri, GEOCRS.includesSRS,URIRef(GEOEPSG+str(subcrs.to_epsg()))))
		else:
			ttl.add((crsuri, RDF.type, GEOCRS.CRS))
		ttl.add((crsuri, RDF.type, PROV.Entity))
		ttl.add((crsuri, GEOCRS.isApplicableTo, URIRef(GEOCRSISBODY+"Earth")))
		ttl.add((crsuri, RDF.type, OWL.NamedIndividual))
		ttl.add((crsuri, RDFS.label, Literal(curcrs.name.strip(),lang="en")))
		ttl.add((crsuri, GEOCRS.isBound, Literal(str(curcrs.is_bound).lower(),datatype=XSD.boolean)))
		if curcrs.coordinate_system is not None and curcrs.coordinate_system.name in coordinatesystem:
			ttl.add((csuri, RDF.type, coordinatesystem[curcrs.coordinate_system.name]))
			if len(curcrs.coordinate_system.axis_list)==2:
				ttl.add((csuri, RDF.type, GEOCRS.PlanarCoordinateSystem))
			elif len(curcrs.coordinate_system.axis_list)==3:
				ttl.add((csuri, RDF.type, URIRef(GEOCRS+"3DCoordinateSystem")))
			ttl.add((csuri, RDFS.label, Literal("EPSG:"+epsgcode+" CS: "+curcrs.coordinate_system.name)))
			if curcrs.coordinate_system.remarks is not None:
				ttl.add((csuri, RDFS.comment, Literal(str(curcrs.coordinate_system.remarks),lang="en")))
			if curcrs.coordinate_system.scope is not None:
				ttl.add((csuri, GEOCRS.scope,  Literal(str(curcrs.coordinate_system.scope),datatype=XSD.string)))
			for axis in curcrs.coordinate_system.axis_list:
				axisid=axis.name.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_")+"_"+axis.unit_name.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_")+"_"+axis.direction.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_")
				axisuri=URIRef(GEOCRSAXIS+axisid)
				ttl.add((csuri, GEOCRS.axis, axisuri))
				ttl.add((axisuri, RDF.type, GEOCRS.CoordinateSystemAxis))
				ttl.add((axisuri, GEOCRS.direction, URIRef(GEOCRS+axis.direction)))
				ttl.add((axisuri, GEOCRS.abbreviation, Literal(str(axis.abbrev).replace("\"","'"),datatype=XSD.string)))
				ttl.add((axisuri, GEOCRS.unit_conversion_factor, Literal(str(axis.unit_conversion_factor),datatype=XSD.double)))
				ttl.add((axisuri, GEOCRS.unit_auth_code,Literal(str(axis.unit_auth_code),datatype=XSD.string)))
				ttl.add((axisuri, GEOCRS.unit_code, Literal(str(axis.unit_code),datatype=XSD.string)))
				ttl.add((URIRef(GEOCRSAXIS+axis.direction), RDF.type, GEOCRS.AxisDirection))
				if axis.unit_name in units:
					ttl.add((axisuri, GEOCRS.unit, URIRef(units[axis.unit_name])))
					ttl.add((axisuri, RDFS.label, Literal(f"{axis.name} ({ConvertCRS.labelFromURI(str(units[axis.unit_name]))})",lang="en")))
				else:
					ttl.add((axisuri,GEOCRS.unit, Literal(str(axis.unit_name),datatype=XSD.string)))
					ttl.add((axisuri, RDFS.label, Literal(f"{axis.name} ({axis.unit_name})",lang="en")))
			ttl.add((csuri, GEOCRS.asWKT, Literal(str(curcrs.coordinate_system.to_wkt()).replace("\"","'").replace("\n",""))))
			ttl.add((csuri, GEOCRS.asProjJSON, Literal(str(curcrs.coordinate_system.to_json()).replace("\"","'").replace("\n",""))))
			ttl.add((crsuri,GEOCRS.coordinateSystem, URIRef(GEOEPSG+epsgcode+"_cs")))
		elif curcrs.coordinate_system is not None:
			ttl.add((crsuri, GEOCRS.coordinateSystem, Literal(str(curcrs.coordinate_system),datatype=XSD.string)))
		if curcrs.source_crs is not None:
			ttl.add((crsuri, GEOCRS.sourceCRS, URIRef(GEOEPSG+curcrs.source_crs.to_epsg())))
		if curcrs.target_crs is not None:
			ttl.add((crsuri, GEOCRS.targetCRS, URIRef(GEOEPSG+str(curcrs.target_crs.to_epsg()))))
		if curcrs.scope is not None:
			if "," in curcrs.scope:
				for scp in curcrs.scope.split(","):
					#print("Scope: "+scp)
					if scp.lower().strip().replace(".","") in scope:
						ttl.add((crsuri,GEOCRS.usage, URIRef(scope[scp.lower().strip().replace(".","")])))
						ttl.add(URIRef(scope[scp.lower().strip().replace(".","")]), RDFS.subClassOf, GEOCRS.SRSApplication)
					else:
						ttl.add((crsuri, GEOCRS.usage, Literal(str(curcrs.datum.scope),datatype=XSD.string)))
			ttl.add((crsuri, GEOCRS.scope, Literal(str(curcrs.scope).replace("\"","'"),datatype=XSD.string)))
		if curcrs.area_of_use is not None:
			ttl.add((crsuri, GEOCRS.area_of_use, URIRef(GEOEPSG+epsgcode+"_area_of_use")))
			ttl.add((URIRef(GEOEPSG + epsgcode+"_area_of_use"), RDF.type, GEOCRS.AreaOfUse))
			ttl.add((URIRef(GEOEPSG + epsgcode+"_area_of_use"), RDFS.label,  Literal(str(curcrs.area_of_use.name).replace("\"","'"),lang="en")))
			#b = box(curcrs.area_of_use.west, curcrs.area_of_use.south, curcrs.area_of_use.east, curcrs.area_of_use.north)
			#ttl.add(crsuri+"_area_of_use"+" geocrs:extent   \"<http://www.opengis.net/def/crs/OGC/1.3/CRS84> "+str(b.wkt)+"\"^^geo:wktLiteral . \n")
			#\"ENVELOPE("+str(curcrs.area_of_use.west)+" "+str(curcrs.area_of_use.south)+","+str(curcrs.area_of_use.east)+" "+str(curcrs.area_of_use.north)+")\"^^geo:wktLiteral . \n")
		if curcrs.get_geod() is not None:
			geoid= GEOCRSGEOD+""+str(geodcounter)
			if curcrs.datum.ellipsoid is not None:
				if curcrs.datum.ellipsoid.name in spheroids:
					geoid=URIRef(spheroids[curcrs.datum.ellipsoid.name])
					ttl.add((geoid, RDF.type, GEOCRS.Ellipsoid))
					ttl.add((geoid, RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
					ttl.add((geoid, GEOCRS.approximates, URIRef(GEOCRSISBODY+"Earth")))
				elif curcrs.get_geod().sphere:
					geoid=URIRef(GEOCRSGEOD+str(curcrs.datum.ellipsoid.name).replace(" ","_").replace("(","_").replace(")","_"))
					ttl.add((geoid, RDF.type, GEOCRS.Sphere))
					ttl.add((geoid, RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
					ttl.add((geoid, GEOCRS.approximates, URIRef(GEOCRSISBODY+"Earth")))
				else:
					geoid=URIRef(GEOCRSGEOD+str(curcrs.datum.ellipsoid.name).replace(" ","_").replace("(","_").replace(")","_"))
					ttl.add((geoid, RDF.type, GEOCRS.Geoid))
					ttl.add((geoid, RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
					ttl.add((geoid, GEOCRS.approximates, URIRef(GEOCRSISBODY+"Earth")))
			else:
				ttl.add((crsuri, GEOCRS.ellipsoid, URIRef(GEOCRSGEOD+str(geodcounter))))
				ttl.add((URIRef(GEOCRSGEOD+str(geodcounter)), RDF.type, GEOCRS.Geoid))
				ttl.add((geoid, RDFS.label, Literal("Geoid "+str(geodcounter),lang="en")))
				ttl.add((geoid, GEOCRS.approximates, URIRef(GEOCRSISBODY+"Earth")))
			ttl.add((geoid, SKOS.definition, Literal(str(curcrs.get_geod().initstring),datatype=XSD.string)))
			ttl.add((geoid, GEOCRS.eccentricity, Literal(str(curcrs.get_geod().es),datatype=XSD.double)))
			ttl.add((geoid, GEOCRS.isSphere, Literal(str(curcrs.get_geod().sphere),datatype=XSD.boolean)))
			ttl.add((geoid, GEOCRS.semiMajorAxis, Literal(str(curcrs.get_geod().a),datatype=XSD.string)))
			ttl.add((geoid, GEOCRS.semiMinorAxis, Literal(str(curcrs.get_geod().b),datatype=XSD.string)))
			ttl.add((geoid, GEOCRS.flatteningParameter, Literal(str(curcrs.get_geod().f),datatype=XSD.double)))
			geodcounter+=1
		if curcrs.coordinate_operation is not None:
			coordoperationid=curcrs.coordinate_operation.name.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_").replace(",","_").replace("&","and").strip()
			csopuri=URIRef(GEOCRSOPERATION+str(coordoperationid))
			ttl.add((crsuri, GEOCRS.coordinateOperation,csopuri))
			ttl.add((csopuri, GEOCRS.accuracy, Literal(str(curcrs.coordinate_operation.accuracy),datatype=XSD.double)))
			ttl.add((csopuri,GEOCRS.method_name,Literal(str(curcrs.coordinate_operation.method_name))))
			ttl.add((csopuri,GEOCRS.asProj4, Literal(str(curcrs.coordinate_operation.to_proj4()).strip().replace("\"","'").replace("\n",""))))
			ttl.add((csopuri,GEOCRS.asProjJSON,Literal(str(curcrs.coordinate_operation.to_json()).strip().replace("\"","'").replace("\n",""))))
			ttl.add((csopuri,GEOCRS.asWKT, Literal(str(curcrs.coordinate_operation.to_wkt()).replace("\"","'").replace("\n",""),datatype=GEOCRS.wktLiteral)))
			if curcrs.coordinate_operation.scope is not None:
				ttl.add((csopuri, GEOCRS.scope, Literal(str(curcrs.coordinate_operation.scope).replace("\"","'"),datatype=XSD.string)))
			if curcrs.coordinate_operation.remarks is not None:
				ttl.add((csopuri,RDFS.comment, Literal(str(curcrs.coordinate_operation.remarks).replace("\"","'").replace("\n",""),datatype=XSD.string)))
			ttl.add((csopuri, GEOCRS.has_ballpark_transformation, Literal(str(curcrs.coordinate_operation.has_ballpark_transformation),datatype=XSD.boolean)))
			if curcrs.coordinate_operation.area_of_use is not None:
				ttl.add((csopuri,GEOCRS.area_of_use,URIRef(GEOCRSAOU+str(coordoperationid)+"_area_of_use")))
				ttl.add(URIRef(GEOCRSAOU+str(coordoperationid)+"_area_of_use"),RDF.type, GEOCRS.AreaOfUse)
				ttl.add(URIRef(GEOCRSAOU+str(coordoperationid)+"_area_of_use"), RDFS.label, Literal(str(curcrs.coordinate_operation.area_of_use.name).replace("\"","'"),lang="en"))
				#b = box(curcrs.coordinate_operation.area_of_use.west, curcrs.coordinate_operation.area_of_use.south, curcrs.coordinate_operation.area_of_use.east, curcrs.coordinate_operation.area_of_use.north)
				#ttl.add("geocrsaou:"+str(coordoperationid)+"_area_of_use geocrs:extent \"<http://www.opengis.net/def/crs/OGC/1.3/CRS84> "+str(b.wkt)+"\"^^geo:wktLiteral . \n")
				#ENVELOPE("+str(curcrs.coordinate_operation.area_of_use.west)+" "+str(curcrs.coordinate_operation.area_of_use.south)+","+str(curcrs.coordinate_operation.area_of_use.east)+" "+str(curcrs.coordinate_operation.area_of_use.north)+")\"^^geocrs:wktLiteral . \n")
			if curcrs.coordinate_operation.towgs84 is not None:
				print(curcrs.coordinate_operation.towgs84)
			for par in curcrs.coordinate_operation.params:
				ttl.add(URIRef(GEOCRS+str(par.name)[0].lower()+str(par.name).title().replace(" ","")[1:]), RDF.type, OWL.DatatypeProperty)
				ttl.add(URIRef(GEOCRS+str(par.name)[0].lower()+str(par.name).title().replace(" ","")[1:]), RDFS.range, XSD.double)
				ttl.add(URIRef(GEOCRS+str(par.name)[0].lower()+str(par.name).title().replace(" ","")[1:]), RDFS.domain, GEOCRS.CoordinateOperation)
				ttl.add(URIRef(GEOCRS+str(par.name)[0].lower()+str(par.name).title().replace(" ","")[1:]), RDFS.label, Literal(str(par.name),lang="en"))
				ttl.add(csopuri, URIRef(GEOCRS+str(par.name)[0].lower()+str(par.name).title().replace(" ","")[1:]),Literal(str(par.value),datatype=XSD.double))
			for grid in curcrs.coordinate_operation.grids:
				ttl.add((csopuri, GEOCRS.grid, URIRef(GEOCRSGRID+str(grid.name).replace(" ","_"))))
				ttl.add((URIRef(GEOCRSGRID+str(grid.name).replace(" ","_")), RDF.type, GEOCRS.Grid))
				ttl.add((URIRef(GEOCRSGRID+str(grid.name).replace(" ","_")), RDFS.label, Literal(str(grid.full_name),lang="en")))
				ttl.add((URIRef(GEOCRSGRID+str(grid.name).replace(" ","_")), RDFS.label, Literal(str(grid.short_name),lang="en")))
				ttl.add((URIRef(GEOCRSGRID+str(grid.name).replace(" ","_")),GEOCRS.open_license, Literal(str(grid.open_license),datatype=XSD.boolean)))
				ttl.add((URIRef(GEOCRSGRID+str(grid.name).replace(" ","_")), RDFS.comment, Literal(str(grid.url),lang="en")))
			if curcrs.coordinate_operation.operations is not None:
				for operation in curcrs.coordinate_operation.operations:
					ttl.add(csopuri, GEOCRS.operation, Literal(str(operation).replace("\n","").replace("\"","'"),datatype=XSD.string))
			if curcrs.coordinate_operation.type_name is None:
				ttl.add(csopuri, RDF.type, GEOCRS.CoordinateOperation)
			elif curcrs.coordinate_operation.type_name=="Conversion":
				found=False
				if curcrs.coordinate_operation.to_proj4() is not None:
					proj4string=curcrs.coordinate_operation.to_proj4().strip().replace("\"","'").replace("\n","")
					for prj in projections:
						if prj in proj4string:
							ttl.add((csopuri, RDF.type,projections[prj]))
							found=True
							break
				if not found:
					ttl.add((csopuri,RDF.type, GEOCRS.CoordinateConversionOperation))
			elif curcrs.coordinate_operation.type_name=="Transformation":
				ttl.add(csopuri, RDF.type, GEOCRS.CoordinateTransformationOperation)
			elif curcrs.coordinate_operation.type_name=="Concatenated Operation":
				ttl.add(csopuri, RDF.type, GEOCRS.CoordinateConcatenatedOperation)
			elif curcrs.coordinate_operation.type_name=="Other Coordinate Operation":
				ttl.add(csopuri, RDF.type, GEOCRS.OtherCoordinateOperation)
			ttl.add((csopuri), RDFS.label, Literal(curcrs.coordinate_operation.name+": "+curcrs.coordinate_operation.method_name,lang="en"))
		if curcrs.datum is not None:
			datumid=str(curcrs.datum.name.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_").replace("+","_plus").replace("[","_").replace("]","_"))
			ttl.add(crsuri, GEOCRS.datum, URIRef(GEOCRSDATUM+str(datumid)))
			if "Geodetic Reference Frame" in curcrs.datum.type_name:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), RDF.type, GEOCRS.GeodeticReferenceFrame))
			elif "Dynamic Vertical Reference Frame" in curcrs.datum.type_name:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), RDF.type, GEOCRS.DynamicVerticalReferenceFrame))
			elif "Vertical Reference Frame" in curcrs.datum.type_name:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), RDF.type, GEOCRS.VerticalReferenceFrame))
			else:
				print(curcrs.datum.type_name)
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)),RDF.type, GEOCRS.Datum))
			ttl.add((URIRef(GEOCRSDATUM+str(datumid)), RDFS.label, Literal("Datum: "+str(curcrs.datum.name),lang="en")))
			if curcrs.datum.remarks is not None:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), RDFS.comment, Literal(str(curcrs.datum.remarks),lang="en")))
			if curcrs.datum.scope is not None:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), GEOCRS.scope, Literal(str(curcrs.datum.scope),datatype=XSD.string)))
				if "," in curcrs.datum.scope:
					for scp in curcrs.datum.scope.split(","):
						#print("Scope: "+scp)
						if scp.lower().strip().replace(".","") in scope:
							ttl.add((URIRef(GEOCRSDATUM+str(datumid)), GEOCRS.usage,URIRef(scope[scp.lower().strip().replace(".","")])))
							ttl.add((URIRef(scope[scp.lower().strip().replace(".","")]),RDFS.subClassOf, GEOCRS.SRSApplication))
						else:
							ttl.add((URIRef(GEOCRSDATUM+str(datumid)), GEOCRS.usage, Literal(str(curcrs.datum.scope),datatype=XSD.string)))
				print(str(curcrs.datum.scope))
			if curcrs.datum.ellipsoid is not None and curcrs.datum.ellipsoid.name in spheroids:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), GEOCRS.ellipse, URIRef(spheroids[curcrs.datum.ellipsoid.name])))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), RDF.type, GEOCRS.Ellipsoid))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), GEOCRS.inverse_flattening, Literal(str(curcrs.datum.ellipsoid.inverse_flattening),datatype=XSD.double)))
				if curcrs.datum.ellipsoid.remarks is not None:
					ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), RDFS.comment, Literal(str(curcrs.datum.ellipsoid.remarks),datatype=XSD.string)))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), GEOCRS.is_semi_minor_computed, Literal(str(curcrs.datum.ellipsoid.is_semi_minor_computed).lower(),datatype=XSD.boolean)))
			elif curcrs.datum.ellipsoid is not None:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), GEOCRS.ellipse, Literal(curcrs.datum.ellipsoid.name,datatype=XSD.string)))
			if curcrs.prime_meridian is not None:
				ttl.add((URIRef(GEOCRSDATUM+str(datumid)), GEOCRS.primeMeridian,URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ",""))))
				ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), RDF.type, GEOCRS.PrimeMeridian))
				ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), RDFS.label, Literal(curcrs.prime_meridian.name,lang="en")))
				ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), GEOCRS.longitude, Literal(str(curcrs.prime_meridian.longitude),datatype=XSD.double)))
				if curcrs.prime_meridian.unit_name in units:
					ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), GEOCRS.unit, URIRef(OM+units[curcrs.prime_meridian.unit_name])))
					ttl.add((URIRef(units[curcrs.prime_meridian.unit_name]), RDF.type, URIRef(OM+"Unit")))
				else:
					ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), GEOCRS.unit, Literal(str(curcrs.prime_meridian.unit_name),datatype=XSD.string)))
				ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), GEOCRS.asWKT, Literal(str(curcrs.prime_meridian.to_wkt()).replace("\"","'").replace("\n",""),datatype=XSD.string)))
				ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), GEOCRS.asProjJSON, Literal(str(curcrs.prime_meridian.to_json()).replace("\"","'").replace("\n",""),datatype=XSD.string)))
				if curcrs.prime_meridian.remarks is not None:
					ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")),RDFS.comment,Literal(str(curcrs.prime_meridian.remarks),lang="en")))
				if curcrs.prime_meridian.scope is not None:
					ttl.add((URIRef(GEOCRSMERIDIAN+curcrs.prime_meridian.name.replace(" ","")), GEOCRS.scope, Literal(str(curcrs.prime_meridian.scope),datatype=XSD.string)))
		ttl.add((crsuri, GEOCRS.isVertical, URIRef(str(curcrs.is_vertical).lower(),datatype=XSD.boolean)))
		ttl.add((crsuri, GEOCRS.isProjected, Literal(str(curcrs.is_projected).lower(),datatype=XSD.boolean)))
		ttl.add((crsuri, GEOCRS.isGeocentric, Literal(str(curcrs.is_geocentric).lower(),datatype=XSD.boolean)))
		ttl.add((crsuri, GEOCRS.isGeographic, Literal(str(curcrs.is_geographic).lower(),datatype=XSD.boolean)))
		if curcrs.utm_zone is not None:
			ttl.add((crsuri,GEOCRS.utm_zone, Literal(str(curcrs.utm_zone),datatype=XSD.string)))
		if curcrs.to_proj4() is not None:
			ttl.add((crsuri,GEOCRS.asProj4, Literal(curcrs.to_proj4().strip().replace("\"","'"),datatype=XSD.string)))
		if curcrs.to_json() is not None:
			ttl.add((crsuri,GEOCRS.asProjJSON, Literal(str(curcrs.to_json().strip().replace("\"","'")),datatype=XSD.string)))
		if wkt!="":
			ttl.add((crsuri, GEOCRS.asWKT, Literal(wkt,datatype=GEOCRS.wktLiteral)))
		ttl.add((crsuri, GEOCRS.epsgCode,Literal("EPSG:"+epsgcode,datatype=XSD.string)))
		return ttl

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
