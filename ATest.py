__author__ = 'jparajeles'

from AEstrella.AEstrella import busqueda, h
from AEstrella.Nodo import Nodo
from TowerP.Tower import Tower, printBeauty
import timeit
d=Tower(
[['n','n','n','e'],
['a','a','A','a'],
['a','r','v','A'],
['A','v','r','r'],
['r','v','A','v']])
final=Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

easy=Tower( #0.5s
[['n','n','n','r'],
['a','a','v','e'],
['r','v','A','A'],
['a','v','A','r'],
['a','v','A','r']])

test = Tower( #0.4s
[['n','n','n','e'],
['a','v','r','A'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

test2 = Tower( #0.7s
[['n','n','n','e'],
['a','v','A','r'],
['a','v','r','A'],
['a','v','A','r'],
['a','v','A','r']])

bio = Tower(
[['n','n','n','e'],
['a','v','r','A'],
['v','A','r','a'],
['a','v','A','r'],
['a','r','A','v']])

#"""

tt = test2
newNodo = Nodo(tt, None, 0)
finNodo = Nodo(final, None, 0)
newNodo.H=h(newNodo.toDict(), finNodo.toDict())
print(newNodo.H)
print("hola")
start = timeit.default_timer()
result = busqueda(tt,final)
#result = busqueda(final,tt)
print("Resultado")
print(result.f())
printBeauty(result.Modelo.matrix)
stop = timeit.default_timer()

print (stop - start)
#"""
