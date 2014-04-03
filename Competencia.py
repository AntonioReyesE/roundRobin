#Clase que calcula las jornadas y termina todos los partidos
import operator
from Equipo import *
from Lector import *
from rounInter import *
from Juego import *


class Competencia(object):
	"""docstring for Competencia"""
	def __init__(self, arg):
		super(Competencia, self).__init__()
		self.arg = arg
		self.lec = Lector("torneo.txt")
		self.lec.lee()
		self.equipos = []
		self.round = RoundRobin(self.lec.nEquipos)
		for i in range(0,self.lec.nEquipos):
			self.equipos.append(Equipo(self.lec.peso[i], self.lec.equipo[i], i))


	def jugarJornada(self):
		
		file = open("jornadas.txt","w")
		file.write("#    Equipo    PJ    PG   PE   PP   GF   GC    DIF   PTS\n")
		#file.close()
		self.arreglo = []
		for i in range(1,self.lec.nEquipos):
			for j in range(0,self.lec.nEquipos):
				x = self.round.matrix[j][i]
				#print x
				Juego(self.equipos[j], self.equipos[x], self.lec.pGanar, self.lec.pEmpatar, self.lec.pPerder)
				#file.write("#    Equipo    PJ    PG   PE   PP   GF   GC    DIF   PTS\n")
			#print ""

			for x in xrange(0,self.lec.nEquipos):
				a = self.equipos[x]
				self.arreglo.append([a.nombre, a.pJugados, a.pGanados, a.pPerdidos, a.golFavor, a.golContra, a.difGoles, a.puntos])
		#self.ordenar()

  	def ordenar(self):
  		sorted(self.arreglo,key = lambda x:x[7], reverse = True)
  		for i in range(0,len(self.arreglo[0])):
			print self.arreglo[i]
c = Competencia(0)
c.jugarJornada()
c.ordenar()