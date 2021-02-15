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

def householder(datos):
    """
    Entrada: Una lista de tuplas (ti, yi) que representan los datos
    Salida: El polinomio interpolante hecho con metodo de transformaciones Householder
    """
    m = n = len(datos)
    A = [[0 for _ in range(n)] for _ in range(m)]
    b = [0 for _ in range(m)]
    #Creacion vector b
    for i in range(m):
        b[i] = datos[i][1]
    #Creacion matriz A
    for i in range(m):
        A[i][0] = 1
        for j in range(1, n):
            A[i][j] = datos[i][0] ** j
    A = np.array(A, dtype=float)
    #Se escoge el menor entre m y n para hallar la diagonal de la matriz sin errores de indice
    l = min(m, n)
    for i in range(l):
        pivote = A[i][i]
        #vector a que representa cada una de las columnas de A, con 0s encima del pivote
        a = A[:, [i]]
        #Todo por encima del pivote tiene que ser 0
        for j in range(i):
            a[j][0] = 0
        #Alpha es la norma del vector a
        alpha = np.linalg.norm(a)
        #se crea el vector ei
        ei = np.zeros((m , 1))
        #Dependiendo del ei se acomoda el alpha con signo contrario al pivote en la pos i (columna)
        ei[i] = -(np.sign(pivote)) * alpha
        #El vector v = a - alpha*ei
        v = a - ei
        vt = np.transpose(v)
        I = np.identity(m)
        #Creacion de la matriz H
        Hi = I - (2 * (np.matmul(v, vt) / np.matmul(vt, v)))

        A = np.matmul(Hi, A).round(5)
        b = np.matmul(Hi, b).round(5)
        #Se redondea con 5 para quitar la notacion cientifica


    #Se redondea a 3 para manejar datos con 3 decimales
    A = np.round(A, 3)
    b = np.round(b, 3)
    #Reduzco el problema principal en un sistema triangular equivalente
    R = A[0:n, 0:n]
    b1 = b[0:n]
    #Resuelvo el sitema triangular con sustitución sucesiva hacia atras
    x = sust_atras(R, b1)
    x.reverse()
    pol = np.poly1d(x)

    return pol
