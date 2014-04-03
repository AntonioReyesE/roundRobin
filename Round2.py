# -*- encoding: utf-8 -*-
class Round:

	tabla = [[]]
	equipos = 0
	def __init__(self, equipos):
		self.equipos = equipos
		self.tabla = [[-1 for x in xrange(self.equipos-1)] for x in xrange(self.equipos)]
		#print self.tabla 


	def imprime(self):
		for i in range(0,self.equipos):
			for j in range(0,self.equipos-1):
				print self.tabla[i][j],
			print ""


	def formarTabla(self, inf, sup):
		medio = 0

		if(inf == sup - 1):
			self.tabla[inf][0] = sup
			self.tabla[sup][0] = inf
		else:
			medio = (inf + sup)/2 
			
			self.formarTabla(inf,medio)
			self.formarTabla(medio+1,sup)

			#self.completarTabla(inf,medio,medio,sup,medio+1)
			print "antes "
			self.imprime()
			print " "
			self.completarTabla(medio+1,sup,medio,sup,inf)
			
 			print "despues "
			self.imprime()
			print " "
 			
 			#self.imprime()
 	def completarTabla(self, eqinf,eqsup, diainf, diasup, eqini):
 		print "eqinf " + str(eqinf) + " eqsup " + str(eqsup) + " diainf " + str(diainf) + " diasup " + str(diasup) + " eqini " + str(eqini) 
 		for i in range(diainf, diasup ):
 			print "         for anonimo x " + str(eqinf) + " y " + str(i)
 			self.tabla[eqinf][i] = eqini + i - diainf
 		
 		for x in range (eqinf+1,eqsup+1):
 			print "        x " + str(x) + " y " + str(diainf)
 			print "        i-1 " + str(x) + " diasup " + str(diasup-1)
 			self.tabla[x][diainf] = self.tabla[x-1][diasup-1]
 			for j in range(diainf + 1,diasup):
 				print "           segundo for x " + str(x) + " j " + str(j)
 				self.tabla[x][j] = self.tabla[x-1][j-1]
RoundRobin = Round(8)
RoundRobin.imprime()
print ""
RoundRobin.formarTabla(0,7)
#RoundRobin.completarTabla(4,7,1,2,4)
RoundRobin.imprime()