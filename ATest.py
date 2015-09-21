__author__ = 'jparajeles'

from AEstrella.AEstrella import busqueda
from TowerP.Tower import Tower
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
[['n','n','n','e'],
['r','a','v','A'],
['a','v','A','r'],
['a','v','A','r'],
['a','v','A','r']])

result = busqueda(easy,final)
print(result)

