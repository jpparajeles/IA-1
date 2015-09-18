__author__ = 'luisdiegopizarro'
from TowerP.Tower import *

d=Tower(
[['n','n','n','e'],
['a','a','A','a'],
['a','r','v','A'],
['A','v','r','r'],
['r','v','A','v']])


a=Tower([['n','n','n','e'],
['a','a','A','a'],
['a','r','v','A'],
['A','v','r','r'],
['r','v','A','v']])


print(d.isEqual(a))
#printAllMoves(d.nextMoves)
