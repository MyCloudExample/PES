#Se graficara la señal Dirac usando la libreria scipy
import scipy.signal as sig
import matplotlib.pyplot as plt
import numpy as np
#Defino los parametros de la onda Dirac
amplitud_dirac=1
dirac=amplitud_dirac*sig.unit_impulse(1000,'mid')
plt.title("Wave Dirac Impulse")
plt.plot(dirac)
plt.ylim(-2,2)
plt.show()