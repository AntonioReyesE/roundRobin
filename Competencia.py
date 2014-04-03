#Clase que calcula las jornadas y termina todos los partidos
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
		print self.lec.pGanar 
		print self.lec.pEmpatar
		print self.lec.pPerder
		file = open("jornadas.txt","w")
		file.write("#    Equipo    PJ    PG   PE   PP   GF   GC    DIF   PTS")

		for i in range(1,self.lec.nEquipos):
			for j in range(0,self.lec.nEquipos):
				x = self.round.matrix[j][i]
				j = Juego(self.equipos[i], self.equipos[x], self.lec.pGanar, self.lec.pEmpatar, self.lec.pPerder)
				






c = Competencia(0)
c.jugarJornada()