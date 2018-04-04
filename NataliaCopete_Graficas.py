import numpy as np
import matplotlib.pyplot as plt


py=np.loadtxt("times_ptyhon.csv")
cmas=np.loadtxt("times_cpp")


##N es el n-esimo numero de fibonacci generado con python
##N es el n-esimo numero de fibonacci generado con c++
##py son los datos generados con el programa de python
##cmas son los datos generados con el programa de c++
##tiempop: tiempo  generado con el programa de python
##tiempoc:tiempo generado con el programa de de c++

N=py[:,0]
tiempop=py[:,1]
N1=cmas[:,0]
tiempoc=cmas[:,1]


plt.plot(N,tiempop, label="python")
plt.plot(N1,tiempoc,label="c++")
plt.savefig("cpp_vs_python.png")
plt.legend()
