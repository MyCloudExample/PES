#1. Generar señal cuadrada, triangular, delta dirac en python si nel uso de librerias
#Parte resuleta por el docente
import matplotlib.pyplot as plt

# Señal cuadrada (escalón)
senial_cuad = [] #inicializo un array vacío
for a in range(5):
    senial_cuad.append(0)
for a in range(5):
    senial_cuad.append(1)
print(senial_cuad)
plt.title("Escalón")
plt.plot(senial_cuad)
plt.show()

# Señal delta de dirac
delta_dirac = []
for a in range(100):
    delta_dirac.append(0)
dd= int(len(delta_dirac)/2) #obtener la posición del medio del array
delta_dirac[dd] = 1
print("el largo del vector delta_dirac es: {}".format(len(delta_dirac)))
plt.title("Dirac")
plt.plot(delta_dirac)
plt.show()


# Señal triangular
senial_tria = []
for a in range(5):
    senial_tria.append(a)
for a in range(5,0,-1):
    senial_tria.append(a)
plt.title("Triangular")
plt.plot(senial_tria)
plt.show()