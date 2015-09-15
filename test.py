__author__ = 'ia'

from AEstrella.Nodo import Nodo



a = [Nodo(1,1,1,2), Nodo(1,3,1,1), Nodo(1,1,1,2)]
print(a)
o = min(a, key=lambda x: x.f())
print(o)
a.remove(o)
print(a)
