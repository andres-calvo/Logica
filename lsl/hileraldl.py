from hileralsl import hileraLSL


class hileraLDL(hileraLSL):
    primero = None
    ultimo = None

    def __init__(self):
        pass

    def subHilera(self, i, j):
        nuevaHilera = hileraLDL()
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
    