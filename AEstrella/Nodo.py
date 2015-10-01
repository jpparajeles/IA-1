from collections import deque
from AEstrella.tools import Point
from TowerP.Movement import Movement

__author__ = 'JP'

class Nodo:
    def __init__(self, pModelo, pPadre, pG, move, pH=-1):
        """Inicia el nodo
        """
        self.Modelo = pModelo
        self.Padre = pPadre
        self.G = pG
        self.H = pH
        self.Move = move
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

def floorkiller(nodo,destino):
    """Encuenda si ya esta el modelo en una lista

    :type destino: AEstrella.Nodo.Nodo
    :type nodo: AEstrella.Nodo.Nodo
    """
    ret = []
    for i in range(4,-1,-1):
        if nodo.Modelo.matrix[i] != destino.Modelo.matrix[i]:
            return ret
        ret.append(i)
    return ret



def findEq(nodo, list):
    """Encuenda si ya esta el modelo en una lista

    :type list: enumerate
    :type nodo: AEstrella.Nodo.Nodo
    """
    for elem in list:
        if elem.Modelo.matrix == nodo.Modelo.matrix:
            return elem
    return False

def toList(nodo):
    """Devuelve los Mov en una lista

    :type nodo: AEstrella.Nodo.Nodo
    """
    current = nodo
    ret = []
    while current:
        ret.append(current.Move)
        current = current.Padre
    ret.reverse()
    return ret

def makeRotations(nodo):
    """

    :type nodo: AEstrella.Nodo.Nodo
    """
    ret = dict()
    for i, row in enumerate(nodo.Modelo.matrix):
        ret[i]=rotar(row)
    return ret


def rotar(fila):
    """

    :type fila: list
    """
    rotator = deque(fila)
    ret = set()
    for i in range(0,len(fila)):
        rotator.rotate(1)
        ret.add("".join(list(rotator)))
    return ret
