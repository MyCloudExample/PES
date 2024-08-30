#Se genera y grafica la señal cuadrada tuilizando funciones

import matplotlib.pyplot as plt

def señal_cuadrada (muestras):
    aux=[]
    for i in range (muestras):
        aux.append(0)
    for i in range (muestras):
        aux.append(1)
    graficar(aux)
    print(aux)
    del aux
    return

def graficar (vector):
    plt.title("Escalón")
    plt.plot(vector)
    plt.show()

a=int(input("Muestras tomadas: "))

señal_cuadrada(a)

    