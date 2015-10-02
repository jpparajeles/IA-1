from tkinter import *
import time
import tkinter.filedialog
import os

ListaElementos = [["n","n","v","n"],["a","e","A","a"],["a","r","r","A"],["A","A","r","r"],["v","v","v","v"]]
ListaObj = []
ListaObj2 = []

ListaEstados1 = [[0,5,5,5],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]
ListaEstados2 = [[0,5,5,5],[1,2,3,4],[1,2,3,4],[1,2,3,4],[1,2,3,4]]

root = Tk()
root.title('Torre de Babilonia')
w = 1000 # El largo de la ventana
h = 600 # La altura de la ventana

# Obtener el largo y alto de la ventana
ws = root.winfo_screenwidth() # Largo de la ventana
hs = root.winfo_screenheight() # Altura de la ventana

# Se calculan las coordenadas x,y de la ventana root creada
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

window=Canvas(root)
window.pack(expand=True, fill=BOTH)

image1=PhotoImage(file="../Imagenes/fondo.png")
window.img=image1
window.create_image(0, 0, anchor=NW, image=image1)

#b1=Button(window, text="Hello", bd=0)
#window.create_window(20,20, window=b1, anchor=NW, width=150, height=150)

#Se asignan las imagenes de la torre de babilonia a una variable
TowerFontA = PhotoImage(file="../Imagenes/Font1.png")
TowerFontB = PhotoImage(file="../Imagenes/Font2.png")
TowerFontC = PhotoImage(file="../Imagenes/Font3.png")
TowerFontD = PhotoImage(file="../Imagenes/Font4.png")

#Se asignan los colores de las bolas a variables
imageBall_Green = PhotoImage(file="../Imagenes/small_ball_green.png")
imageBall_Red = PhotoImage(file="../Imagenes/small_ball_red.png")
imageBall_Blue = PhotoImage(file="../Imagenes/small_ball_blue.png")
imageBall_Yellow = PhotoImage(file="../Imagenes/small_ball_yellow.png")
imageBall_Empty = PhotoImage(file="../Imagenes/small_ball_black.png")
image_Tiny = PhotoImage(file="../Imagenes/image_tiny.png")

#Crea la torre
labelTower1 = Label(window,image = TowerFontA)
window.create_window(20,150, window=labelTower1, anchor=NW, width=279, height=300)
#Crea la torre2
labelTower2 = Label(window,image = TowerFontA)
window.create_window(320,150, window=labelTower2, anchor=NW, width=279, height=300)


#Declara los labels de cada elemento de la torre
ListaObj.append(Button(window,image = imageBall_Empty,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,0,0)))
ListaObj.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,0,0)))
ListaObj.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,0,0)))
ListaObj.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,0,0)))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,1,0)))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,1,1)))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,1,2)))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,1,3)))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,2,0)))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,2,1)))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,2,2)))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,2,3)))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,3,0)))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,3,1)))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,3,2)))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,3,3)))

ListaObj.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,4,0)))
ListaObj.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,4,1)))
ListaObj.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,4,2)))
ListaObj.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(1,ListaObj,ListaEstados1,4,3)))

#Crea los labels de la torre
window.create_window(36 ,165, window=ListaObj[0] , anchor=NW, width=50, height=50)
window.create_window(103,165, window=ListaObj[1] , anchor=NW, width=50, height=50)
window.create_window(168,165, window=ListaObj[2] , anchor=NW, width=50, height=50)
window.create_window(233,165, window=ListaObj[3] , anchor=NW, width=50, height=50)

window.create_window(36 ,221, window=ListaObj[4] , anchor=NW, width=50, height=50)
window.create_window(103,221, window=ListaObj[5] , anchor=NW, width=50, height=50)
window.create_window(168,221, window=ListaObj[6] , anchor=NW, width=50, height=50)
window.create_window(233,221, window=ListaObj[7] , anchor=NW, width=50, height=50)

window.create_window(36 ,275, window=ListaObj[8] , anchor=NW, width=50, height=50)
window.create_window(103,275, window=ListaObj[9] , anchor=NW, width=50, height=50)
window.create_window(168,275, window=ListaObj[10], anchor=NW, width=50, height=50)
window.create_window(233,275, window=ListaObj[11], anchor=NW, width=50, height=50)

window.create_window(36 ,330, window=ListaObj[12], anchor=NW, width=50, height=50)
window.create_window(103,330, window=ListaObj[13], anchor=NW, width=50, height=50)
window.create_window(168,330, window=ListaObj[14], anchor=NW, width=50, height=50)
window.create_window(233,330, window=ListaObj[15], anchor=NW, width=50, height=50)

window.create_window(36 ,385, window=ListaObj[16], anchor=NW, width=50, height=50)
window.create_window(103,385, window=ListaObj[17], anchor=NW, width=50, height=50)
window.create_window(168,385, window=ListaObj[18], anchor=NW, width=50, height=50)
window.create_window(233,385, window=ListaObj[19], anchor=NW, width=50, height=50)

window.create_window(36 ,165, window=ListaObj[0] , anchor=NW, width=50, height=50)
window.create_window(103,165, window=ListaObj[1] , anchor=NW, width=50, height=50)
window.create_window(168,165, window=ListaObj[2] , anchor=NW, width=50, height=50)
window.create_window(233,165, window=ListaObj[3] , anchor=NW, width=50, height=50)

def CambiaEstado(estado, ListaObjetos,Posiciones,x,y):
    global v
    global ListaEstados1
    global ListaEstados2
    if (v.get() == 2 and x!=0):
        if (Posiciones [x][y]==1):
            Posiciones [x][y]=2
            ListaObjetos[4*x+y].config(image = imageBall_Blue)
        elif (Posiciones [x][y]==2):
            Posiciones [x][y]=3
            ListaObjetos[4*x+y].config(image = imageBall_Green)
        elif (Posiciones [x][y]==3):
            Posiciones [x][y]=4
            ListaObjetos[4*x+y].config(image = imageBall_Yellow)
        elif (Posiciones [x][y]==4):
            Posiciones [x][y]=0
            ListaObjetos[4*x+y].config(image = imageBall_Empty)
        elif (Posiciones [x][y]==0):
            Posiciones [x][y]=1
            ListaObjetos[4*x+y].config(image = imageBall_Red)
        if (estado == 1):
            ListaEstados1 = Posiciones
        else:
            ListaEstados2 = Posiciones



#CARGA LA SEGUNDA TORRE DE BABILONIA
ListaObj2.append(Button(window,image = imageBall_Empty,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,0,0)))
ListaObj2.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,0,0)))
ListaObj2.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,0,0)))
ListaObj2.append(Button(window,image = image_Tiny     ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,0,0)))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,1,0)))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,1,1)))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,1,2)))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,1,3)))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,2,0)))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,2,1)))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,2,2)))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,2,3)))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,3,0)))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,3,1)))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,3,2)))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,3,3)))

ListaObj2.append(Button(window,image = imageBall_Red   ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,4,0)))
ListaObj2.append(Button(window,image = imageBall_Blue  ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,4,1)))
ListaObj2.append(Button(window,image = imageBall_Green ,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,4,2)))
ListaObj2.append(Button(window,image = imageBall_Yellow,borderwidth=0,highlightthickness=0, command=lambda: CambiaEstado(2,ListaObj2,ListaEstados2,4,3)))

#Crea los labels de la torre
window.create_window(336 ,165, window=ListaObj2[0] , anchor=NW, width=50, height=50)
window.create_window(403,165, window=ListaObj2[1] , anchor=NW, width=50, height=50)
window.create_window(468,165, window=ListaObj2[2] , anchor=NW, width=50, height=50)
window.create_window(533,165, window=ListaObj2[3] , anchor=NW, width=50, height=50)

window.create_window(336 ,221, window=ListaObj2[4] , anchor=NW, width=50, height=50)
window.create_window(403,221, window=ListaObj2[5] , anchor=NW, width=50, height=50)
window.create_window(468,221, window=ListaObj2[6] , anchor=NW, width=50, height=50)
window.create_window(533,221, window=ListaObj2[7] , anchor=NW, width=50, height=50)

window.create_window(336 ,275, window=ListaObj2[8] , anchor=NW, width=50, height=50)
window.create_window(403,275, window=ListaObj2[9] , anchor=NW, width=50, height=50)
window.create_window(468,275, window=ListaObj2[10], anchor=NW, width=50, height=50)
window.create_window(533,275, window=ListaObj2[11], anchor=NW, width=50, height=50)

window.create_window(336 ,330, window=ListaObj2[12], anchor=NW, width=50, height=50)
window.create_window(403,330, window=ListaObj2[13], anchor=NW, width=50, height=50)
window.create_window(468,330, window=ListaObj2[14], anchor=NW, width=50, height=50)
window.create_window(533,330, window=ListaObj2[15], anchor=NW, width=50, height=50)

window.create_window(336 ,385, window=ListaObj2[16], anchor=NW, width=50, height=50)
window.create_window(403,385, window=ListaObj2[17], anchor=NW, width=50, height=50)
window.create_window(468,385, window=ListaObj2[18], anchor=NW, width=50, height=50)
window.create_window(533,385, window=ListaObj2[19], anchor=NW, width=50, height=50)

window.create_window(336 ,165, window=ListaObj2[0] , anchor=NW, width=50, height=50)
window.create_window(403,165, window=ListaObj2[1] , anchor=NW, width=50, height=50)
window.create_window(468,165, window=ListaObj2[2] , anchor=NW, width=50, height=50)
window.create_window(533,165, window=ListaObj2[3] , anchor=NW, width=50, height=50)

def CargarFila1(labelTower,ListaE,ListaObjetos,i,j):
    if (ListaE[i][j]=="n"):
        if (j==0):
            ListaObjetos[0].config(image = image_Tiny)
        elif (j==1):
            ListaObjetos[1].config(image = image_Tiny)
        elif (j==2):
            ListaObjetos[2].config(image = image_Tiny)
        elif (j==3):
            ListaObjetos[3].config(image = image_Tiny)
    elif (ListaE[i][j]=="e"):
        if (j==0):
            labelTower.config(image = TowerFontA)
        elif (j==1):
            labelTower.config(image = TowerFontB)
        elif (j==2):
            labelTower.config(image = TowerFontC)
        elif (j==3):
            labelTower.config(image = TowerFontD)
    elif (ListaE[i][j]=="A"):
        if (j==0):
            labelTower.config(image = TowerFontA)
            ListaObjetos[0].config(image = imageBall_Blue)
        elif (j==1):
            labelTower.config(image = TowerFontB)
            ListaObjetos[1].config(image = imageBall_Blue)
        elif (j==2):
            labelTower.config(image = TowerFontC)
            ListaObjetos[2].config(image = imageBall_Blue)
        elif (j==3):
            labelTower.config(image = TowerFontD)
            ListaObjetos[3].config(image = imageBall_Blue)
    elif (ListaE[i][j]=="a"):
        if (j==0):
            labelTower.config(image = TowerFontA)
            ListaObjetos[0].config(image = imageBall_Yellow)
        elif (j==1):
            labelTower.config(image = TowerFontB)
            ListaObjetos[1].config(image = imageBall_Yellow)
        elif (j==2):
            labelTower.config(image = TowerFontC)
            ListaObjetos[2].config(image = imageBall_Yellow)
        elif (j==3):
            labelTower.config(image = TowerFontD)
            ListaObjetos[3].config(image = imageBall_Yellow)
    elif (ListaE[i][j]=="r"):
        if (j==0):
            labelTower.config(image = TowerFontA)
            ListaObjetos[0].config(image = imageBall_Red)
        elif (j==1):
            labelTower.config(image = TowerFontB)
            ListaObjetos[1].config(image = imageBall_Red)
        elif (j==2):
            labelTower.config(image = TowerFontC)
            ListaObjetos[2].config(image = imageBall_Red)
        elif (j==3):
            labelTower.config(image = TowerFontD)
            ListaObjetos[3].config(image = imageBall_Red)
    elif (ListaE[i][j]=="v"):
        if (j==0):
            labelTower.config(image = TowerFontA)
            ListaObjetos[0].config(image = imageBall_Green)
        elif (j==1):
            labelTower.config(image = TowerFontB)
            ListaObjetos[1].config(image = imageBall_Green)
        elif (j==2):
            labelTower.config(image = TowerFontC)
            ListaObjetos[2].config(image = imageBall_Green)
        elif (j==3):
            labelTower.config(image = TowerFontD)
            ListaObjetos[3].config(image = imageBall_Green)  

def CargarFilas(ListaE,ListaObjetos,i,j,Col1,Col2,Col3,Col4):
    if (ListaE[i][j]=="e"):
        if (j==0):
            ListaObjetos[Col1].config(image = imageBall_Empty)
        elif (j==1):
            ListaObjetos[Col2].config(image = imageBall_Empty)
        elif (j==2):
            ListaObjetos[Col3].config(image = imageBall_Empty)
        elif (j==3):
            ListaObjetos[Col4].config(image = imageBall_Empty)
    elif (ListaE[i][j]=="A"):
        if (j==0):
            ListaObjetos[Col1].config(image = imageBall_Blue)
        elif (j==1):
            ListaObjetos[Col2].config(image = imageBall_Blue)
        elif (j==2):
            ListaObjetos[Col3].config(image = imageBall_Blue)
        elif (j==3):
            ListaObjetos[Col4].config(image = imageBall_Blue)
    elif (ListaE[i][j]=="a"):
        if (j==0):
            ListaObjetos[Col1].config(image = imageBall_Yellow)
        elif (j==1):
            ListaObjetos[Col2].config(image = imageBall_Yellow)
        elif (j==2):
            ListaObjetos[Col3].config(image = imageBall_Yellow)
        elif (j==3):
            ListaObjetos[Col4].config(image = imageBall_Yellow)
    elif (ListaE[i][j]=="r"):
        if (j==0):
            ListaObjetos[Col1].config(image = imageBall_Red)
        elif (j==1):
            ListaObjetos[Col2].config(image = imageBall_Red)
        elif (j==2):
            ListaObjetos[Col3].config(image = imageBall_Red)
        elif (j==3):
            ListaObjetos[Col4].config(image = imageBall_Red)
    elif (ListaE[i][j]=="v"):
        if (j==0):
            ListaObjetos[Col1].config(image = imageBall_Green)
        elif (j==1):
            ListaObjetos[Col2].config(image = imageBall_Green)
        elif (j==2):
            ListaObjetos[Col3].config(image = imageBall_Green)
        elif (j==3):
            ListaObjetos[Col4].config(image = imageBall_Green)  

def CargarActual(labelTower1,ListaE,ListaObjetos):
    for i in range (len(ListaE)):
        for j in range(4):
            if   (i==0):
                CargarFila1(labelTower1,ListaE,ListaObjetos,i,j)
            elif (i==1):
                CargarFilas(ListaE,ListaObjetos,i,j,4,5,6,7)
            elif (i==2):
                CargarFilas(ListaE,ListaObjetos,i,j,8,9,10,11)
            elif (i==3):
                CargarFilas(ListaE,ListaObjetos,i,j,12,13,14,15)
            elif (i==4):
                CargarFilas(ListaE,ListaObjetos,i,j,16,17,18,19)
                
    
#ListaElementos = [["n","n","a","n"],["a","e","A","a"],["a","r","r","A"],["A","A","r","r"],["v","v","v","v"]]
def Cambia():
    L1=[["n","n","a","n"],["a","v","A","a"],["a","r","e","A"],["A","A","r","r"],["v","v","v","v"]]
    CargarActual(labelTower1,L1,ListaObj)
    CargarActual(labelTower2,L1,ListaObj2)
    root.after(500, CambiaN)

def CambiaN():
    L2=[["n","v","n","n"],["a","e","v","a"],["a","a","v","A"],["v","A","v","r"],["a","v","r","A"]]
    CargarActual(labelTower1,L2,ListaObj)
    CargarActual(labelTower2,L2,ListaObj2)
    root.after(500, Cambia)

#Funcion que valida botones del modo automatico
def ValidaAutomatico():
    L1=[["e","n","n","n"],["r","A","v","a"],["r","A","v","a"],["r","A","v","a"],["r","A","v","a"]]
    CargarActual(labelTower1,L1,ListaObj)
    CargarActual(labelTower2,L1,ListaObj2)

    buttonColorMuesca1.config(state="disabled")
    buttonMuesca1.config(state="disabled")
    buttonColorMuesca2.config(state="disabled")
    buttonMuesca2.config(state="disabled")
    buttonSolucionManual.config(state="disabled")
    buttonConfInicial.config(state="normal")
    buttonConfFinal.config(state="normal")
    buttonSolucionAutomatico.config(state="normal")

#Funcion que valida los botones del modo manual
def ValidaManual():
    L1=[["e","n","n","n"],["r","A","v","a"],["r","A","v","a"],["r","A","v","a"],["r","A","v","a"]]
    CargarActual(labelTower1,L1,ListaObj)
    CargarActual(labelTower2,L1,ListaObj2)
    buttonColorMuesca1.config(state="normal")
    buttonMuesca1.config(state="normal")
    buttonColorMuesca2.config(state="normal")
    buttonMuesca2.config(state="normal")
    buttonSolucionManual.config(state="normal")
    buttonConfInicial.config(state="disabled")
    buttonConfFinal.config(state="disabled")
    buttonSolucionAutomatico.config(state="disabled")

#MODO AUTOMATICO----------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------

#Funcion que solicita la ruta de los archivos
def SolicitaRuta(opcion):
    if (opcion == 1):
        dirNameInicial = tkinter.filedialog.askopenfilename(title = "Configuración inicial",initialdir='./' )
        print("Ruta de archivo de configuración inicial: " +dirNameInicial)
    else:
        dirNameFinal = tkinter.filedialog.askopenfilename(title = "Configuración final",initialdir='./' )
        print("Ruta de archivo de configuración final: " +dirNameFinal)

#Boton que carga la ruta del archivo inicial
buttonConfInicial = Button(root, text="Carga configuración inicial", command=lambda :SolicitaRuta(1),state="disabled")
window.create_window(200,10, window=buttonConfInicial , anchor=NW)

#Boton que carga la ruta del archivo final
buttonConfFinal = Button(root, text="Carga configuración final", command=lambda :SolicitaRuta(2),state="disabled")
window.create_window(400,10, window=buttonConfFinal , anchor=NW)

#Boton que llama a la función generar para realizar operacion para el modo automatico
buttonSolucionAutomatico = Button(root, text="Generar solución",state="disabled")
window.create_window(605,10, window=buttonSolucionAutomatico , anchor=NW)
#------------------------------------------------------------------------------------------------------------------------------
muesca1 = 0
muesca2 = 0
#MODO MANUAL----------------------------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------------------------------------------
def MuescaManual(torre,ListaObjetos,ListaEstado):
    global muesca1
    global muesca2
    if ( torre == 1 ):
        if (ListaEstado[0][0]!=5):
            labelTower1.config(image = TowerFontB)
            ListaObjetos[0].config(image = image_Tiny)
            ListaObjetos[1].config(image = imageBall_Empty)
            ListaEstados1[0][0]=5
            ListaEstados1[0][1]=0
            muesca1 = 1
        elif (ListaEstado[0][1]!=5):
            labelTower1.config(image = TowerFontC)
            ListaObjetos[1].config(image = image_Tiny)
            ListaObjetos[2].config(image = imageBall_Empty)
            ListaEstados1[0][1]=5
            ListaEstados1[0][2]=0
            muesca1 = 2
        elif (ListaEstado[0][2]!=5):
            labelTower1.config(image = TowerFontD)
            ListaObjetos[2].config(image = image_Tiny)
            ListaObjetos[3].config(image = imageBall_Empty)
            ListaEstados1[0][2]=5
            ListaEstados1[0][3]=0
            muesca1 = 3
        elif (ListaEstado[0][3]!=5):
            labelTower1.config(image = TowerFontA)
            ListaObjetos[3].config(image = image_Tiny)
            ListaObjetos[0].config(image = imageBall_Empty)
            ListaEstados1[0][3]=5
            ListaEstados1[0][0]=0
            muesca1 = 0
    else:
        if (ListaEstado[0][0]!=5):
            labelTower2.config(image = TowerFontB)
            ListaObjetos[0].config(image = image_Tiny)
            ListaObjetos[1].config(image = imageBall_Empty)
            ListaEstados2[0][0]=5
            ListaEstados2[0][1]=0
            muesca2 = 1
        elif (ListaEstado[0][1]!=5):
            labelTower2.config(image = TowerFontC)
            ListaObjetos[1].config(image = image_Tiny)
            ListaObjetos[2].config(image = imageBall_Empty)
            ListaEstados2[0][1]=5
            ListaEstados2[0][2]=0
            muesca2 = 2
        elif (ListaEstado[0][2]!=5):
            labelTower2.config(image = TowerFontD)
            ListaObjetos[2].config(image = image_Tiny)
            ListaObjetos[3].config(image = imageBall_Empty)
            ListaEstados2[0][2]=5
            ListaEstados2[0][3]=0
            muesca2 = 3
        elif (ListaEstado[0][3]!=5):
            labelTower2.config(image = TowerFontA)
            ListaObjetos[3].config(image = image_Tiny)
            ListaObjetos[0].config(image = imageBall_Empty)
            ListaEstados2[0][3]=5
            ListaEstados2[0][0]=0
            muesca2 = 0


def MuescaColorManual(torre,ListaObjetos,ListaEstado):
    global muesca1
    global muesca2
    if (torre == 1):
        if (ListaEstado[0][muesca1]==0):
            ListaObjetos[muesca1].config(image = imageBall_Red)
            ListaEstado[0][muesca1]=1
        elif (ListaEstado[0][muesca1]==1):
            ListaObjetos[muesca1].config(image = imageBall_Blue)
            ListaEstado[0][muesca1]=2
        elif (ListaEstado[0][muesca1]==2):
            ListaObjetos[muesca1].config(image = imageBall_Green)
            ListaEstado[0][muesca1]=3
        elif (ListaEstado[0][muesca1]==3):
            ListaObjetos[muesca1].config(image = imageBall_Yellow)
            ListaEstado[0][muesca1]=4
        elif (ListaEstado[0][muesca1]==4):
            ListaObjetos[muesca1].config(image = imageBall_Empty)
            ListaEstado[0][muesca1]=0
        ListaEstados1 = ListaEstado

    else:
        if (ListaEstado[0][muesca2]==0):
            ListaObjetos[muesca2].config(image = imageBall_Red)
            ListaEstado[0][muesca2]=1
        elif (ListaEstado[0][muesca2]==1):
            ListaObjetos[muesca2].config(image = imageBall_Blue)
            ListaEstado[0][muesca2]=2
        elif (ListaEstado[0][muesca2]==2):
            ListaObjetos[muesca2].config(image = imageBall_Green)
            ListaEstado[0][muesca2]=3
        elif (ListaEstado[0][muesca2]==3):
            ListaObjetos[muesca2].config(image = imageBall_Yellow)
            ListaEstado[0][muesca2]=4
        elif (ListaEstado[0][muesca2]==4):
            ListaObjetos[muesca2].config(image = imageBall_Empty)
            ListaEstado[0][muesca2]=0
        ListaEstados2 = ListaEstado

#Boton que carga la ruta del archivo inicial
buttonMuesca1 = Button(root, text="Muesca 1", command=lambda:MuescaManual(1,ListaObj,ListaEstados1),state="disabled")
window.create_window(25,110, window=buttonMuesca1 , anchor=NW)

#Boton que carga la ruta del archivo final
buttonColorMuesca1 = Button(root, text="Cambiar bola muesca 1", command=lambda:MuescaColorManual(1,ListaObj,ListaEstados1),state="disabled")
window.create_window(127,110, window=buttonColorMuesca1 , anchor=NW)

#Boton que carga la ruta del archivo inicial
buttonMuesca2 = Button(root, text="Muesca 2", command=lambda:MuescaManual(2,ListaObj2,ListaEstados2),state="disabled")
window.create_window(325,110, window=buttonMuesca2 , anchor=NW)

#Boton que carga la ruta del archivo final
buttonColorMuesca2 = Button(root, text="Cambiar bola muesca 2", command=lambda:MuescaColorManual(2,ListaObj2,ListaEstados2),state="disabled")
window.create_window(427,110, window=buttonColorMuesca2 , anchor=NW)

#Boton que llama a la función generar para realizar operacion para el modo automatico
buttonSolucionManual = Button(root, text="Generar solución",state="disabled")
window.create_window(605,110, window=buttonSolucionManual , anchor=NW)
#------------------------------------------------------------------------------------------------------------------------------

#Se crean los radioButton
global v
v = IntVar()
Rb1 = Radiobutton(window,text="Modo automático", variable = v, value = 1, padx=10,command= ValidaAutomatico)
Rb2 = Radiobutton(window,text="Modo manual", variable = v, value = 2, padx=10,command= ValidaManual)
window.create_window(10,10, window=Rb1 , anchor=NW)
window.create_window(10,60, window=Rb2 , anchor=NW)
#------------------------------------------------------------------------------------------------------------------------------


button = Button(root, text="Cambiar a negro!", command=Cambia)
button.pack()

button1 = Button(root, text="Cambiar a rojo!", command=CambiaN)
button1.pack()

#------------------------------------------------------------------------------------------------------------------------------
# Se agregan las dimensiones a la ventana y su localizacion en pantalla
root.geometry('%dx%d+%d+%d' % (w, h, x, y))
root.mainloop() # Crea la ventana