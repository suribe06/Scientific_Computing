from pypoly import X
import numpy as np

def lagrange(datos):
    """
    Entrada: Un conjunto de datos (ti, yi)
    Salida: Polinomio interpolante del conjunto de datos con metodo de Lagrange
    """
    n, pol = len(datos), 0
    for j in range(n):
        y = datos[j][1]
        prod1, prod2 = 1, 1
        for k in range(n):
            if k != j:
                #Calculo de las productorias
                prod1 *= (X - datos[k][0]) #la X sirve para dejar la expresion como una ecuacion que posteriormente se podra evaluar
                prod2 *= (datos[j][0] - datos[k][0])
        #Funciones base de Lagrange
        Lj = prod1 / prod2
        ans = (y * Lj)
        #Se suman las expresiones para obtener el polinomio interpolante
        pol += ans
    return pol
