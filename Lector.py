# -*- encoding: utf-8 -*-
#Clase lector

class Lector(object):

	nombre = ""
	nEquipos = 0
	indicador = 0
	pGanar = 0
	pPerder = 0
	pEmpatar = 0
	equipo = []
	peso = []

	"""docstring for Lector"""
	def __init__(self, path):
		super(Lector, self).__init__()
		self.path = path
		self.nombre = ""
		self.nEquipos = 0
		self.indicador = 0
		self.pGanar = 0
		self.pPerder = 0
		self.pEmpatar = 0
		self.equipo = []
		self.peso = []

	def lee(self):
		f = open(self.path, "r")
		self.nombre = f.readline()
		self.nEquipos = int(f.readline())
		self.indicador = int(f.readline())
		self.pGanar = int(f.readline())
		self.pPerder = int(f.readline())
		self.pEmpatar = int(f.readline())
		x = 0
		while x < self.nEquipos:
			linea = f.readline()
			linea = linea.rstrip("\n")
			y=linea.split(",")
			self.equipo.append(y[0])
			self.peso.append(y[1])
			x = x + 1



