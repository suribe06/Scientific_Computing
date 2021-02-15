import numpy as np

def dif_fin_adelante(f, x, h):
    #Entrada: f que representa una funcion, x que representa el punto a evaluar y h que representa un desplazamiento
    #Salida: La derivada aproximada de la funcion f evaluada en x por metodo diferencias finitas hacia adelante
    ans = (f(x + h) - f(x)) / h
    return ans

def dif_fin_atras(f, x, h):
    #Entrada: f que representa una funcion, x que representa el punto a evaluar y h que representa un desplazamiento
    #Salida: La derivada aproximada de la funcion f evaluada en x por metodo diferencias finitas hacia atras
    ans = (f(x) - f(x - h)) / h
    return ans

def dif_fin_centrado(f, x, h):
    #Entrada: f que representa una funcion, x que representa el punto a evaluar y h que representa un desplazamiento
    #Salida: La derivada aproximada de la funcion f evaluada en x por metodo diferencias centradas
    ans = (f(x + h) - f(x - h)) / (2 * h)
    return ans
