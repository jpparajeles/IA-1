__author__ = 'jparajeles'

from AEstrella.AEstrella import busqueda
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

easy=Tower(
[['n','n','n','r'],
['a','a','v','e'],
['r','v','A','A'],
['a','v','A','r'],
['a','v','A','r']])

test = Tower(
[['n','n','n','e'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

start = timeit.default_timer()
result = busqueda(test,final)
print("Resultado")
print(result.f())
printBeauty(result.Modelo.matrix)
stop = timeit.default_timer()

print (stop - start)
