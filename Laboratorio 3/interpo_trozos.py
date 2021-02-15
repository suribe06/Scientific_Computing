import numpy as np

def trozos(datos):
    """
    Entrada: Un conjunto de datos (ti, yi)
    Salida: Una matriz A que representa una matriz de polinomios de grado 1, que representan las ecuaciones de las n-1 rectas.
    La fila 1 de la matriz representa las pendientes y la fila 2 representa los interceptos.
    """
    n = len(datos)
    A = np.ones((2, n-1)) #matriz de polinomios

    for i in range(n-1):
        punto1 = datos[i]
        punto2 = datos[i+1]
        m = (punto2[1] - punto1[1]) / (punto2[0] - punto1[0]) #pendiente
        b = punto1[1] - (m * punto1[0]) #intercepto
        A[0][i] = m
        A[1][i] = b

    return A
