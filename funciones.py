from lxml import etree

def jornada(enlace="Dime el numero de jornada: "):
	jornada=input(enlace)
	url=str("http://apiclient.resultados-futbol.com/scripts/api/api.php?key=7171673be04cc06aa2426307d8b42836&tz=Europe/Madrid&format=xml&req=matchs&league=1&round="+jornada+"&order=twin&twolegged=1&year=2018")
	return url

def local(url):
	loc=[]
	arbol=etree.parse(url)
	for i in arbol.findall("/match/local"):
		loc.append(i.text.replace("\n", ""))
	return loc

def visitante(url):
	vis=[]
	arbol=etree.parse(url)
	for i in arbol.findall("/match/visitor"):
		vis.append(i.text.replace("\n", ""))
	return vis