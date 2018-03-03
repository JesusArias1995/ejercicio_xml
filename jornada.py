from funciones import jornada, local, visitante, resultado, fecha, tv, minuto


print("Elige una opción: ")
print("1. Mostrar partidos de la jornada indicada.")
print("2. Partidos que hay una fecha especificada.")
print("3. Poner equipo y jornada para mostrarnos información.")
print("4. Poner tv y nos dira los partidos que retransmiten por dicho canal.")
print("5. Poner local o visitante y nos mostrara solo los partidos ganados por el señalado.")
print("0. Salir")
print("")
menu=input("Introduce el número de opcion que desea realizar: ")

jornada=jornada(input("Dime la jornada que vas a utilizar, si desea la actual dejelo en blanco: "))

while menu!="0":
	if menu=="1":
		for l, v, r, f, t, m in zip(local(jornada),visitante(jornada),resultado(jornada),fecha(jornada), tv(jornada),minuto(jornada)):
			if r=="x-x":
				print (l, "-", v, f, t)
			elif m=="" and r!="x-x":
				print(l, r, v, "FIN")
			else:
				print(l, r, v, "Min:", m)

		menu=input("Elige otra opcion: ")

	if menu=="2":
		fechas=[]
		for f in fecha(jornada):
			fechas.append(f[0:10])
		for i in set(fechas):
			print (i, fechas.count(i))

		menu=input("Elige otra opcion: ")

	if menu=="3":
		equipo=input("Dime el equipo: ")
		for l, v, r, f, t, m in zip(local(jornada),visitante(jornada),resultado(jornada),fecha(jornada), tv(jornada),minuto(jornada)):
			if l==equipo or v==equipo:	
				if r=="x-x":
					print (l, "-", v, f, t)
				elif m=="" and r!="x-x":
					print(l, r, v, "FIN")
				else:
					print(l, r, v, "Min:", m)

		menu=input("Elige otra opcion: ")

	if menu=="4":
		tele=input("Dime la TV(beIN LaLiga / M. Partidazo / GOL): ")
		for l, v, r, f, t, m in zip(local(jornada),visitante(jornada),resultado(jornada),fecha(jornada), tv(jornada),minuto(jornada)):
			if tele==t:	
				if r=="x-x":
					print (l, "-", v, f)
				elif m=="" and r!="x-x":
					print(l, r, v, "FIN")
				else:
					print(l, r, v, "Min:", m)

		menu=input("Elige otra opcion: ")

	if menu=="5":
		ganados=input("Ganadores de la jornada(local/visitante): ")
		for l, v, r, f, t, m in zip(local(jornada),visitante(jornada),resultado(jornada),fecha(jornada), tv(jornada),minuto(jornada)):
			if ganados=="local":
				if r[0]>r[2]:
					if m=="" and r!="x-x":
						print(l, r, v, "FIN")
					else:
						print(l, r, v, "Min:", m)
			elif ganados=="visitante":
				if r[2]>r[0]:
					if m=="" and r!="x-x":
						print(l, r, v, "FIN")
					else:
						print(l, r, v, "Min:", m)
		menu=input("Elige otra opcion: ")

