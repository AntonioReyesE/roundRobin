from Competencia import *
from Lector2 import *

print "Bienvenido a la aplicacion para calculo de juegos y temporadas de futbol"

print "ingresa por favor el número de equipos que van a participar"
n = raw_input("-->")
comp = Competencia(n)
lec = Lector2()
print "¿Deseas ver el total de resultados o solamente 1 jornada? 1 = todos, 2 = una jornada"
a = raw_input("-->")
if a:
	print "¿De que jornada quieres ver el resultado?: "
	c = raw_input("-->")
else:
	c = 0
print "¿Deseas ver las estadisticas, los resultados de los juegos o ambos?"
b = raw_input("-->")

if :
	pass