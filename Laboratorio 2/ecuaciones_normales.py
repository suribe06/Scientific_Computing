import numpy as np

def sust_atras(A, b):
    """
    Entrada: Una matriz A (cuadrada nxn) triangular superior y un vector b nx1
    Salida: x como la solucion de Ax = b, con metodo de sustitucion sucesiva hacia atras
    """
    n = len(A)
    x = [0] * n

    x[n-1] = b[n-1]/A[n-1][n-1]
    for i in range(n-2, -1, -1):
        sigma = 0.0
        for j in range(i+1, n):
            sigma += A[i][j] * x[j]
        x[i] = (b[i] - sigma) / A[i][i]

    return x

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

def ecua_norm(parametros, datos):
    """
    Entrada: Un numero de parametros del polinomio y una lista de tuplas (ti, yi)
    Salida: El polinomio de ajuste del sistema en representacion de lista de coeficientes, hecho con metodo de
    ecuaciones normales
    """
    A = np.zeros((len(datos), parametros))
    b = [0 for i in range(len(datos))]
    #Creacion vector b
    for i in range(len(datos)):
        b[i] = datos[i][1]
    #Creacion matriz A
    for i in range(len(A)):
        A[i][0] = 1
        for j in range(1, len(A[0])):
            A[i][j] = datos[i][0] ** j
    #Sistema de ecucaciones normal. At*A es matriz no singular por lo que tiene solucion unica
    At = np.transpose(A)
    A = np.matmul(At, A)
    b = np.matmul(At, b)
    #Descomposicion de Cholesky. At*A = L*Lt
    L = np.linalg.cholesky(A)
    Lt = np.transpose(L)
    #Se resuelve el sistema triangular resultante
    y = sust_adelante(L, b)
    x = sust_atras(Lt, y)
    return x
