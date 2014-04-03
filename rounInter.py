#Clase principal que ejecuta el roundrobin para el calendario de juegos

class RoundRobin(object):

    """docstring for RoundRobin"""
    def __init__(self, arg):
        super(RoundRobin, self).__init__()
        self.n = arg
        

    def roundrobin(n):
        # setup tabla
        global tabla
        tabla = [range(n)]
        for i in range(1,n):
            fila = [i]
            while len(fila)<n: fila.append(0)
            tabla.append(fila)
        # perform recursive brute search
        encuentraRonda(1,2,n)
        # output in a dirty manner:
        for fila in tabla: print fila

    def encuentraRonda(fila,columna,dimension):
        global tabla
        posibles = range(dimension) # posibles for round to play the game
        # remove posibles already in the same fila
        for i in range(columna): posibles.remove(tabla[fila][i])
        # remove posibles in filas already constructed
        for i in range(fila):
            if tabla[i][columna] in posibles: posibles.remove(tabla[i][columna])

        for i in posibles:
            # try round nr. i
            tabla[fila][columna]=i
            tabla[columna][fila]=i
            if (fila == dimension-2) and (columna == dimension-1):
                # everything found
                return 1
            if columna < dimension - 1:
                if encuentraRonda(fila,columna+1,dimension):
                    return 1
            elif fila < dimension - 2:
                if encuentraRonda(fila+1,fila+2,dimension):
                    return 1
            # undo the try
            tabla[fila][columna]=0
            tabla[columna][fila]=0
        # no success
        return 0

# an now call for instance:

r = RoundRobin(10)
r.roundrobin(16)
r.roundrobin(8)
r.roundrobin(4)