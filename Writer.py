__author__ = 'ia'

from TowerP.Tower import Tower, printBeauty
import time

class Writer:
    def __init__(self):
        self.variablesSistema = {'v':'verde', 'r': 'rojo', 'a':'amarillo','A': 'azul', 'e':'vacio', 'n': 'X'}

    """
        le entra el resultado de esto: result = busqueda(easy,final)
        escribe en un txt cada una de las matrices con este formato:

        M4
        Fila1 = {amarillo,amarillo,verde,rojo}
        Fila2 = {amarillo,verde,azul,azul}
        Fila3 = {amarillo,verde,azul,rojo}
        Fila4 = {rojo,verde,azul,rojo}
    """
    def writeSolution(self,initialMat, result):
        text = ''
        for elem in result:
            try:
                text += elem.description + "\n"
                text += (self.matrix2Txt(elem.Move.tower.matrix)) #deberia ser la funcion para escribir en archivos
            except:
                text += (self.matrix2Txt(initialMat.matrix)) # inicial #deberia ser la funcion para escribir en archivos
        #print(text) #\n
        current_time = time.strftime("%m%d%y_%H%M", time.localtime())
        output_name = 'solucion_%s.txt' % current_time
        #print (output_name)
        output_file = open(output_name, "w")
        output_file.write(text)

    #order debe ser: 'inicial' o 'final'
    def writeConfiguracion(self, order, matrix):

        text =''

        cont_row = 1
        for row in matrix:
            cont_col = 1
            for cell in row:
                if cell != 'n':
                    text += 'F%dC%d=%s\n'% (cont_row, cont_col, self.variablesSistema[cell])
                cont_col += 1
            cont_row +=1
        #print (text)

        current_time = time.strftime("%m%d%y_%H%M", time.localtime())
        output_name = 'config_%s_%s.txt' % (order,current_time)
        #print (output_name)
        output_file = open(output_name, "w")
        output_file.write(text)


    def matrix2Txt(self, matrix):
        text = ''
        cont = 0
        for row in matrix:
            cont2 = 0
            text += 'Fila' + str(cont) + ' = {'
            for cell in row:
                if cont2 == 3:
                    text += self.variablesSistema[cell]
                else:
                    text += self.variablesSistema[cell] + ','
                cont2+= 1
            text += '}\n'
            cont += 1
        text += '\n'
        return text