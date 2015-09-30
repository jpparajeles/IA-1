import timeit

MAX_D = 96

__author__ = 'JP'
E = "e"
N = "n"

from AEstrella.Nodo import *
from TowerP.Tower import printBeauty
from AEstrella.TriList import TriList, PentaList
from itertools import permutations

def busqueda(ModeloI, ModeloF):
    return estrella(Nodo(ModeloI,None,0,0),Nodo(ModeloF,None, 0,0))


def Cross(init, end):
    """
    acc = 0
    for i in init:
        work = []
        for j in end:
            work.append(i.diff(j))
        acc += min(work)
    return acc
    """
    wk = []
    for i in init:
        inn = []
        for j in end:
            inn.append(i.diff(j))
        wk.append(inn)
    perm = permutations(range(0,len(wk)))
    ret = []
    for p in perm:
        acc = 0
        for i, k in enumerate(wk):
            acc += k[p[i]]
        ret.append(acc)
    return min(ret)

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


def floork(inicial, target, succ):
    """


    :type succ: list
    :type inicial: AEstrella.Nodo.Nodo
    :type target: AEstrella.Nodo.Nodo
    """
    inv = floorkiller(inicial, target)
    for i in inv:
        if target.Modelo.matrix[i]!=succ[i*2].Modelo.matrix[i]:
            succ[i*2].H+= MAX_D
        if target.Modelo.matrix[i]!=succ[i*2+1].Modelo.matrix[i]:
            succ[i*2+1].H+= MAX_D



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
    #cerrados = TriList()
    abiertos_f = PentaList()
    cerrados_f = PentaList()

    final_d = final.toDict()
    inicial.H = h(inicial.toDict(),final_d)

    abiertos.add(inicial)
    abiertos_f.add(inicial)
    contar = 0
    while abiertos:
        #start = timeit.default_timer()

        min_f = abiertos.pop_min()
        abiertos_f.remove(min_f)

        #stop = timeit.default_timer()
        #print (stop - start)
        if contar%10000 == 5:
            print(min_f.H, min_f.G)
            print(contar)
            print(len(abiertos))
            #print(len(cerrados))
        contar+=1
        #printBeauty(min_f.Modelo.matrix)
        #print()

        #cerrados.add(min_f)
        cerrados_f.add(min_f)

        succ = sucesores(min_f, final_d)
        floork(min_f,final,succ)
        for sucesor in succ:
            if(sucesor.igual(final)):
                print(len(abiertos))
                #print(len(cerrados))
                print(contar)
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
