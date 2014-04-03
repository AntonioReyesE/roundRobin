#Clase principal que simula el juego de torneos

class Juego(object):
	"""docstring for Juego"""

	equipo1
	equipo2
	pGanar
	pEmpatar
	pPerder

	def __init__(self, equipo1, equipo2, pGanar, pEmpatar, pPerder):
		self.equipo1 = equipo1
		self.equipo2 = equipo2
		self.pGanar = pGanar
		self.pEmpatar = pEmpatar
		self.pPerder = pPerder

	def partido(self):
		gol1 = equipo1.jugarPartido()
		gol2 = equipo2.jugarPartido()
		equipo1.golContra = gol2
		equipo2.golContra = gol1
		if gol1 > gol2:
			equipo1.pGanados = equipo1.pGanados + 1
			equipo1.puntos = equipo1.puntos + self.pGanar
			equipo2.pPerdidos = equipo2.pPerdidos + 1
			equipo2.puntos = equipo2.puntos + self.pPerder
		elif gol2 > gol1:
			equipo2.pGanados = equipo2.pGanados + 1
			equipo2.puntos = equipo2.puntos + self.pGanar
			equipo1.pPerdidos = equipo1.pPerdidos + 1
			equipo1.puntos = equipo1.puntos + self.pPerder
		else:
			equipo1.puntos = equipo1.puntos + self.pEmpatar
			equipo1.pEmpatados = equipo1.pEmpatados + 1
			equipo2.puntos = equipo2.puntos + self.pEmpatar
			equipo2.pEmpatados = equipo2.pEmpatados + 1

	'''def penales(self):
		gol1 = randint(0, 5)
		gol2 = randint(0, 5)
		if gol1 > gol2:
			equipo1.pGanados = equipo1.pGanados + 1
			equipo1.puntos = equipo1.puntos + self.pGanar
			equipo2.pPerdidos = equipo2.pPerdidos + 1
			equipo2.puntos = equipo2.puntos + self.pPerder
		elif gol2 > gol1:
			equipo2.pGanados = equipo2.pGanados + 1
			equipo2.puntos = equipo2.puntos + self.pGanar
			equipo1.pPerdidos = equipo1.pPerdidos + 1
			equipo1.puntos = equipo1.puntos + self.pPerder
		else:
			penales()'''
		
		