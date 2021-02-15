from diferenciacion import dif_fin_atras, dif_fin_adelante, dif_fin_centrado
from integracion import rectangulo, trapezoide, simpson
import matplotlib.pyplot as plt
import numpy as np
import statistics
import math

def f3(x):
    #funcion que representa e^cos(x)
    x2 = np.cos(x)
    ans = np.exp(x2)
    return ans

def der_f3(x):
    #funcion que representa la derivada analitica de e^cos(x)
    ans = -f3(x)* np.sin(x)
    return ans

def f4(x):
    #funcion que representa ln(x^2)
    x2 = x * x
    ans = np.log(x2)
    return ans

def main():
    f1 = np.sin #funcion seno
    der_f1 = np.cos #derivada analitica de f1
    f2 = np.poly1d([4,5,-7,3]) #polinomio 4x^3 + 5x^2 -7x + 3
    der_f2 = np.poly1d([12,10,-7]) #derivada analitica de f2

    #########Diferenciación########

    xd = np.linspace(-20, 20, 400)
    yda = []
    for x in xd:
        yda.append(der_f3(x))
    plt.plot(xd,yda,'m', label="Derivada analitica")

    value_h = [0.001, 0.2, 0.45, 2, 5, 7]
    h = value_h[3]
    yd1, yd2, yd3 = [], [], []
    for x in xd:
        yd1.append(dif_fin_adelante(f3, x, h))
        yd2.append(dif_fin_atras(f3, x, h))
        yd3.append(dif_fin_centrado(f3, x, h))

    plt.plot(xd, yd1, label="Derivada adelante con h = {0}".format(h))
    plt.plot(xd, yd2, label="Derivada atras con h = {0}".format(h))
    plt.plot(xd, yd3, label="Derivada centrada con h = {0}".format(h))
    plt.legend(loc='upper center', bbox_to_anchor=(0.5, -0.05),shadow=True, ncol=4)
    plt.title("Diferenciacion para e^cos(x)")
    plt.grid()
    plt.show()

    #Calculo error
    error = []
    for i in range(len(yda)):
        error.append(abs((yd3[i] - yda[i])/yda[i]))
    error_medio = statistics.mean(error)
    print("El error relativo promedio para h = {0} es {1}".format(h, error_medio))
    desv_error = statistics.stdev(error)
    print("La desviacion del error para h = {0} es {1}".format(h, desv_error))


    #########Integración########
    #integracion para f1
    a, b, n = 0, math.pi/6, 20
    print("Integración por regla del rectangulo para f1 en el intervalo [{0}, {1}] = {2}".format(a, b, rectangulo(f1, a, b, n)))
    print("Integración por regla del trapezoide para f1 en el intervalo [{0}, {1}] = {2}".format(a, b, trapezoide(f1, a, b, n)))
    print("Integración por regla de simpson para f1 en el intervalo [{0}, {1}] = {2}".format(a, b, simpson(f1, a, b, n)))
    #integracion para f2
    a, b, n = -7, 25, 30
    print("Integración por regla del rectangulo para f2 en el intervalo [{0}, {1}] = {2}".format(a, b, rectangulo(f2, a, b, n)))
    print("Integración por regla del trapezoide para f2 en el intervalo [{0}, {1}] = {2}".format(a, b, trapezoide(f2, a, b, n)))
    print("Integración por regla de simpson para f2 en el intervalo [{0}, {1}] = {2}".format(a, b, simpson(f2, a, b, n)))
    #integracion para f4
    a, b, n = 2, 10, 40
    print("Integración por regla del rectangulo para f4 en el intervalo [{0}, {1}] = {2}".format(a, b, rectangulo(f4, a, b, n)))
    print("Integración por regla del trapezoide para f4 en el intervalo [{0}, {1}] = {2}".format(a, b, trapezoide(f4, a, b, n)))
    print("Integración por regla de simpson para f4 en el intervalo [{0}, {1}] = {2}".format(a, b, simpson(f4, a, b, n)))

    return

main()
