from lxml import etree

def partido_tv(partido):
	for i in doc.findall("/match/local"):
		print(i.text)

jornada=str("")
url=str("http://apiclient.resultados-futbol.com/scripts/api/api.php?key=7171673be04cc06aa2426307d8b42836&tz=Europe/Madrid&format=xml&req=matchs&league=1&round="+jornada+"&order=twin&twolegged=1&year=2018")
doc = etree.parse(url)
lista_partidos=partido_tv(doc)
