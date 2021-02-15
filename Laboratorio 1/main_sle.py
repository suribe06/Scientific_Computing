from system_linear_equations import gauss, gauss_jordan
import numpy as np

def parametros(A, b):
    x1 = gauss(A, b)
    print("La solucion para el sistema Ax = b con metodo Gauss es: {0}".format(x1))

    x2 = gauss_jordan(A, b)
    print("La solucion para el sistema Ax = b con metodo Gauss-Jordan es: {0}".format(x2))

def main():
    A = [[2, 4, -2], [4, 9, -3], [-2, -3, 7]]
    b = [2, 8, 10]
    #A = [[0,0,-2],[0,1,4],[4,3,1]]
    #b = [2,8,4]
    #A = np.random.rand(100,100)
    #b = np.random.rand(100)
    parametros(A, b)

main()
