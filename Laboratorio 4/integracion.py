import numpy as np

def rectangulo(f, a, b, n):
    #Entrada: f que representa una funcion. a y b que representan los limites de integracion
    #Salida: integral aproximada por metodo del rectangulo con cuadratura compuesta
    sigma = 0
    paneles = np.linspace(a,b,n)
    for i in range(1,len(paneles)):
        xi = paneles[i]
        xi_1 = paneles[i-1]
        sigma += (xi - xi_1) * f((xi_1 + xi)/2)
    return sigma

def trapezoide(f, a, b, n):
    #Entrada: f que representa una funcion. a y b que representan los limites de integracion
    #Salida: integral aproximada por metodo del trapezoide con cuadratura compuesta
    sigma = 0
    paneles = np.linspace(a,b,n)
    for i in range(1,len(paneles)):
        xi = paneles[i]
        xi_1 = paneles[i-1]
        sigma += (xi - xi_1) * (f(xi_1) + f(xi))
    ans = (1/2) * sigma
    return ans

def simpson(f, a, b, n):
    #Entrada: f que representa una funcion. a y b que representan los limites de integracion
    #Salida: integral aproximada por metodo de simpson con cuadratura compuesta
    sigma = 0
    paneles = np.linspace(a,b,n)
    for i in range(1,len(paneles)):
        xi = paneles[i]
        xi_1 = paneles[i-1]
        sigma += (xi - xi_1) * (f(xi_1) + (4 * f((xi_1 + xi)/2)) + f(xi))
    ans = (1/6) * sigma
    return ans
