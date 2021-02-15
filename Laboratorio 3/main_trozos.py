from interpo_trozos import trozos
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
    salto = 2
    #Division de los datos en entrenamiento y validacion
    for i in range(len(data)):
        if i % salto == 0:
            data_en.append(data[i])
        else:
            data_val.append(data[i])

    A = trozos(data_en)
    #Graficar funciones a trozos
    plt.plot(0,0,'g', label="Polinomio de ajuste con salto = {0}".format(salto))
    for i in range(len(data_en)-1):
        punto1 = data_en[i]
        punto2 = data_en[i+1]
        x = np.linspace(punto1[0], punto2[0], 2)
        y = A[0][i] * x + A[1][i] #Polinomio de grado 1
        plt.plot(x,y,'g')

    x_en = [x[0] for x in data_en]
    y_en = [x[1] for x in data_en]
    x_val = [x[0] for x in data_val]
    y_val = [x[1] for x in data_val]

    plt.plot(x_en,y_en,'ro', label="Datos entrenamientos")
    plt.plot(x_val,y_val,'bo', label="Datos validacion")
    plt.title("Interpolacion polinomial a trozos")
    plt.legend()
    plt.grid()
    if bd[1] == "deaths":
        plt.xlabel('Dias')
        plt.ylabel('Muertos por Covid 19 en Colombia')
    elif bd[1] == "price":
        plt.xlabel('Dias')
        plt.ylabel('Precio del Bitcoin')
    plt.show()

    #Calculo de error medio y desviacion del error para trozos
    ultimo = x_en[-1]
    yp3 = []
    for t in x_val:
        if t < ultimo:
            i = (t // salto) - 1
            yp3.append(A[0][i] * t + A[1][i])
    error = []
    for i in range(len(yp3)):
        error.append(abs(yp3[i] - y_val[i]))
    error_medio = statistics.mean(error)
    print("El error promedio es {0}".format(error_medio))
    desv_error = statistics.stdev(error)
    print("La desviacion del error es {0}".format(desv_error))

main()
