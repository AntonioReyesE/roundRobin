#Clase principal que ejecuta el roundrobin para el calendario de juegos

class RoundRobin(object):

    matrix =[[]]
    """docstring for RoundRobin"""
    def __init__(self, arg):
        super(RoundRobin, self).__init__()
        self.n = arg
        self.roundrobin(self.n)
        self.tabla = [[]]

    def roundrobin(self,n):
        # setup self.tabla
        #self.tabla
        self.tabla = [range(n)]
        for i in range(1,n):
            fila = [i]
            while len(fila)<n: fila.append(0)
            self.tabla.append(fila)
        # perform recursive brute search
        self.encuentraRonda(1,2,n)
        # output in a dirty manner:
        #for fila in self.tabla: print fila
        #print self.tabla
        self.matrix = self.tabla

    def encuentraRonda(self,fila,columna,dimension):
        posibles = range(dimension) # posibles for round to play the game
        # remove posibles already in the same fila
        for i in range(columna): posibles.remove(self.tabla[fila][i])
        # remove posibles in filas already constructed
        for i in range(fila):
            if self.tabla[i][columna] in posibles: posibles.remove(self.tabla[i][columna])

        for i in posibles:
            # try round nr. i
            self.tabla[fila][columna]=i
            self.tabla[columna][fila]=i
            if (fila == dimension-2) and (columna == dimension-1):
                # everything found
                return 1
            if columna < dimension - 1:
                if self.encuentraRonda(fila,columna+1,dimension):
                    return 1
            elif fila < dimension - 2:
                if self.encuentraRonda(fila+1,fila+2,dimension):
                    return 1
            # undo the try
            self.tabla[fila][columna]=0
            self.tabla[columna][fila]=0
        # no success

        return 0

# an now call for instance:

#r = RoundRobin(10)

