#!/usr/bin/env python3
import sys
import matplotlib.pyplot as plt
from taylor import taylor_exp
import math

def main():
    try:
        x = float(input("Ingrese el valor de x para e^x: "))
        n = int(input("Ingrese el número de términos de la serie: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Por favor ingrese un número real para x y un entero positivo para términos.")
        sys.exit(1)

    # Cálculo de aproximación y función real
    approx = taylor_exp(x, n)
    real    = math.exp(x)

    print(f"\ne^({x}) aproximado con {n} términos: {approx}")
    print(f"e^({x}) real: {real}\n")

    # Para graficar: vemos cómo converge en los primeros n puntos
    xs = [i * x/(n-1) for i in range(n)]  # puntos entre 0 y x
    ys_approx = [taylor_exp(val, n) for val in xs]
    ys_real    = [math.exp(val) for val in xs]

    plt.figure()
    plt.plot(xs, ys_real,    label="e^x real")
    plt.plot(xs, ys_approx, '--', label=f"Aprox. Taylor ({n} términos)")
    plt.title(f"Aproximación de e^x con Taylor en [0, {x}]")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
