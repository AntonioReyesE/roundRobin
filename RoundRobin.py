#Clase principal RoundRobin

class RoundRobin(object):
	"""docstring for RoundRobin"""

	tabla = [[]]
	jugadores = 0
	Nequipos = 0
	def __init__(self):
		super(RoundRobin, self).__init__()
		self.tabla = [[-1 for i in range(17)]for j in range(16)]
		self.jugadores = 0
		self.Nequipos = 4
		

	def formarTabla(self, tabla ,inferior, superior):
		#print inferior
		#print str(superior)+" superior"
		#self.printTabla()
		if inferior == superior - 1:
			self.tabla[inferior][0] = superior
			self.tabla[superior][0] = inferior
		else:
			medio = (inferior + superior) / 2
			self.formarTabla(self.tabla, inferior, medio)
			self.formarTabla(self.tabla, medio + 1, superior)
			self.completarTabla(self.tabla, medio + 1, superior, medio, superior - 1, inferior)
			self.completarTabla(self.tabla, inferior, medio, medio, superior - 1, medio + 1)
			

	def completarTabla(self, tabla, equipoInferior, equipoSuperior, diaInferior, diaSuperior, equipoInicial):
		print "equipoInferior: "+str(equipoInferior)+"  equipoSuperior"+str( equipoSuperior) + " diaInferior: "+str( diaInferior)+"diaSuperior: "+str( diaSuperior)+" equipoInicial: "+str( equipoInicial)
		#j = diaInferior
		for j in range(diaInferior,diaSuperior + 1):
			self.tabla[equipoInferior][j] = (equipoInicial + j) - diaInferior
		#i = equipoInferior + 1

		'''El pedo se encuentra en estos for tentativamente'''
		print "Estoy en la funcion"
		for i in range(equipoInferior,equipoSuperior):
			print "Entre al for"
			self.tabla[i][diaInferior] = self.tabla[i -1][diaSuperior]
			
			#w = diaInferior + 1
			for w in xrange(diaInferior ,diaSuperior + 1):
				print "Entre al segundo for"
				self.tabla[i][w] = self.tabla[i - 1][w - 1]

	def calendario(self):
		self.formarTabla(self.tabla, 0, self.Nequipos - 1)

	def printTabla(self):
		print "---------------------------------"
		for i in xrange(0,self.Nequipos):
			for j in range(0,self.Nequipos - 1):
				print self.tabla[i][j],
			print ""
		print "---------------------------------"
