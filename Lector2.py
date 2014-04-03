#Clase que lee los resultados especificos

class Lector2(object):
	"""docstring for Lector2"""
	def __init__(self):
		self.path1 = "torneo.txt"
		self.path2 = "goles.txt"

	def leeGoles(self, n, tam):
		f = open(self.path1, "r")
		contador1 = 0
		contador2 = 0
		while contador1 < tam * n:
			f.readline()
			contador1 = contador1 + 1
		while contador2 < n:
			print f.readline()
			contador2 = contador2 + 1

	def leeEstadisticas(self, n, tam):
		f = open(self.path2, "r")
		contador1 = 0
		contador2 = 0
		while contador1 < tam * n:
			f.readline()
			contador1 = contador1 + 1
		while contador2 < n:
			print f.readline()
			contador2 = contador2 + 1
