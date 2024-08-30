#Se genera y grafica la señal triangular utilizando funciones

import matplotlib.pyplot as plt

def señal_triangular (muestras):
    aux=[]
    for i in range (muestras):
        aux.append(i)
    for i in range (muestras,0,-1):
        aux.append(i)
    graficar(aux)
    print(aux)
    del aux
    return

def graficar (vector):
    plt.title("Triangular")
    plt.plot(vector)
    plt.show()

a=int(input("Muestras tomadas: "))

señal_triangular(a)
