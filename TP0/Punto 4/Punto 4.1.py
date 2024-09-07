#Se buscara el maximo y su indice usando la libreria Numpy
import numpy as np

#genero el array de señal cuadrada usando numpy
s_cuad_numpy = np.append(np.zeros(5),np.ones(5))
#genero el array de señal triangular usando numpy
s_tria_numpy = np.append(range(5),range(5,0,-1))
#genero el array de señal Dirac usando numpy
delta_dirac_numpy_1 = np.append(np.zeros(100),np.ones(1))
delta_dirac_numpy =np.append(delta_dirac_numpy_1,np.zeros(99))

#maximo e indice de señal cuadrada
cuadrada_max=np.max(s_cuad_numpy)
cuadrada_indice=np.argmax(s_cuad_numpy)
print("Cuadrada Maximo:{}".format(cuadrada_max))
print("Cuadrada indice:{}".format(cuadrada_indice))
print(np.where(s_cuad_numpy == cuadrada_max))

#maximo e indice de señal triangular
triangular_max=np.max(s_tria_numpy)
triangular_indice=np.argmax(s_tria_numpy)
print("Triangular Maximo:{}".format(triangular_max))
print("Trianuglar indice:{}".format(triangular_indice))
print(np.where(s_tria_numpy == triangular_max))

#maximo e indice de señal Dirac
Dirac_max=np.max(delta_dirac_numpy)
Dirac_indice=np.argmax(delta_dirac_numpy)
print("Dirac Maximo:{}".format(Dirac_max))
print("Dirac indice:{}".format(Dirac_indice))
print(np.where(delta_dirac_numpy == Dirac_max))
