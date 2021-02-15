from PVI import euler,taylor,rungekutta2,rungekutta4,multipaso2,multipasoAB
from math import cos,sin
import matplotlib.pyplot as plt
import numpy as np
from time import time
import math
import statistics

def f_analitica(t):
    f = 2*(t**4)
    #f = np.cos(t)
    return f

def f(t,y):
    f = 8*(t**3)
    #f = -1 * np.sin(t)
    return f

def ft(t,y):
    ft = 24*(t**2)
    #ft = -1* np.cos(t)
    return ft

def fy(t,y):
    fy = 0
    return fy

def main():
    #h,t,t0, y y0 aplicados para las funciones
    h = 0.5
    t = 6
    t0 = 1
    y0 = 2
    #ODE analitica
    t_vector = np.arange(t0,t+h,h)
    y_array = []
    for i in range(len(t_vector)):
        y_array.append(f_analitica(t_vector[i]))
    #Metodos PVI
    #euler
    e_vector = euler(f,t0,t,y0,h)
    #taylor
    ta_vector = taylor(f,ft,fy,t0,t,y0,h)
    #rungekutta2
    r2_vector = rungekutta2(f,t0,t,y0,h)
    #rungekutta4
    r4_vector = rungekutta4(f,t0,t,y0,h)
    #multipasos
    #Se inician los 3 primeros valores con rungekutta4
    n2_vec = r4_vector[:1]
    nAB_vec = r4_vector[:3]
    m2_vector = multipaso2(f,t,n2_vec[-1],h,n2_vec,t_vector[1])
    mAB_vector = multipasoAB(f,t,nAB_vec[-1],h,nAB_vec,t_vector[3])
    #Graficacion
    plt.plot(t_vector, y_array, label = "Solución analitica")
    plt.plot(t_vector, e_vector, label = "Euler")
    plt.plot(t_vector,ta_vector, label = "Taylor")
    plt.plot(t_vector,r2_vector, label = "Rungekutta2")
    plt.plot(t_vector,r4_vector, label = "Rungekutta4")
    plt.plot(t_vector,m2_vector, label = "multipaso2")
    plt.plot(t_vector,mAB_vector, label = "multipasoAB")
    plt.ylabel("Valores ODE")
    plt.xlabel("Valores puntos de t")
    plt.legend()
    plt.grid()
    plt.show()
    #Calculo error
    print("calculo error")
    error = []
    for i in range(len(y_array)):
        error.append(abs((e_vector[i] - y_array[i])/y_array[i]))
    error_medio = statistics.mean(error)
    print("euler",error_medio)

    error = []
    for i in range(len(y_array)):
        error.append(abs((ta_vector[i] - y_array[i])/y_array[i]))
    error_medio = statistics.mean(error)
    print("taylor",error_medio)
    error = []
    for i in range(len(y_array)):
        error.append(abs((r2_vector[i] - y_array[i])/y_array[i]))
    error_medio = statistics.mean(error)
    print("rungekutta2",error_medio)
    error = []
    for i in range(len(y_array)):
        error.append(abs((r4_vector[i] - y_array[i])/y_array[i]))
    error_medio = statistics.mean(error)
    print("rungekutta4",error_medio)
    error = []
    for i in range(len(y_array)):
        error.append(abs((m2_vector[i] - y_array[i])/y_array[i]))
    error_medio = statistics.mean(error)
    print("multipaso2",error_medio)
    error = []
    for i in range(len(y_array)):
        error.append(abs((mAB_vector[i] - y_array[i])/y_array[i]))
    error_medio = statistics.mean(error)
    print("multipasoAB",error_medio)


main()
