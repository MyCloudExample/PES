#Se genera y grafica la señal delta dirac utilizando funciones

import matplotlib.pyplot as plt

def señal_DeltaDirac (muestras):
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

def graficar (vector):
    plt.title("Delta Dirac")
    plt.plot(vector)
    plt.show()

a=int(input("Muestras tomadas: "))

señal_DeltaDirac(a)
