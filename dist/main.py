# -*- encoding: utf-8 -*-
from Competencia import *
from Lector2 import *
projecto = Competencia()
equipo = open("torneo.txt","r")
print "Bienvenido a la aplicacion para calculo de juegos y temporadas de futbol del torneo "+str(equipo.readline())
equipos=int(equipo.readline())
equipo.close()
menu = True;
print ' Favor de introducir los comandos que desee:'
print ' Para ver los juegos introduce ---> "1"'
print ' Para ver las estadísticas introduce --> "2"'
print ' Escribe "salir" para salir del programa'
print ""


while menu:
	opcion = raw_input(">>>")
	if opcion == '1':
		juegos = open("goles.txt","r")
		print("Introduce  1 para desplegar los resultados la jornada que quiere ver")
		print("Introduce  2 para desplegar todos los resultados del torneo")
		opcion2 = raw_input(">>>")
		if opcion2 =='1':
			mul = str(raw_input("introduce la jornada que quieres ver>>>"))
			n=0
			print juegos.readline()
			global equipos
			x=equipos
			for i in range((equipos*int(mul)+int(mul))):
				juegos.readline()
			while(n<equipos):
				print juegos.readline()
				n = n+1
		elif opcion2 == '2':
			for line in juegos:
				print line,
		juegos.close()
	elif opcion == '2':
		jornadas = open("jornadas.txt","r")
		print("Introduce  1 para desplegar las estadísticas la jornada que quiere ver")
		print("Introduce  2 para desplegar todas las estadísticas del torneo")
		opcion2 = raw_input(">>>")
		if opcion2 =='1':
			mul = str(raw_input("introduce la jornada que quieres ver>>>"))
			n=0
			print jornadas.readline()
			global equipos
			x=equipos
			for i in range((equipos*int(mul)+int(mul))):
				jornadas.readline()
			while(n<equipos):
				print jornadas.readline()
				n = n+1

	
		elif opcion2 == '2':
			for line in jornadas:
				print line,
		jornadas.close()
	elif opcion == 'salir':
		menu = False;
		print " Adios..."
	else:
		print "revisa la opción que escogiste"
	print ' Favor de introducir los comandos que desee:'
	print ' Para ver los juegos introduce ---> "1"'	
	print ' Para ver las estadísticas introduce --> "2"'
	print ' Escribe "salir" para salir del programa'
	print ""
		
