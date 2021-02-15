import matplotlib.pyplot as plt
import itertools

def floating_point_system(beta, t, L, U):
    """
    Entrada: beta que corresponde a la base o raiz, t que corresponde a la presicion y L, U corresponden a rango del exponente
    Salida: Un sistema punto flotante normalizado correspondiente a las parametros.
    """
    #Calculo de la cantidad de numeros flotantes del sistema
    N = 2 * (beta - 1) * beta**(t-1) * (U - L + 1) + 1
    #Calculo del numero mas pequeno que se puede representar
    UFL = beta**(L)
    #Calculo del numero mas grande que se puede representar
    OFL = beta**(U+1) * (1 - beta**(-t))

    #Tabla de verdad
    table = list(itertools.product([0, 1], repeat=t-1))

    numbers = []
    for e in range(L, U+1):
        #Calculo de la mantisa
        for i in range(2**(t-1)):
            #xi empieza en 1 pues para beta=2 el bit inicial siempre es 1
            xi = 1
            for j in range(t-1):
                if table[i][j] == 1:
                    #Cuando haya un 1 en la tabla de verdad hago la operacion de cada di
                    xi += (1.0 / beta**(j+1))
            num = xi * beta**(e)
            #Agrego al sitema el numero positivo y negativo (+-)
            numbers.append(num)
            numbers.append(-num)

    numbers.append(0.0)
    return numbers, N, UFL, OFL

def graficar(x, N):
    y = [0] * N
    plt.axhline(0, color='black')
    plt.ylim(-3, 3)
    plt.plot(x, y, 'ro')
    plt.grid()
    plt.show()
