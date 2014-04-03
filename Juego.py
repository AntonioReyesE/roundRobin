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
		self.partido()

	def partido(self):
		gol1 = self.equipo1.jugarPartido()
		gol2 = self.equipo2.jugarPartido()
		self.equipo1.golContra = gol2
		self.equipo2.golContra = gol1
		if gol1 > gol2:
			self.equipo1.pGanados = self.equipo1.pGanados + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pGanar
			self.equipo2.pPerdidos = self.equipo2.pPerdidos + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pPerder
		elif gol2 > gol1:
			self.equipo2.pGanados = self.equipo2.pGanados + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pGanar
			self.equipo1.pPerdidos = self.equipo1.pPerdidos + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pPerder
		else:
			self.equipo1.puntos = self.equipo1.puntos + self.pEmpatar
			self.equipo1.pEmpatados = self.equipo1.pEmpatados + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pEmpatar
			self.equipo2.pEmpatados = self.equipo2.pEmpatados + 1

	'''def penales(self):
		gol1 = randint(0, 5)
		gol2 = randint(0, 5)
		if gol1 > gol2:
			self.equipo1.pGanados = self.equipo1.pGanados + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pGanar
			self.equipo2.pPerdidos = self.equipo2.pPerdidos + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pPerder
		elif gol2 > gol1:
			self.equipo2.pGanados = self.equipo2.pGanados + 1
			self.equipo2.puntos = self.equipo2.puntos + self.pGanar
			self.equipo1.pPerdidos = self.equipo1.pPerdidos + 1
			self.equipo1.puntos = self.equipo1.puntos + self.pPerder
		else:
			penales()'''

		
		