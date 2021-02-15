import numpy as np

def gauss(A, b):
    assert len(A) == len(A[0]) and len(b) == len(A)
    """
    Entrada: A es una matriz n x n y b es un vector n x 1
    Salida: x como la solucion de Ax = b resuelto con metodo de Gauss
    """

    determinante = np.linalg.det(A)
    #Revisamos con el determiannte de la matriz si tiene solucion
    if determinante != 0:
        n = len(A)
        x = [0] * n #vector solucion

        #volver la matriz A en triangular superior
        for i in range(n-1):
            cont = i
            #si el pivote es 0 hago cambio de filas hasta que el pivote sea diferente de 0
            while A[i][i] == 0 and cont < n-1:
                #cambio de filas en A
                temp = list(A[cont+1])
                A[cont+1] = A[i]
                A[i] = temp
                #cambio de filas en b
                temp2 = int(b[cont+1])
                b[cont+1] = b[i]
                b[i] = temp2

                cont += 1

            pivote = A[i][i]

            #si por mas que se cambien filas el pivote es 0, entonces el sistema no tiene solucion
            if pivote == 0:
                print("El sistema no tiene solucion")
                break

            #matriz de eliminacion elemental E
            E = np.identity(n) #crear matriz identidad nxn
            for j in range(i+1,n):
                if A[j][i] != 0:
                    E[j][i] = A[j][i] / (-pivote)


            A = np.matmul(E, A)
            b = np.matmul(E, b)


        #aplicar sustitucion sucesiva hacia atras
        x[n-1] = b[n-1]/A[n-1][n-1]

        for i in range(n-2, -1, -1):
            sigma = 0.0
            for j in range(i+1, n):
                sigma += A[i][j] * x[j]
            x[i] = (b[i] - sigma) / A[i][i]

        return x

    else:
        print("El sistema no tiene solucion")


def gauss_jordan(A, b):
    assert len(A) == len(A[0]) and len(b) == len(A)
    """
    Entrada: A es una matriz n x n y b es un vector n x 1
    Salida: x como la solucion de Ax = b resuelto con metodo de Gauss-Jordan
    """
    determinante = np.linalg.det(A)
    #Revisamos con el determinante de la matriz si tiene solucion
    if determinante != 0:
        n = len(A)
        x = [0] * n #vector solucion

        #volver la matriz A en triangular superior
        for i in range(n-1):
            cont = i
            #si el pivote es 0 hago cambio de filas hasta que el pivote sea diferente de 0
            while A[i][i] == 0 and cont < n-1:
                #cambio de filas en A
                temp = list(A[i+1])
                A[i+1] = A[i]
                A[i] = temp
                #cambio de filas en b
                temp2 = int(b[i+1])
                b[i+1] = b[i]
                b[i] = temp2

                cont += 1

            pivote = A[i][i]

            #si por mas que se cambien filas el pivote es 0, entonces el sistema no tiene solucion
            if pivote == 0:
                print("El sistema no tiene solucion")
                break

            #matriz de eliminacion elemental E
            E = np.identity(n) #crear matriz identidad nxn
            for j in range(i+1,n):
                E[j][i] = A[j][i] / (-pivote)

            A = np.matmul(E, A)
            b = np.matmul(E, b)

        #volver la matriz A en triangular inferior
        for i in range(n-1, 0, -1):
            cont = i
            #si el pivote es 0 hago cambio de filas hasta que el pivote sea diferente de 0
            while A[i][i] == 0 and cont < n-1:
                #cambio de filas en A
                temp = list(A[i+1])
                A[i+1] = A[i]
                A[i] = temp
                #cambio de filas en b
                temp2 = int(b[i+1])
                b[i+1] = b[i]
                b[i] = temp2

                cont += 1

            pivote = A[i][i]

            #si por mas que se cambien filas el pivote es 0, entonces el sistema no tiene solucion
            if pivote == 0:
                print("El sistema no tiene solucion")
                break

            #matriz de eliminacion elemental E
            E = np.identity(n) #crear matriz identidad nxn
            for j in range(n-2,-1, -1):
                E[j][i] = A[j][i] / (-pivote)

            A = np.matmul(E, A)
            b = np.matmul(E, b)

        #Con la matriz diagonal resolvemos el sistema
        for i in range(n):
            x[i] = b[i] / A[i][i]

        return x

    else:
        print("El sistema no tiene solucion")
