from pvf import diferencias_finitas, elementos_finitos
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math

def ed1(x):
    return 24*(x**2)

def soled1(x):
    return 2*(x**4)

def ed2(x):
    return -1*np.cos(x)

def soled2(x):
    return np.cos(x)

def main():
    a, b = 2, 5
    ya, yb = 34, 1255
    pi = 8 #paneles intermedios
    p = elementos_finitos(ed1, a, b, ya, yb, pi)
    xp = np.linspace(a, b, 500)
    yp = []
    ypa = []
    for t in xp:
       yp.append(p(t))
       ypa.append(soled1(t))
    plt.plot(xp,ypa,'g', label="Solucion Analitica")
    plt.plot(xp,yp,'r', label="Metodo elementos finitos")

    xp = np.linspace(a,b,pi)
    ypa2 = []
    for t in xp:
       ypa2.append(soled1(t))
    yp2 = diferencias_finitas(ed1, a, b, ya, yb, pi)
    plt.plot(xp,yp2,'b', label="Metodo diferencias finitas")
    plt.title("Problema Valores de Frontera")
    plt.xlabel('Tiempo')
    plt.ylabel('y(t)')
    plt.legend()
    plt.grid()
    plt.show()

    #Calculo del error relativo elementos finitos
    error = []
    for i in range(len(ypa)):
        error.append(abs((yp[i] - ypa[i])/ypa[i]))
    error_medio = statistics.mean(error)
    print("El error relativo promedio en E.F. para n = {0} es {1}".format(pi, error_medio))
    #Calculo del error relativo diferencias finitas
    error = []
    for i in range(len(ypa2)):
        error.append(abs((yp2[i] - ypa2[i])/ypa2[i]))
    error_medio = statistics.mean(error)
    print("El error relativo promedio en D.F. para n = {0} es {1}".format(pi, error_medio))

    return

main()
