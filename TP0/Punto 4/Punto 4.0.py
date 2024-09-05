#La variable amplitud es para tener diferentes valores en los puntos maximos
amplitud=3
# Señal cuadrada (escalón)
senial_cuad = [] #inicializo un array vacío
for a in range(10):
    senial_cuad.append(0)
for a in range(10):
    senial_cuad.append(amplitud)
# Señal delta de dirac
delta_dirac = []
for a in range(100):
    delta_dirac.append(0)
dd= int(len(delta_dirac)/2) #obtener la posición del medio del array
delta_dirac[dd] = amplitud
# Señal triangular
senial_tria = []
for a in range(5):
    senial_tria.append(a*amplitud)
for a in range(5,0,-1):
    senial_tria.append(a*amplitud)

max_cuad=max(senial_cuad)
indice=senial_cuad.index(max_cuad)
print("Maximo de Cuadrada {}".format(max_cuad))
print("Indice Maximo Cuadrada {}".format(indice))

max_tria=max(senial_tria)
indice=senial_tria.index(max_tria)
print("Maximo de Triangular {}".format(max_tria))
print("Indice Maximo Triangular {}".format(indice))

max_DD=max(delta_dirac)
indice=delta_dirac.index(max_DD)
print("Maximo de Dira {}".format(max_DD))
print("Indice Maximo Dirac {}".format(indice))
