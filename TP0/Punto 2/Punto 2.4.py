#Se graficara la señal seno usando la libreria scipy
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
#Defino los parametros de la onda Dirac
amplitud=1
max_x=2
x=np.arange(0,max_x,0.1)
print(x)
y=amplitud*np.sin(np.pi*x)
plt.title("Wave Sin")
plt.plot(x,y)
plt.ylim(-2,2)
plt.show()