#Clase que define todo lo necesario para un equipo
from random import randrange
class Equipo:
	"""docstring for Equipo"""

	#Atributos de la clase equipo
	peso = 0
	nombre = ""
	numero = 0
	#Estadisticas necesarias
	posicion = 0
	pJugados = 0
	pGanados = 0
	pEmpatados = 0
	pPerdidos = 0
	golFavor = 0
	golContra = 0
	difGoles = 0
	puntos = 0

	#Constructor de la clase
	def __init__(self, peso, nombre, numero):
		self.numero
		self.peso = peso
		self.nombre = nombre
		self.posicion = 0
		self.pJugados = 0
		self.pGanados = 0
		self.pEmpatados = 0
		self.pPerdidos = 0
		self.golFavor = 0
		self.golContra = 0
		self.difGoles = 0
		self.puntos = 0

	def jugarPartido(self):
		goles = randrange(5)
		self.golFavor = goles
		self.pJugados = self.pJugados + 1
		return goles



