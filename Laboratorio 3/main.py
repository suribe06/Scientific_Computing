from interpo_householder import householder
from interpo_lagrange import lagrange
from interpo_newton import newton
from sys import stdin
import numpy as np
import matplotlib.pyplot as plt
import statistics

bd = None
def read_data():
    global bd
    data = [None for _ in range(60)]
    bd = stdin.readline().split()
    for i in range(60):
        line = stdin.readline().split()
        data[i] = (int(line[0]), float(line[1]))
    return data

def main():
    global bd
    data = read_data()
    data_en = []
    data_val = []
    #variable salto para separacion datos en entrenamiento y validacion
    salto = 5
    #Division de los datos en entrenamiento y validacion
    for i in range(len(data)):
        if i % salto == 0:
            data_en.append(data[i])
        else:
            data_val.append(data[i])

    #Calculo del polinomio de ajuste
    #metodo polinomico (householder)
    #p = householder(data_en)
    #metodo de lagrange
    p = lagrange(data_en)
    #metodo de newton
    #p = newton(data_en)

    #Polinomio continuo
    ultimo = data_en[-1][0] #para evitar extrapolacion
    xp = np.linspace(1, ultimo, 500)
    yp = []
    for t in xp:
       yp.append(p(t)) #Evaluacion del polinomio

    x_en = [x[0] for x in data_en]
    y_en = [x[1] for x in data_en]
    x_val = [x[0] for x in data_val]
    y_val = [x[1] for x in data_val]

    plt.plot(x_en,y_en,'ro', label="Datos entrenamientos")
    plt.plot(x_val,y_val,'bo', label="Datos validacion")
    plt.plot(xp,yp,'g', label="Polinomio de ajuste con salto = {0}".format(salto))
    plt.title("Interpolacion polinomial")
    plt.legend()
    plt.grid()
    if bd[1] == "deaths":
        plt.xlabel('Dias')
        plt.ylabel('Muertos por Covid 19 en Colombia')
    elif bd[1] == "price":
        plt.xlabel('Dias')
        plt.ylabel('Precio del Bitcoin')
    plt.show()

    #Calculo de error medio y desviacion del error
    ultimo = x_en[-1]
    yp2 = []
    for t in x_val:
        if t < ultimo:
            yp2.append(p(t))
    error = []
    for i in range(len(yp2)):
        error.append(abs(yp2[i] - y_val[i]))
    error_medio = statistics.mean(error)
    print("El error promedio es {0}".format(error_medio))
    desv_error = statistics.stdev(error)
    print("La desviacion del error es {0}".format(desv_error))

main()
