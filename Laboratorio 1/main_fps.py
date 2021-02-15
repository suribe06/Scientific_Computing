from fps import floating_point_system, graficar

def parametros(beta, t, L, U):
    numbers, N, UFL, OFL = floating_point_system(beta, t, L, U)
    print("La cantidad de numeros flotantes del sistema es: {0}. El numero mas pequeño que se puede representar(UFL) es: {1} y el numero mas grande que se puede representar(OFL) es: {2}".format(N,UFL,OFL))
    graficar(numbers, N)

def main():
    parametros(2,3,-3,3)
    parametros(2,6,-3,3)

main()
