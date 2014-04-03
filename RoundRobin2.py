#Clase principal RoundRobin

class RoundRobin2(object):
	"""docstring for RoundRobin"""

	tabla = [[]]
	jugadores = 0
	Nequipos = 0
	contador = 0
	def __init__(self):
		super(RoundRobin2, self).__init__()
		self.tabla = [[0 for i in range(6)]for j in range(5)]
		self.jugadores = 0
		self.Nequipos = 4
		self.contador = 0

	def formarTabla(self, tabla ,inferior, superior):
		if inferior == superior - 1:
			self.tabla[inferior][0] = superior
			self.tabla[superior][0] = inferior
		else:
			medio = (inferior + superior) / 2
			self.formarTabla(self.tabla, inferior, medio)
			self.formarTabla(self.tabla, medio + 1, superior)
			self.completarTabla(self.tabla, medio + 1, superior, medio + 1, superior - 1, medio + 1)
			self.completarTabla(self.tabla, inferior, medio, medio, superior - 1, inferior)


	def completarTabla(self, tabla, equipoInferior, equipoSuperior, diaInferior, diaSuperior, equipoInicial):
		self.contador = self.contador + 1
		print "Contador de llamadas recursivas: "+str(self.contador)
		print "diaInferior: "+str(diaInferior)
		print "diaSuperior: "+str(diaSuperior)
		for i in range(diaInferior,diaSuperior + 1):
			self.tabla[equipoInferior][i] = (equipoInicial + i) - diaInferior
		for j in range(equipoInferior,equipoSuperior):
		 	self.tabla[j][diaInferior] = self.tabla[j - 1][diaSuperior]
		 	for k in range(diaInferior + 1,diaSuperior):
		 		self.tabla[j][k] = self.tabla[j - 1][k - 1]


	def circular(self, ini, fin, x, y):
		lista = []
		for x in xrange(ini,fin):
			lista.append(x)
		for i in range(y,lista.len()):
			for j in range(x,lista.len()):
				self.tabla[y][x] = lista[j]

	def calendario(self):
		self.formarTabla(self.tabla, 0, self.Nequipos - 1)

	def printTabla(self):
		print "---------------------------------"
		for i in xrange(0,self.Nequipos):
			for j in range(0,self.Nequipos - 1):
				print self.tabla[i][j],
			print ""
		print "---------------------------------"
