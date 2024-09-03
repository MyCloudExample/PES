#Se graficara la señal triangular usando la libreria scipy
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
#Defino los parametros de la onda cuadrada
frecuencia_señal=5
amplitud_señal=1
DC=0.5 #ajustando el DC se puede obtener triangualar o diente de sierra
fn=500 #es la frecuencia de muestreo
#Defino el tramo del eje x, que representa la base de tiempo
x=np.linspace(0,1,500)
y=amplitud_señal*sig.sawtooth(2*np.pi*frecuencia_señal*x,DC)
plt.title("Wave Sawtooth")
plt.plot(x,y)
plt.ylim(-2,2)
plt.show()
