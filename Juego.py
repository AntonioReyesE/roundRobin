# -*- encoding: utf-8 -*-
#Clase principal que simula el juego de torneos
from Equipo import *

class Juego(object):
	"""docstring for Juego"""

	def __init__(self, equipo1, equipo2, pGanar, pEmpatar, pPerder):
		self.equipo1 = equipo1
		self.equipo2 = equipo2
		self.pGanar = pGanar
		self.pEmpatar = pEmpatar
		self.pPerder = pPerder
		self.gol1 = 0
		self.gol2 = 0

		self.partido()
		
	def partido(self):
		self.gol1 = self.equipo1.jugarPartido()
		self.gol2 = self.equipo2.jugarPartido()
		self.equipo1.golContra = self.gol2
		self.equipo2.golContra = self.gol1
		if self.gol1 > self.gol2:
			self.equipo1.pGanados = self.equipo1.pGanados + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pGanar
			self.equipo2.pPerdidos = self.equipo2.pPerdidos + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pPerder
			self.equipo2.difGoles = self.equipo2.golFavor - self.equipo2.golContra
			self.equipo1.difGoles = self.equipo1.golFavor - self.equipo1.golContra
		elif self.gol2 > self.gol1:
			self.equipo2.pGanados = self.equipo2.pGanados + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pGanar
			self.equipo1.pPerdidos = self.equipo1.pPerdidos + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pPerder
			self.equipo2.difGoles = self.equipo2.golFavor - self.equipo2.golContra
			self.equipo1.difGoles = self.equipo1.golFavor - self.equipo1.golContra
		else:
			self.equipo1.puntos = self.equipo1.puntos + self.pEmpatar
			self.equipo1.pEmpatados = self.equipo1.pEmpatados + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pEmpatar
			self.equipo2.pEmpatados = self.equipo2.pEmpatados + 1
			self.equipo2.difGoles = self.equipo2.golFavor - self.equipo2.golContra
			self.equipo1.difGoles = self.equipo1.golFavor - self.equipo1.golContra

		#return [self.gol1,self.gol2]

	'''def penales(self):
		self.gol1 = randint(0, 5)
		self.gol2 = randint(0, 5)
		if self.gol1 > self.gol2:
			self.equipo1.pGanados = self.equipo1.pGanados + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pGanar
			self.equipo2.pPerdidos = self.equipo2.pPerdidos + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pPerder
		elif self.gol2 > self.gol1:
			self.equipo2.pGanados = self.equipo2.pGanados + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pGanar
			self.equipo1.pPerdidos = self.equipo1.pPerdidos + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pPerder
		else:
			penales()'''

		
		