# -*- encoding: utf-8 -*-
#Clase que calcula las jornadas y termina todos los partidos
import operator
from Equipo import *
from Lector import *
from rounInter import *
from Juego import *


class Competencia(object):
	"""docstring for Competencia"""
	def __init__(self):
		super(Competencia, self).__init__()
		
		self.lec = Lector("torneo.txt")
		self.lec.lee()
		self.equipos = []
		self.round = RoundRobin(self.lec.nEquipos)
		for i in range(0,self.lec.nEquipos):
			self.equipos.append(Equipo(self.lec.peso[i], self.lec.equipo[i], i))


	def jugarJornada(self):
		
		
		
		self.arreglo = []
		self.juegos =[]
		for i in range(1,self.lec.nEquipos):
			for j in range(0,self.lec.nEquipos):
				x = self.round.matrix[j][i]
				#print x
				

				
				temp = Juego(self.equipos[j], self.equipos[x], self.lec.pGanar, self.lec.pEmpatar, self.lec.pPerder)
				self.juegos.append([self.equipos[j].nombre, self.equipos[x].nombre,temp.gol1,temp.gol2])
				#file.write("#    Equipo    PJ    PG   PE   PP   GF   GC    DIF   PTS\n")
			#print ""

			for x in xrange(0,self.lec.nEquipos):
				a = self.equipos[x]
				self.arreglo.append([a.nombre, a.pJugados, a.pGanados, a.pPerdidos, a.golFavor, a.golContra, a.difGoles, a.puntos])
			#file.write("\n")
			
		#self.escribeTxt()
		#self.ordenar()
		#print self.arreglo
  	def ordenar(self):
  		#print len(self.arreglo[0])
  		#c = 1;
  		for k in range (1,(len(self.arreglo)/self.lec.nEquipos)+1):
  			for i in range(len(self.arreglo[0])*(k-1),len(self.arreglo[0])*k):
  				#print i
  				for j in range(i+1*k,len(self.arreglo[0])*k):
  					
					if(self.arreglo[i][7]<self.arreglo[j][7]):
						temp = self.arreglo[i]
						self.arreglo[i] = self.arreglo[j]
						self.arreglo[j] =temp 
					elif (self.arreglo[i][7]==self.arreglo[j][7]):
						if (self.arreglo[i][4]>self.arreglo[j][4]):
							temp = self.arreglo[i]
							self.arreglo[i] = self.arreglo[j]
							self.arreglo[j] =temp
							
				#c=c+1

		
	def escribeTxt(self):
		self.ordenar()
		c = 1
		file = open("jornadas.txt","w")
		#file = open("jornadas.txt","w")
		file.write("#    Equipo    PJ    PG   PE   PP   GF   GC    DIF   PTS\n")
		for i in range(0,len(self.arreglo)):
			file.write(""+str((c)))
  			for j in range(0,len(self.arreglo[i])):
				file.write("        "+str(self.arreglo[i][j]))
				#print j
			file.write("\n")
			
			if(c>=self.lec.nEquipos):
				c=1
				file.write("\n")
			else:
				c = c+1

		file.close()

	def escribeGol(self):
		c = 1
		file = open("goles.txt","w")
		file.write("visitante   vs    local     marcador   \n")
		for i in range(0,len(self.juegos)):
			file.write(""+str((c)))
  			for j in range(0,len(self.juegos[i])):
				file.write("        "+str(self.juegos[i][j]))
				#print j
			file.write("\n")
			
			if(c>=self.lec.nEquipos):
				c=1
				file.write("\n")
			else:
				c = c+1

		file.close()


c = Competencia()
c.jugarJornada()
c.escribeTxt()
c.escribeGol()
print 
#c.ordenar()