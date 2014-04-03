#Clase que lee los resultados especificos

class Lector2(object):
	"""docstring for Lector2"""
	def __init__(self):
		self.path1 = "torneo.txt"
		self.path2 = "goles.txt"

	def leeGoles(self, n):
		f = open(self.path1, "r")
		contador1 = 0
		contador2 = 0
		while contador1 < n:
			f.readline()
