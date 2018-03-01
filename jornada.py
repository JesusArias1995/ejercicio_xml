from funciones import jornada, local, visitante

jornada=jornada()

local=local(jornada)
visitante=visitante(jornada)

for i, x in zip(local,visitante):
	print(i, "-", x)