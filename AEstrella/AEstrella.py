import timeit

__author__ = 'JP'
E = "e"
N = "n"

from AEstrella.Nodo import *
from TowerP.Tower import printBeauty
from AEstrella.TriList import TriList, PentaList


def busqueda(ModeloI, ModeloF):
    return estrella(Nodo(ModeloI,None,0,0),Nodo(ModeloF,None, 0,0))


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
        acc += Cross(actual[key], meta[key])
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
    abiertos = TriList()
    cerrados = TriList()
    abiertos_f = PentaList()
    cerrados_f = PentaList()

    final_d = final.toDict()
    inicial.H = h(inicial.toDict(),final_d)

    abiertos.add(inicial)
    abiertos_f.add(inicial)
    while abiertos:
        #start = timeit.default_timer()

        min_f = abiertos.pop_min()
        abiertos_f.remove(min_f)

        #stop = timeit.default_timer()
        #print (stop - start)
        print(min_f.H, min_f.G)
        #printBeauty(min_f.Modelo.matrix)
        #print()

        cerrados.add(min_f)
        cerrados_f.add(min_f)

        for sucesor in sucesores(min_f, final_d):
            if(sucesor.igual(final)):
                print(len(abiertos))
                print(len(cerrados))
                return sucesor
            if(cerrados_f.find(sucesor)):
                continue
            abierto=abiertos_f.find(sucesor)
            if(abierto):
                if abierto.f() > sucesor.f():
                    abiertos.remove(abierto)
                    abiertos_f.remove(abierto)
                    abiertos.add(sucesor)
                    abiertos_f.add(sucesor)
                continue
            abiertos.add(sucesor)
            abiertos_f.add(sucesor)
#estrella end
