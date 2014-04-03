#Clase principal que ejecuta el roundrobin para el calendario de juegos

class RoundRobin(object):

    matrix =[[]]
   
    def __init__(self, arg):
        super(RoundRobin, self).__init__()
        self.n = arg
        self.roundrobin(self.n)
        self.tabla = [[]]

    def roundrobin(self,n):

        self.tabla = [range(n)]
        for i in range(1,n):
            fila = [i]
            while len(fila)<n: fila.append(0)
            self.tabla.append(fila)
        # busqueda recursiva
        self.encuentraRonda(1,2,n)

        self.matrix = self.tabla

    def encuentraRonda(self,fila,columna,dimension):
        posibles = range(dimension) 
        # remover posibles en la fila
        for i in range(columna): 
            posibles.remove(self.tabla[fila][i])
        # remover posibles en las filas contruidas
        for i in range(fila):
            if self.tabla[i][columna] in posibles: 
                posibles.remove(self.tabla[i][columna])

        for i in posibles:
            self.tabla[fila][columna]=i
            self.tabla[columna][fila]=i
            if (fila == dimension-2) and (columna == dimension-1):
                # Todo fue encontrado
                return 1
            if columna < dimension - 1:
                if self.encuentraRonda(fila,columna+1,dimension):
                    return 1
            elif fila < dimension - 2:
                if self.encuentraRonda(fila+1,fila+2,dimension):
                    return 1
            # deshacer el intento
            self.tabla[fila][columna]=0
            self.tabla[columna][fila]=0
        # Sin exito

        return 0

