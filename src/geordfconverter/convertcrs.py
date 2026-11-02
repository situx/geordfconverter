
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
units["m"] = f"{OM}meter"
units["metre"] = f"{OM}metre"
units["grad"] = f"{OM}degree"
units["degree"] = f"{OM}degree"
units["ft"] = f"{OM}foot"
units["us-ft"] = f"{OM}usfoot"
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
spheroids["GRS80"] = f"{GEOCRSGEOD}GRS1980"
spheroids["GRS 80"] = f"{GEOCRSGEOD}GRS1980"
spheroids["GRS67"] = f"{GEOCRSGEOD}GRS67"
spheroids["GRS 1967"] = f"{GEOCRSGEOD}GRS67"
spheroids["GRS 1967 Modified"] = f"{GEOCRSGEOD}GRS67Modified"
spheroids["GRS 67"] = f"{GEOCRSGEOD}GRS67"
spheroids["GRS1980"] = f"{GEOCRSGEOD}GRS1980"
spheroids["GRS 1980"] = f"{GEOCRSGEOD}GRS1980"
spheroids["NWL 9D"] = f"{GEOCRSGEOD}NWL9D"
spheroids["PZ-90"] = f"{GEOCRSGEOD}PZ90"
spheroids["Airy 1830"] = f"{GEOCRSGEOD}Airy1830"
spheroids["Airy Modified 1849"] = f"{GEOCRSGEOD}AiryModified1849"
spheroids["intl"] = f"{GEOCRSGEOD}International1924"
spheroids["aust_SA"] = f"{GEOCRSGEOD}AustralianNationalSpheroid"
spheroids["Australian National Spheroid"] = f"{GEOCRSGEOD}AustralianNationalSpheroid"
spheroids["International 1924"] = f"{GEOCRSGEOD}International1924"
spheroids["clrk"] = f"{GEOCRSGEOD}Clarke1866"
spheroids["War Office"] = f"{GEOCRSGEOD}WarOffice"
spheroids["evrst30"] = f"{GEOCRSGEOD}Everest1930"
spheroids["clrk66"] = f"{GEOCRSGEOD}Clarke1866"
spheroids["Plessis 1817"] = f"{GEOCRSGEOD}Plessis1817"
spheroids["Danish 1876"] = f"{GEOCRSGEOD}Danish1876"
spheroids["Struve 1860"] = f"{GEOCRSGEOD}Struve1860"
spheroids["IAG 1975"] = f"{GEOCRSGEOD}IAG1975"
spheroids["Clarke 1866"] = f"{GEOCRSGEOD}Clarke1866"
spheroids["Clarke 1858"] = f"{GEOCRSGEOD}Clarke1858"
spheroids["Clarke 1880"] = f"{GEOCRSGEOD}Clarke1880"
spheroids["Helmert 1906"] = f"{GEOCRSGEOD}Helmert1906"
spheroids["Moon_2000_IAU_IAG"] = f"{GEOCRSGEOD}Moon2000_IAU_IAG"
spheroids["CGCS2000"] = f"{GEOCRSGEOD}CGCS2000"
spheroids["GSK-2011"] = f"{GEOCRSGEOD}GSK2011"
spheroids["Zach 1812"] = f"{GEOCRSGEOD}Zach1812"
spheroids["Hough 1960"] = f"{GEOCRSGEOD}Hough1960"
spheroids["Hughes 1980"] = f"{GEOCRSGEOD}Hughes1980"
spheroids["Indonesian National Spheroid"] = f"{GEOCRSGEOD}IndonesianNationalSpheroid"
spheroids["clrk80"] = f"{GEOCRSGEOD}Clarke1880RGS"
spheroids["Clarke 1880 (Arc)"] = f"{GEOCRSGEOD}Clarke1880ARC"
spheroids["Clarke 1880 (RGS)"] = f"{GEOCRSGEOD}Clarke1880RGS"
spheroids["Clarke 1880 (IGN)"] = f"{GEOCRSGEOD}Clarke1880IGN"
spheroids["clrk80ign"] = f"{GEOCRSGEOD}Clarke1880IGN"
spheroids["WGS66"] = f"{GEOCRSGEOD}WGS66"
spheroids["WGS 66"] = f"{GEOCRSGEOD}WGS66"
spheroids["WGS72"] = f"{GEOCRSGEOD}WGS72"
spheroids["WGS 72"] = f"{GEOCRSGEOD}WGS72"
spheroids["WGS84"] = f"{GEOCRSGEOD}WGS84"
spheroids["WGS 84"] = f"{GEOCRSGEOD}WGS84"
spheroids["Krassowsky 1940"] = f"{GEOCRSGEOD}Krassowsky1940"
spheroids["krass"] = f"{GEOCRSGEOD}Krassowsky1940"
spheroids["Bessel 1841"] = f"{GEOCRSGEOD}Bessel1841"
spheroids["bessel"] = f"{GEOCRSGEOD}Bessel1841"
spheroids["Bessel Modified"] = f"{GEOCRSGEOD}BesselModified"
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
		self.ttlhead = (
			"@prefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> .\n"
			"@prefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> .\n"
			"@prefix owl: <http://www.w3.org/2002/07/owl#> .\n"
			"@prefix xsd: <http://www.w3.org/2001/XMLSchema#> .\n"
			"@prefix skos: <http://www.w3.org/2004/02/skos/core#> .\n"
			"@prefix prov: <http://www.w3.org/ns/prov-o/> .\n"
			"@prefix geoepsg: <http://www.opengis.net/def/crs/EPSG/0/> .\n"
			"@prefix geo: <http://www.opengis.net/ont/geosparql#> .\n"
			"@prefix geocrs: <http://www.opengis.net/ont/crs/> .\n"
			"@prefix geocrsdatum: <http://www.opengis.net/ont/crs/datum/> .\n"
			"@prefix geocrsisbody: <http://www.opengis.net/ont/crs/isbody/> .\n"
			"@prefix geocrsgrid: <http://www.opengis.net/ont/crs/grid/> .\n"
			"@prefix geocrsproj: <http://www.opengis.net/ont/crs/proj/> .\n"
			"@prefix geocrsaxis: <http://www.opengis.net/ont/crs/cs/axis/> .\n"
			"@prefix geocrsgeod: <http://www.opengis.net/ont/crs/geod/> .\n"
			"@prefix geocrsaou: <http://www.opengis.net/ont/crs/areaofuse/> .\n"
			"@prefix geocrsmeridian: <http://www.opengis.net/ont/crs/primeMeridian/> .\n"
			"@prefix geocrsoperation: <http://www.opengis.net/ont/crs/operation/> .\n"
			"@prefix geocs: <http://www.opengis.net/ont/crs/cs/> .\n"
			"@prefix dc: <http://purl.org/dc/elements/1.1/> .\n"
			"@prefix wd: <http://www.wikidata.org/entity/> .\n"
			"@prefix om: <http://www.ontology-of-units-of-measure.org/resource/om-2/> .\n"
		)

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
			print(f"EPSG: {epsgcode}")
			ttl+=ConvertCRS.crsToTTL(ttl, curcrs, epsgcode, 1, None)
		except:
			print(f"Could not parse EPSG code {epsgcode}")
		return ttl

	@staticmethod
	def convertCRSFromWKTStringSet(wkt,ttl, authcode=None):
		if authcode!=None and "EPSG:" in authcode:
			authcode=authcode.replace("EPSG:","")
		try:
			#print("WKT " + str(wkt), MESSAGE_CATEGORY, Qgis.Info)
			curcrs=CRS.from_wkt(wkt)
			print(f"Parsed WKT {curcrs}")
			if authcode!=None and authcode!="":
				res=ConvertCRS.crsToTTL(ttl, curcrs, authcode, 1, None)
			else:
				res=ConvertCRS.crsToTTL(ttl, curcrs, "WKT", 1, None)
			print(f"Parsed WKT Res {res}")
			ttl=res
		except:
			print(f"Could not parse WKT {wkt}")
		return ttl

	@staticmethod
	def convertCRSFromWKTString(wkt,ttl, authcode=None):
		set=ConvertCRS.convertCRSFromWKTStringSet(wkt,ttl, authcode)
		return "".join(set)

	@staticmethod
	def crsToTTL(ttl,curcrs,x,geodcounter,crsclass):
		epsgcode=str(x)
		csuri=URIRef(f"{GEOEPSG}{epsgcode}_cs")
		crsuri=URIRef(f"{GEOEPSG}{x}")
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
				ttl.add((crsuri, GEOCRS.includesSRS,URIRef(f"{GEOEPSG}{subcrs.to_epsg()}")))
		else:
			ttl.add((crsuri, RDF.type, GEOCRS.CRS))
		ttl.add((crsuri, RDF.type, PROV.Entity))
		ttl.add((crsuri, GEOCRS.isApplicableTo, URIRef(f"{GEOCRSISBODY}Earth")))
		ttl.add((crsuri, RDF.type, OWL.NamedIndividual))
		ttl.add((crsuri, RDFS.label, Literal(curcrs.name.strip(),lang="en")))
		ttl.add((crsuri, GEOCRS.isBound, Literal(str(curcrs.is_bound).lower(),datatype=XSD.boolean)))
		if curcrs.coordinate_system is not None and curcrs.coordinate_system.name in coordinatesystem:
			ttl.add((csuri, RDF.type, coordinatesystem[curcrs.coordinate_system.name]))
			if len(curcrs.coordinate_system.axis_list)==2:
				ttl.add((csuri, RDF.type, GEOCRS.PlanarCoordinateSystem))
			elif len(curcrs.coordinate_system.axis_list)==3:
				ttl.add((csuri, RDF.type, URIRef(f"{GEOCRS}3DCoordinateSystem")))
			ttl.add((csuri, RDFS.label, Literal(f"EPSG:{epsgcode} CS: {curcrs.coordinate_system.name}")))
			if curcrs.coordinate_system.remarks is not None:
				ttl.add((csuri, RDFS.comment, Literal(str(curcrs.coordinate_system.remarks),lang="en")))
			if curcrs.coordinate_system.scope is not None:
				ttl.add((csuri, GEOCRS.scope,  Literal(str(curcrs.coordinate_system.scope),datatype=XSD.string)))
			for axis in curcrs.coordinate_system.axis_list:
				axisid=f"{axis.name.replace(' ','_').replace('(','_').replace(')','_').replace('/','_').replace(chr(39),'_')}_{axis.unit_name.replace(' ','_').replace('(','_').replace(')','_').replace('/','_').replace(chr(39),'_')}_{axis.direction.replace(' ','_').replace('(','_').replace(')','_').replace('/','_').replace(chr(39),'_')}"
				axisuri=URIRef(f"{GEOCRSAXIS}{axisid}")
				ttl.add((csuri, GEOCRS.axis, axisuri))
				ttl.add((axisuri, RDF.type, GEOCRS.CoordinateSystemAxis))
				ttl.add((axisuri, GEOCRS.direction, URIRef(f"{GEOCRS}{axis.direction}")))
				ttl.add((axisuri, GEOCRS.abbreviation, Literal(str(axis.abbrev).replace("\"","'"),datatype=XSD.string)))
				ttl.add((axisuri, GEOCRS.unit_conversion_factor, Literal(str(axis.unit_conversion_factor),datatype=XSD.double)))
				ttl.add((axisuri, GEOCRS.unit_auth_code,Literal(str(axis.unit_auth_code),datatype=XSD.string)))
				ttl.add((axisuri, GEOCRS.unit_code, Literal(str(axis.unit_code),datatype=XSD.string)))
				ttl.add((URIRef(f"{GEOCRSAXIS}{axis.direction}"), RDF.type, GEOCRS.AxisDirection))
				if axis.unit_name in units:
					ttl.add((axisuri, GEOCRS.unit, URIRef(units[axis.unit_name])))
					ttl.add((axisuri, RDFS.label, Literal(f"{axis.name} ({ConvertCRS.labelFromURI(str(units[axis.unit_name]))})",lang="en")))
				else:
					ttl.add((axisuri,GEOCRS.unit, Literal(str(axis.unit_name),datatype=XSD.string)))
					ttl.add((axisuri, RDFS.label, Literal(f"{axis.name} ({axis.unit_name})",lang="en")))
			ttl.add((csuri, GEOCRS.asWKT, Literal(str(curcrs.coordinate_system.to_wkt()).replace("\"","'").replace("\n",""))))
			ttl.add((csuri, GEOCRS.asProjJSON, Literal(str(curcrs.coordinate_system.to_json()).replace("\"","'").replace("\n",""))))
			ttl.add((crsuri,GEOCRS.coordinateSystem, URIRef(f"{GEOEPSG}{epsgcode}_cs")))
		elif curcrs.coordinate_system is not None:
			ttl.add((crsuri, GEOCRS.coordinateSystem, Literal(str(curcrs.coordinate_system),datatype=XSD.string)))
		if curcrs.source_crs is not None:
			ttl.add((crsuri, GEOCRS.sourceCRS, URIRef(f"{GEOEPSG}{curcrs.source_crs.to_epsg()}")))
		if curcrs.target_crs is not None:
			ttl.add((crsuri, GEOCRS.targetCRS, URIRef(f"{GEOEPSG}{curcrs.target_crs.to_epsg()}")))
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
			ttl.add((crsuri, GEOCRS.area_of_use, URIRef(f"{GEOEPSG}{epsgcode}_area_of_use")))
			ttl.add((URIRef(f"{GEOEPSG}{epsgcode}_area_of_use"), RDF.type, GEOCRS.AreaOfUse))
			ttl.add((URIRef(f"{GEOEPSG}{epsgcode}_area_of_use"), RDFS.label,  Literal(str(curcrs.area_of_use.name).replace("\"","'"),lang="en")))
			#b = box(curcrs.area_of_use.west, curcrs.area_of_use.south, curcrs.area_of_use.east, curcrs.area_of_use.north)
			#ttl.add(crsuri+"_area_of_use"+" geocrs:extent   \"<http://www.opengis.net/def/crs/OGC/1.3/CRS84> "+str(b.wkt)+"\"^^geo:wktLiteral . \n")
			#\"ENVELOPE("+str(curcrs.area_of_use.west)+" "+str(curcrs.area_of_use.south)+","+str(curcrs.area_of_use.east)+" "+str(curcrs.area_of_use.north)+")\"^^geo:wktLiteral . \n")
		if curcrs.get_geod() is not None:
			geoid= f"{GEOCRSGEOD}{geodcounter}"
			if curcrs.datum.ellipsoid is not None:
				if curcrs.datum.ellipsoid.name in spheroids:
					geoid=URIRef(spheroids[curcrs.datum.ellipsoid.name])
					ttl.add((geoid, RDF.type, GEOCRS.Ellipsoid))
					ttl.add((geoid, RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
					ttl.add((geoid, GEOCRS.approximates, URIRef(f"{GEOCRSISBODY}Earth")))
				elif curcrs.get_geod().sphere:
					geoid=URIRef(f"{GEOCRSGEOD}{str(curcrs.datum.ellipsoid.name).replace(' ','_').replace('(','_').replace(')','_')}")
					ttl.add((geoid, RDF.type, GEOCRS.Sphere))
					ttl.add((geoid, RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
					ttl.add((geoid, GEOCRS.approximates, URIRef(f"{GEOCRSISBODY}Earth")))
				else:
					geoid=URIRef(f"{GEOCRSGEOD}{str(curcrs.datum.ellipsoid.name).replace(' ','_').replace('(','_').replace(')','_')}")
					ttl.add((geoid, RDF.type, GEOCRS.Geoid))
					ttl.add((geoid, RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
					ttl.add((geoid, GEOCRS.approximates, URIRef(f"{GEOCRSISBODY}Earth")))
			else:
				ttl.add((crsuri, GEOCRS.ellipsoid, URIRef(f"{GEOCRSGEOD}{geodcounter}")))
				ttl.add((URIRef(f"{GEOCRSGEOD}{geodcounter}"), RDF.type, GEOCRS.Geoid))
				ttl.add((geoid, RDFS.label, Literal(f"Geoid {geodcounter}",lang="en")))
				ttl.add((geoid, GEOCRS.approximates, URIRef(f"{GEOCRSISBODY}Earth")))
			ttl.add((geoid, SKOS.definition, Literal(str(curcrs.get_geod().initstring),datatype=XSD.string)))
			ttl.add((geoid, GEOCRS.eccentricity, Literal(str(curcrs.get_geod().es),datatype=XSD.double)))
			ttl.add((geoid, GEOCRS.isSphere, Literal(str(curcrs.get_geod().sphere),datatype=XSD.boolean)))
			ttl.add((geoid, GEOCRS.semiMajorAxis, Literal(str(curcrs.get_geod().a),datatype=XSD.string)))
			ttl.add((geoid, GEOCRS.semiMinorAxis, Literal(str(curcrs.get_geod().b),datatype=XSD.string)))
			ttl.add((geoid, GEOCRS.flatteningParameter, Literal(str(curcrs.get_geod().f),datatype=XSD.double)))
			geodcounter+=1
		if curcrs.coordinate_operation is not None:
			coordoperationid=curcrs.coordinate_operation.name.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_").replace(",","_").replace("&","and").strip()
			csopuri=URIRef(f"{GEOCRSOPERATION}{coordoperationid}")
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
				ttl.add((csopuri,GEOCRS.area_of_use,URIRef(f"{GEOCRSAOU}{coordoperationid}_area_of_use")))
				ttl.add(URIRef(f"{GEOCRSAOU}{coordoperationid}_area_of_use"),RDF.type, GEOCRS.AreaOfUse)
				ttl.add(URIRef(f"{GEOCRSAOU}{coordoperationid}_area_of_use"), RDFS.label, Literal(str(curcrs.coordinate_operation.area_of_use.name).replace("\"","'"),lang="en"))
				#b = box(curcrs.coordinate_operation.area_of_use.west, curcrs.coordinate_operation.area_of_use.south, curcrs.coordinate_operation.area_of_use.east, curcrs.coordinate_operation.area_of_use.north)
				#ttl.add("geocrsaou:"+str(coordoperationid)+"_area_of_use geocrs:extent \"<http://www.opengis.net/def/crs/OGC/1.3/CRS84> "+str(b.wkt)+"\"^^geo:wktLiteral . \n")
				#ENVELOPE("+str(curcrs.coordinate_operation.area_of_use.west)+" "+str(curcrs.coordinate_operation.area_of_use.south)+","+str(curcrs.coordinate_operation.area_of_use.east)+" "+str(curcrs.coordinate_operation.area_of_use.north)+")\"^^geocrs:wktLiteral . \n")
			if curcrs.coordinate_operation.towgs84 is not None:
				print(curcrs.coordinate_operation.towgs84)
			for par in curcrs.coordinate_operation.params:
				param_uri = f"{GEOCRS}{str(par.name)[0].lower()}{str(par.name).title().replace(' ','')[1:]}"
				ttl.add(URIRef(param_uri), RDF.type, OWL.DatatypeProperty)
				ttl.add(URIRef(param_uri), RDFS.range, XSD.double)
				ttl.add(URIRef(param_uri), RDFS.domain, GEOCRS.CoordinateOperation)
				ttl.add(URIRef(param_uri), RDFS.label, Literal(str(par.name),lang="en"))
				ttl.add(csopuri, URIRef(param_uri),Literal(str(par.value),datatype=XSD.double))
			for grid in curcrs.coordinate_operation.grids:
				grid_uri = f"{GEOCRSGRID}{str(grid.name).replace(' ','_')}"
				ttl.add((csopuri, GEOCRS.grid, URIRef(grid_uri)))
				ttl.add((URIRef(grid_uri), RDF.type, GEOCRS.Grid))
				ttl.add((URIRef(grid_uri), RDFS.label, Literal(str(grid.full_name),lang="en")))
				ttl.add((URIRef(grid_uri), RDFS.label, Literal(str(grid.short_name),lang="en")))
				ttl.add((URIRef(grid_uri),GEOCRS.open_license, Literal(str(grid.open_license),datatype=XSD.boolean)))
				ttl.add((URIRef(grid_uri), RDFS.comment, Literal(str(grid.url),lang="en")))
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
			ttl.add((csopuri), RDFS.label, Literal(f"{curcrs.coordinate_operation.name}: {curcrs.coordinate_operation.method_name}",lang="en"))
		if curcrs.datum is not None:
			datumid=str(curcrs.datum.name.replace(" ","_").replace("(","_").replace(")","_").replace("/","_").replace("'","_").replace("+","_plus").replace("[","_").replace("]","_"))
			datum_uri = f"{GEOCRSDATUM}{datumid}"
			ttl.add(crsuri, GEOCRS.datum, URIRef(datum_uri))
			if "Geodetic Reference Frame" in curcrs.datum.type_name:
				ttl.add((URIRef(datum_uri), RDF.type, GEOCRS.GeodeticReferenceFrame))
			elif "Dynamic Vertical Reference Frame" in curcrs.datum.type_name:
				ttl.add((URIRef(datum_uri), RDF.type, GEOCRS.DynamicVerticalReferenceFrame))
			elif "Vertical Reference Frame" in curcrs.datum.type_name:
				ttl.add((URIRef(datum_uri), RDF.type, GEOCRS.VerticalReferenceFrame))
			else:
				print(curcrs.datum.type_name)
				ttl.add((URIRef(datum_uri),RDF.type, GEOCRS.Datum))
			ttl.add((URIRef(f"{GEOCRSDATUM}{datumid}"), RDFS.label, Literal(f"Datum: {curcrs.datum.name}",lang="en")))
			if curcrs.datum.remarks is not None:
				ttl.add((URIRef(datum_uri), RDFS.comment, Literal(str(curcrs.datum.remarks),lang="en")))
			if curcrs.datum.scope is not None:
				ttl.add((URIRef(datum_uri), GEOCRS.scope, Literal(str(curcrs.datum.scope),datatype=XSD.string)))
				if "," in curcrs.datum.scope:
					for scp in curcrs.datum.scope.split(","):
						#print("Scope: "+scp)
						if scp.lower().strip().replace(".","") in scope:
							ttl.add((URIRef(datum_uri), GEOCRS.usage,URIRef(scope[scp.lower().strip().replace(".","")])))
							ttl.add((URIRef(scope[scp.lower().strip().replace(".","")]),RDFS.subClassOf, GEOCRS.SRSApplication))
						else:
							ttl.add((URIRef(datum_uri), GEOCRS.usage, Literal(str(curcrs.datum.scope),datatype=XSD.string)))
				print(str(curcrs.datum.scope))
			if curcrs.datum.ellipsoid is not None and curcrs.datum.ellipsoid.name in spheroids:
				ttl.add((URIRef(datum_uri), GEOCRS.ellipse, URIRef(spheroids[curcrs.datum.ellipsoid.name])))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), RDFS.label, Literal(str(curcrs.datum.ellipsoid.name),lang="en")))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), RDF.type, GEOCRS.Ellipsoid))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), GEOCRS.inverse_flattening, Literal(str(curcrs.datum.ellipsoid.inverse_flattening),datatype=XSD.double)))
				if curcrs.datum.ellipsoid.remarks is not None:
					ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), RDFS.comment, Literal(str(curcrs.datum.ellipsoid.remarks),datatype=XSD.string)))
				ttl.add((URIRef(spheroids[curcrs.datum.ellipsoid.name]), GEOCRS.is_semi_minor_computed, Literal(str(curcrs.datum.ellipsoid.is_semi_minor_computed).lower(),datatype=XSD.boolean)))
			elif curcrs.datum.ellipsoid is not None:
				ttl.add((URIRef(datum_uri), GEOCRS.ellipse, Literal(curcrs.datum.ellipsoid.name,datatype=XSD.string)))
			if curcrs.prime_meridian is not None:
				ttl.add((URIRef(datum_uri), GEOCRS.primeMeridian,URIRef(f"{GEOCRSMERIDIAN}{curcrs.prime_meridian.name.replace(' ', '')}")))
				prime_meridian_uri = f"{GEOCRSMERIDIAN}{curcrs.prime_meridian.name.replace(' ', '')}"
				ttl.add((URIRef(prime_meridian_uri), RDF.type, GEOCRS.PrimeMeridian))
				ttl.add((URIRef(prime_meridian_uri), RDFS.label, Literal(curcrs.prime_meridian.name,lang="en")))
				ttl.add((URIRef(prime_meridian_uri), GEOCRS.longitude, Literal(str(curcrs.prime_meridian.longitude),datatype=XSD.double)))
				if curcrs.prime_meridian.unit_name in units:
					ttl.add((URIRef(prime_meridian_uri), GEOCRS.unit, URIRef(f"{OM}{units[curcrs.prime_meridian.unit_name]}")))
					ttl.add((URIRef(units[curcrs.prime_meridian.unit_name]), RDF.type, URIRef(f"{OM}Unit")))
				else:
					ttl.add((URIRef(prime_meridian_uri), GEOCRS.unit, Literal(str(curcrs.prime_meridian.unit_name),datatype=XSD.string)))
				ttl.add((URIRef(prime_meridian_uri), GEOCRS.asWKT, Literal(str(curcrs.prime_meridian.to_wkt()).replace("\"","'").replace("\n",""),datatype=XSD.string)))
				ttl.add((URIRef(prime_meridian_uri), GEOCRS.asProjJSON, Literal(str(curcrs.prime_meridian.to_json()).replace("\"","'").replace("\n",""),datatype=XSD.string)))
				if curcrs.prime_meridian.remarks is not None:
					ttl.add((URIRef(prime_meridian_uri),RDFS.comment,Literal(str(curcrs.prime_meridian.remarks),lang="en")))
				if curcrs.prime_meridian.scope is not None:
					ttl.add((URIRef(prime_meridian_uri), GEOCRS.scope, Literal(str(curcrs.prime_meridian.scope),datatype=XSD.string)))
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
		ttl.add((crsuri, GEOCRS.epsgCode,Literal(f"EPSG:{epsgcode}",datatype=XSD.string)))
		return ttl
