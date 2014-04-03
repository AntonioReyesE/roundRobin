#Clase que define todo lo necesario para un equipo
class Equipo(object):
	"""docstring for Equipo"""

	#Atributos de la clase equipo
	peso
	nombre
	numero
	#Estadisticas necesarias
	posicion
	pJugados
	pGanados
	pEmpatados
	pPerdidos
	golFavor
	golContra
	difGoles
	puntos

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
		goles = randint(0, 10)
		self.golFavor = goles
		self.pJugados = self.pJugados + 1
		return goles
		




