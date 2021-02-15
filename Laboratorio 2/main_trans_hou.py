from trans_householder import householder
from sys import stdin
import numpy as np
import matplotlib.pyplot as plt
import statistics

bd = None
def read_data():
    global bd
    data = [None for _ in range(50)]
    bd = stdin.readline().split()
    for i in range(50):
        line = stdin.readline().split()
        data[i] = (int(line[0]), float(line[1]))
    return data

def main():
    global bd
    data = read_data()
    data_en = []
    data_val = []
    #Division de los datos en entrenamiento y validacion
    for i in range(len(data)):
        if i % 2 == 0:
            data_en.append(data[i])
        else:
            data_val.append(data[i])

    #Calculo de los coeficientes del polinomio de ajuste con los datos de entrenamiento
    n = 10 #parametros
    x = householder(n, data_en)
    #Armo el polimomio de ajuste respectivo
    x.reverse()
    p = np.poly1d(x)
    print("Polinomio de ajuste:")
    print(p)
    #Polinomio continuo
    xp = np.linspace(1, len(data), 500)
    yp = []
    for t in xp:
        yp.append(p(t)) #Evaluacion del polinomio
    #Graficar
    x1 = [x[0] for x in data_en]
    y1 = [x[1] for x in data_en]

    data_val.pop() #para evitar extrapolacion
    x2 = [x[0] for x in data_val]
    y2 = [x[1] for x in data_val]

    plt.plot(x1,y1,'ro', label="Datos entrenamientos")
    plt.plot(x2,y2,'bo', label="Datos validacion")
    plt.plot(xp,yp,'g', label="Polinomio de ajuste")
    plt.title("Metodo transformaciones Householder")
    plt.legend()
    plt.grid()

    if bd[0] == "day":
        plt.xlabel('Dias')
        plt.ylabel('Muertos por Covid 19 en Colombia')
    elif bd[0] == "month":
        plt.xlabel('Meses')
        plt.ylabel('Precio del Petroleo WTI')

    plt.show()

    #Calculo de error medio y desviacion del error
    yp2 = []
    for t in x2:
        yp2.append(p(t))
    error = []
    for i in range(len(y2)):
        error.append(abs(yp2[i]-y2[i]))
    error_medio = statistics.mean(error)
    print("El error promedio es {0}".format(error_medio))
    desv_error = statistics.stdev(error)
    print("La desviacion del error es {0}".format(desv_error))

main()
