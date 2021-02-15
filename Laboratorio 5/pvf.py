import numpy as np

def diferencias_finitas(ed, a, b, ya, yb, pi):
    h = (b-a)/(pi+1)
    A = np.zeros((pi,pi))
    b = np.zeros(pi)
    t = a + h
    for i in range(1,pi+1):
        if i == 1:
            bi = (ed(t) * (h**2)) - ya
            #Si es la primer ecuacion agrego un 1 a la derecha
            A[i-1][i] = 1
        elif i == pi:
            bi = (ed(t) * (h**2)) - yb
            #Si es la ultima ecuacion agrego un 1 a la izquierda
            A[i-1][i-2] = 1
        else:
            bi = (ed(t) * (h**2))
            #se agrega un 1 a ambos lados
            A[i-1][i-2] = 1
            A[i-1][i] = 1
        A[i-1][i-1] = -2 #la diagonal de la matriz siempre es -2
        b[i-1] = bi
        t += h

    b = np.transpose(b)
    A = np.linalg.inv(np.matrix(A))
    x = np.matmul(A, b)
    return x.tolist()[0]

def elementos_finitos(ed, a, b, ya, yb, pi):
    h = (b-a)/(pi+1)
    A = [None for _ in range(pi+2)]
    bm = [None for _ in range(pi+2)]
    u = [(1,i) for i in range(pi+2)]
    du = []
    for i in range(1,len(u)):
        du.append((u[i][0] * u[i][1], u[i][1]-1))
    ddu = []
    for i in range(1,len(du)):
        ddu.append((du[i][0] * du[i][1], du[i][1]-1))

    eq, eq2 = [], []
    for i in range(len(u)):
        eq.append(a ** u[i][1])
        eq2.append(b ** u[i][1])
    A[0], A[1] = eq, eq2
    bm[0], bm[1] = ya, yb
    t = a + h
    for i in range(2,pi+2):
        equi = [0, 0]
        for x in ddu:
            equi.append(x[0]*(t ** x[1]))
        A[i] = equi
        bm[i] = ed(t)
        t += h
    bm = np.transpose(bm)
    A = np.linalg.inv(np.matrix(A, dtype='float'))
    x = np.matmul(A, bm)
    coef = x.tolist()[0]
    coef.reverse()
    p = np.poly1d(coef)
    return p
