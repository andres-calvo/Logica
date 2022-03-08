from lsl import listaEnlazada
# replace,borrar


class hileraLSL(listaEnlazada):
    def __init__(self):
        pass

    def subHilera(self, i, j):
        nuevaHilera = hileraLSL()
        n = self.length()
        if (i < 0 or i > n):
            print("parámetro i errado")
            return None
        if (j < 0 or j > n - i + 1):
            print("parámetro j errado")
            return None
        for k in range(i, i + j):
            nodoAinsertar = self.get(k)
            nuevaHilera.append(nodoAinsertar.data)

        return nuevaHilera

    def posicion(self, letra):
        contador = 0
        for i in range(self.length()):
            if self.get(i).data != letra:
                contador += 1
            else:
                return contador

    def concat(self, hileraT):
        copia = self
        tlon = hileraT.length()
        for i in range(tlon):
            copia.append(hileraT.get(i).data)
        return copia

    def insertar(self, hileraT, i):
        p1 = self.subHilera(0, i)
        p2 = self.subHilera(i+1, self.length())
        final = p1.concat(hileraT).concat(p2)
        self = final

    def borrar(self, posicion, cantidadEliminar):
        print("hola")
        for i in range(posicion, cantidadEliminar+posicion):
            self.erase(i)

    def replace(self, i, j, t):
        if i < 0 or j < 0:
            print("Parametros i o j invalidos")
            return

        if i == 0:
            partefinal = self.subHilera(j, self.length() - j)
            return self.concat(t, partefinal)

        parte1 = self.subHilera(0, i)
        parte2 = self.subHilera(i+j, self.lenght() - i - j)
        final = parte1.concat(t).concat(parte2)
        return final


l = hileraLSL()
l.append("y")
l.append("x")
l.append("b")
l.append("a")
# l.display()
l2 = l.subHilera(1, 2)
l2.display()
# #print(l.posicion("y"))
