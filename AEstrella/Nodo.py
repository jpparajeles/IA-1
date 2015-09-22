from AEstrella.tools import Point

__author__ = 'JP'

class Nodo:
    def __init__(self, pModelo, pPadre, pG, pH=-1):
        """Inicia el nodo
        """
        self.Modelo = pModelo
        self.Padre = pPadre
        self.G = pG
        self.H = pH
    def f(self):
        """Retorna F"""
        return self.G + self.H

    def igual(self, pModelo):
        return self.Modelo.matrix[1:] == pModelo.Modelo.matrix[1:]

    def toDict(self):
        ret = dict()
        for i, row in enumerate(self.Modelo.matrix):
            for j, elem in enumerate(row):
                if elem not in ret.keys():
                    ret[elem]=[Point(i,j)]
                else:
                    ret[elem].append(Point(i,j))
        return ret

"""
    def __lt__(self, other):
        if not isinstance(other, Nodo):
            raise TypeError
        return self.f()<other.f()

    def __le__(self, other):
        if not isinstance(other, Nodo):
            raise TypeError
        return self.f()<=other.f()

    def __eq__(self, other):
        if not isinstance(other, Nodo):
            raise TypeError
        return self.f() == other.f()

    def __ne__(self, other):
        if not isinstance(other, Nodo):
            raise TypeError
        return self.f()!=other.f()

    def __ge__(self, other):
        if not isinstance(other, Nodo):
            raise TypeError
        return self.f()>=other.f()

    def __gt__(self, other):
        if not isinstance(other, Nodo):
            raise TypeError
        return self.f()>=other.f()

"""


def findEq(nodo, list):
    """Encuenda si ya esta el modelo en una lista

    :type list: enumerate
    :type nodo: AEstrella.Nodo.Nodo
    """
    for elem in list:
        if elem.Modelo.matrix == nodo.Modelo.matrix:
            return elem
    return False

