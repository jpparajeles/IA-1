__author__ = 'luisdiegopizarro'
from copy import deepcopy
from TowerP.Space import *
from TowerP.Movement import *
'''
A amarillo
a azul
r rojo
v verde
e espacio
n barrera

n n n e
a a A a
a r v A
A v r r
r v A v'''
class Tower:
    def __init__(self,pMatrix):
        self.matrix=pMatrix;
        self.emptySpace=self.setEmptySpace()
        self.rowLen=len(pMatrix)
        self.nextMoves=[]
        ###################
        self.setNextMovements()

    def getColumn(self,numCol):
        col=[]
        for x in self.matrix:
            col.append(x[numCol])
        return col

    def getRotations(self):
        #el movimiento de la mueca vale menos
        self.nextMoves.append(Movement(1,rotateRight(deepcopy(self.matrix),0)))
        self.nextMoves.append(Movement(1,rotateLeft(deepcopy(self.matrix),0)))
        for rowNum in range(1,self.rowLen):
            self.nextMoves.append(Movement(4,rotateRight(deepcopy(self.matrix),rowNum)))
            self.nextMoves.append(Movement(4,rotateLeft(deepcopy(self.matrix),rowNum)))

    def setEmptySpace(self):
        #el empty aca lo tengo como 'e' si en el txt cambia tuesta, hay q ver si me lo mandan x parametro
        for rowNum,row in enumerate(self.matrix):
            if('e' in row):
               return Space(rowNum,row.index('e'))#[fila,columna]

    def getBallMovement(self):
        col=self.emptySpace.column
        row=self.emptySpace.row
        rowsCopy=deepcopy(self.matrix)#copia necesaria para no alterar el objeto original
        if(row==0):#mueve bola hacia abajo
            rowsCopy[row][col],rowsCopy[row+1][col]=rowsCopy[row+1][col],rowsCopy[row][col]
            self.nextMoves.append(Movement(1,rowsCopy))
        elif(row==self.rowLen-1):#mueve bola hacia arriba
            rowsCopy[row][col],rowsCopy[row-1][col]=rowsCopy[row-1][col],rowsCopy[row][col]
            self.nextMoves.append(Movement(1,rowsCopy))
        else:#mueve la bola hacia arriba y hacia abajo
            rowsCopy[row][col],rowsCopy[row+1][col]=rowsCopy[row+1][col],rowsCopy[row][col]
            rowsCopy2=deepcopy(self.matrix)#se necesita una segunda copia para no alterar la primera
            rowsCopy2[row][col],rowsCopy2[row-1][col]=rowsCopy2[row-1][col],rowsCopy2[row][col]
            self.nextMoves.append(Movement(1,rowsCopy))
            self.nextMoves.append(Movement(1,rowsCopy2))

    def setNextMovements(self):
        self.getRotations()
        self.getBallMovement()

    def isEqual(self,towerCompare):
        return self.matrix==towerCompare.matrix

def rotateRight(tower,pos):
    tower[pos]=tower[pos][-1:]+tower[pos][:-1]
    return tower

def rotateLeft(towel,pos):
    towel[pos]=towel[pos][1:]+towel[pos][:1]
    return towel


###test prints
def printBeauty(rows):
        for x in rows:
            for y in x:
                print(y,end=" ")
            print(" ")

def printAllMoves(moves):
    for x,y in enumerate(moves):
        print("mov# "+str(x+1)+" Costo"+str(y.cost))
        printBeauty(y.mov)




