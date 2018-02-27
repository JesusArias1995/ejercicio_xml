def partido_tv(partido):
	nombrelocal=doc.findall("match/local")
	nombrevisitante=doc.finall("match/visitor")
	hora=doc.findall("match/schedule")
	tv=doc.findall("match/channels/name")
	return print(nombrelocal,"-",nombrevisitante, hora, tv)


doc = etree.parse('http://apiclient.resultados-futbol.com/scripts/api/api.php?key=7171673be04cc06aa2426307d8b42836&tz=Europe/Madrid&format=xml&req=matchs&league=1&round=&order=twin&twolegged=1&year=2018')
lista_partidos=partido_tv(doc)
