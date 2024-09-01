import numpy as np
import matplotlib.pyplot as plt

# Señal Cuadrada con numpy
senial_cuad_numpy = np.append(np.zeros(5),np.ones(5))
# una variante con mas de 2 vectores seria:
# senial_cuad_numpy = np.append(np.append(np.zeros(2),np.ones(5)),np.zeros(2))
print(senial_cuad_numpy)

# Señal delta de dirac con numpy
delta_dirac_numpy_1 = np.append(np.zeros(100),np.ones(1))
delta_dirac_numpy =np.append(delta_dirac_numpy_1,np.zeros(100))
print(delta_dirac_numpy)

# Señal triangular con numpy
senial_tria_numpy = np.append(range(5),range(5,0,-1))
print(senial_tria_numpy)

plt.title("Cuadrada")
plt.plot(senial_cuad_numpy)
plt.show()

plt.title("Triangular")
plt.plot(senial_tria_numpy)
plt.show()

plt.title("Delta Dirac")
plt.plot(delta_dirac_numpy)
plt.show()