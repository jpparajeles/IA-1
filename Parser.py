__author__ = 'ia'
import re
import copy
from operator import itemgetter
import sys

"""
fila(#, {azul, azul, azul, color})

muesca(#col)

"""

class Parser:
    def __init__(self):

        self.tabla = []
        self.texto = ''
        self.posicionInicial = []
        self.posicionFinal = []
        self.posiciontemp = []
        self.posicionLista = self.inicializarLista()
        self.variablesSistema = {'verde':'v', 'rojo':'r', 'amarillo':'a', 'azul':'A'}


    def inicializarLista(self):
        lista = []
        for i in range (0,5):
            temp = []
            for j in range(0,4):
                temp.append('n')
            lista.append(temp)

        return lista

    def readFile(self, url):
        if url == "":
            return
        f = open(url)

        self.texto = f.read()
        f.close()
        return


    def getHayConfigInicial(self):
        return self.hayConfigInicial

    def getHayConfigFinal(self):
        return self.hayConfigFinal




    def revisarEstructura(self): #revisa si se ingreso las dos configuraciones (inicial y final) o solo una de ellas (e indica cuál)
        self.texto = re.sub(r"[\n]+","\n", self.texto) #quita line breaks extra
        self.texto = re.sub(r"[ ]+","", self.texto)  #quita los espacios extra
        print(self.texto)
        matchObj = re.match( r'^(\w+=\w+\n*|M[1-9]\n*|\n)*$', self.texto, re.U)
        self.separarTexto()
        if matchObj:
            return ""
        else:
            return "Error en la estructura general."


    def separarTexto(self):
        listaPosiciones = [ re.split(r'=', x, maxsplit=2) for x in re.split(r'\n', self.texto) ]
        if listaPosiciones.count(['']) > 0:
            listaPosiciones.remove([''])
        for elemento in listaPosiciones:
            temp = elemento[0]
            matchObj = re.match( r'F[1-5]C[1-4]|C[1-4]F[1-5]$', temp)

            if len(temp) > 2:
                elemento[0] = [ temp[:2], temp[2:]  ]
            else:
                elemento[0] = [temp]

            if len(elemento[0])>1: #para que no intente ordenar donde esta la muesca, porque en ese caso falla el sort
                elemento[0].sort(key=itemgetter(0))  #lo ordeno para que siempre quede primero las columnas, aunque en el txt hayan entrado al reves

            if not(matchObj): #si no hizo match, hay que revisar si porque corresponde a la muesca. Si con ese caso tampoco calza, definitivamente hay un error
                matchObj = re.match( r'M[1-4]$', temp)
                if matchObj:
                    elemento[0] = ['C'+temp[1],'F0']
                    elemento.append('Muesca')
                else:
                    return  ("Hay un error en la linea: '"+temp +"'")

        self.posiciontemp = copy.deepcopy(listaPosiciones)

        for elemento in self.posiciontemp:
            temp = elemento[0]
            elemento.pop(0)
            elemento.insert(0, temp[0][1])
            elemento.insert(0, temp[1][1])

        return ""

    def montarMatriz(self):
        for elemento in self.posiciontemp:
            if elemento[2].lower() in self.variablesSistema.keys() :  #aqui se  valida que los colores sean validos

                self.posicionLista [int(elemento[0])] [int(elemento[1])-1] = self.variablesSistema[elemento[2].lower()]
            elif elemento[2].lower() == 'muesca':
                self.posicionLista [int(elemento[0])] [int(elemento[1])-1] = 'e'
            else:
                #print("Uso de palabra no conocida " + elemento[2])
                return "Uso de la palabra no reconocida por el lenguaje: '" + elemento[2] + "'"
        return ""

    def validarMatriz(self):
        error = ''
        #revisar la primera fila
        #debe hacer solo una e, 3 n, y ningun otro color
        e_fila1 = self.posicionLista[0].count('e')
        n_fila1 = self.posicionLista[0].count('n')
        if e_fila1 != 1:
            error += 'Debe colocar la muesca en una única columna de la parte superior de la torre.\n'
        if n_fila1 != 3:
            error += 'Sólo 3 de las 4 columnas en la parte superior no deben tener elementos asignados.\n'

        #revisar el resto de la matriz
        #contar cuantos elementos hay de cada uno (incluyendo e y n)
        #para cada elemento, ver si la cantidad corresponde con el correcto (4 de 'A' 'a' 'v' y 'r', 0 de 'e' y 0 de 'n')
        cant_a = sum(row.count('a') for row in self.posicionLista[1:])
        cant_A = sum(row.count('A') for row in self.posicionLista[1:])
        cant_v = sum(row.count('v') for row in self.posicionLista[1:])
        cant_r = sum(row.count('r') for row in self.posicionLista[1:])
        e_matriz = sum(row.count('e') for row in self.posicionLista[1:])
        n_matriz = sum(row.count('n') for row in self.posicionLista[1:])

        if cant_a != 4:
            error += 'Cantidad incorrecta de bolitas de color amarillo.\n'
        if cant_A != 4:
            error += 'Cantidad incorrecta de bolitas de color azul.\n'
        if cant_v != 4:
             error += 'Cantidad incorrecta de bolitas de color verde.\n'
        if cant_r != 4:
            error += 'Cantidad incorrecta de bolitas de color rojo.\n'
        if e_matriz != 0:
            error += 'No se debe colocar la muesca abajo.\n'
        if n_matriz != 0:
            error += 'Hay espacios sin asignar color.\n'
        return error

    def getPosicionInicial(self):
        return self.posicionInicial

    def getPosicionFinal(self):
        return self.posicionFinal



    def parsear(self, configuracion, archivo):
        if (archivo == ''):
            return "Para parsear debe elegir un archivo de texto."

        self.readFile(archivo)
        error = self.revisarEstructura()

        if (error==''):
            error = self.separarTexto()
            if (error == ''):
                error = self.montarMatriz()
                if error == '':
                    error = self.validarMatriz()
                    if error == '':
                        if configuracion == 'inicial':
                            self.posicionInicial = copy.deepcopy(self.posicionLista)
                        elif configuracion == 'final':
                            self.posicionFinal = copy.deepcopy(self.posicionLista)
              #  else:
           #         return error
            #else:
             #   return error

        return error







