from pypoly import X
import numpy as np

def sust_adelante(A, b):
    """
    Entrada: Una matriz A (cuadrada nxn) triangular inferior y un vector b nx1
    Salida: x como la solucion de Ax = b, con metodo de sustitucion sucesiva hacia adelante
    """
    n = len(A)
    x = [0] * n

    x[0] = b[0]/A[0][0]
    for i in range(1,n):
        sigma = 0.0
        for j in range(0, i):
            sigma += A[i][j] * x[j]
        x[i] = (b[i] - sigma) / A[i][i]

    return x

def newton(datos):
    """
    Entrada: Un conjunto de datos (ti, yi)
    Salida: Polinomio interpolante del conjunto de datos con metodo de Newton
    """
    n = len(datos)
    funciones_base = []
    for j in range(n):
        phi = 1
        for k in range(j):
            #Calculo de la funcion base
            phi *= (X - datos[k][0]) #la X sirve para dejar la expresion como una ecuacion que posteriormente se podra evaluar
        #Guardamos la funciones base, para calcular la matriz A despues
        funciones_base.append(phi)

    #A y b para el sistema de ecuaciones
    A = np.ones((n, n))
    b = [x[1] for x in datos]

    #Armamos la matriz A
    for i in range(n):
        for j in range(1, n):
            A[i][j] = funciones_base[j](datos[i][0]) #funciones base evaluadas en el t respectivo

    #Coeficientes del polinomio
    x = sust_adelante(A, b)

    #Calculo del polinomio
    pol = 0
    for i in range(n):
        pol += ((funciones_base[i]) * x[i])

    return pol
