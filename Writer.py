__author__ = 'ia'

from TowerP.Tower import Tower, printBeauty

class Writer:
    def __init__(self):
        self.variablesSistema = {'v':'verde', 'r': 'rojo', 'a':'amarillo','A': 'azul', 'e':'Muesca', 'n': 'X'}

    #le entra el resultado de esto: result = busqueda(easy,final)
    def writeSolution(self,initialMat, result):
        text = ''
        for elem in result:
            try:
                text += (self.matrix2Txt(elem.Move.tower.matrix)) #deberia ser la funcion para escribir en archivos
            except:
                text += (self.matrix2Txt(initialMat.matrix)) # inicial #deberia ser la funcion para escribir en archivos
            print(text) #\n

    def matrix2Txt(self, matrix):
        text = ''
        cont = 0
        for row in matrix:  #text = ''
            cont2 = 0
            if cont != 0:
                text += 'Fila' + str(cont) + ' = {'
            for cell in row:
                if (cont ==0 ) and (cell == 'e'):
                    text += 'M'+str(cont2+1)+'\n'
                elif cell != 'n':
                    if cont2 == 3:
                        text += self.variablesSistema[cell]
                    else:
                        text += self.variablesSistema[cell] + ','
                cont2+= 1
            if cont != 0:
                text += '}\n'
            cont += 1
        text += '\n'
        return text