__author__ = 'JP'
E = "e"
N = "n"

from AEstrella.Nodo import *
from TowerP.Tower import printBeauty

def busqueda(ModeloI, ModeloF):
    estrella(Nodo(ModeloI,None,0,0),Nodo(ModeloF,None, 0,0))


def Cross(init, end):
    acc = 0
    for i in init:
        work = []
        for j in end:
            work.append(i.diff(j))
        acc += min(work)
    return acc


def h(actual, meta):
    """obtiene la h^ entre el actual y la distancia
    :type meta: dict
    :type actual: dict
    """
    acc = 0
    for key in meta.keys():
        if key == N or key == E:
            continue
        acc += Cross(actual[key], actual[key])
    return acc


def sucesores(inicial, modelo_d):
    """ Encuentra los sucesores de un nodo dado y les asigna los valores


    :type modelo_d: dict
    :type inicial: AEstrella.Nodo.Nodo
    """
    ret = []
    for mov in inicial.Modelo.getNextMovements():
        newNodo = Nodo(mov.tower, inicial, mov.cost+inicial.G)
        newNodo.H=h(newNodo.toDict(), modelo_d)
        ret.append(newNodo)
    return ret



def estrella(inicial, final):
    abiertos = []
    cerrados = []
    final_d = final.toDict()
    abiertos.append(inicial)
    while abiertos:
        print(cerrados)
        min_f = min(abiertos, key=lambda x: x.f())
        abiertos.remove(min_f)
        for sucesor in sucesores(min_f, final_d):
            printBeauty(sucesor.Modelo.matrix)
            print()
            if(sucesor.igual(final)):
                return sucesor
            abierto=findEq(sucesor, abiertos)
            if(abierto and abierto.f() < sucesor.f()):
                continue
            cerrado=findEq(sucesor,cerrados)
            if(cerrado and cerrado.f() < sucesor.f()):
                continue
            abiertos.append(sucesor)
        cerrados.append(min_f)











