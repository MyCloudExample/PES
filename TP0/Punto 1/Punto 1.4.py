#Se realizara un menu que permita seleccionar que funcion se desea graficar, el menu se dee hacer si utilizar tantas funciones IF

import matplotlib.pyplot as plt


def graficar (vector):
    plt.title("Delta Dirac")
    plt.plot(vector)
    plt.show()

def switch_case (muestras):
    """ESTE ES UN MENU PARA SELECCIONAR QUE FUNCION GRAFICAR, LAS FUNCIONES CONTENIDAS DENTRO DE SWITCH_CASE
    PUEDEN MANIPULAR LAS VARAIBLES DENTRO DE SWITCH_CASE"""

    print("1. Señal Cuadrada")
    print("2. Señal Triangular")
    print("3. Señal Delta Dirac")

    opcion=int(input("Señal a graficar: "))
    #muestras=int(input("Cantidad de muestras: "))

    def señal_DeltaDirac ():
        aux=[]
        medio=int(muestras/2)
        for i in range (muestras):
            aux.append(0)
            if(i==medio):
                aux.append(1)
        graficar(aux)
        print(aux)
        del aux
        return

    def señal_cuadrada ():
        aux=[]
        for i in range (muestras):
            aux.append(0)
        for i in range (muestras):
            aux.append(1)
        graficar(aux)
        print(aux)
        del aux
        return

    def señal_triangular ():
        aux=[]
        for i in range (muestras):
            aux.append(i)
        for i in range (muestras,0,-1):
            aux.append(i)
        graficar(aux)
        print(aux)
        del aux
        return

    dic={3:señal_DeltaDirac, 1:señal_cuadrada, 2:señal_triangular}
    dic.get(opcion) ()

a=int(input("Ingrese cantidad de muestras: "))
switch_case(a)
help(switch_case)

