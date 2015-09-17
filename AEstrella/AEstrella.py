__author__ = 'JP'

from AEstrella.Nodo import findEq

def busqueda():
    pass

def f(actual, meta):
    """obtiene la h^ entre el actual y la distancia"""
    pass

def sucesores(inicial):
    pass


def estrella(inicial, final):
    abiertos = []
    cerrados = []

    abiertos.append(inicial)
    while abiertos:
        min_f = min(abiertos, key=lambda x: x.f())
        abiertos.remove(min_f)
        for sucesor in sucesores(min_f):
            # Añadir la creacion en sucesores
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











