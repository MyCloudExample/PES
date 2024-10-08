#Se graficaran la señal cuadrada usadno la libreria scipy.signal
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
#Defino los parametros de la onda cuadrada
frecuencia_señal=5
amplitud_señal=1
DC=0.5
#Defino el tramo del eje x, que representa la base de tiempo
x=np.linspace(0,1,500)
y=amplitud_señal*sig.square(2*np.pi*frecuencia_señal*x,DC)
plt.title("Wave Square")
plt.plot(x,y)
plt.ylim(-2,2)
plt.show()

