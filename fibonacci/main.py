#!/usr/bin/env python3
import sys
from fibonacci import Fibonacci
import matplotlib.pyplot as plt

def main():
    try:
        n = int(input("Ingrese el número de términos de Fibonacci a graficar: "))
        if n <= 0:
            raise ValueError
    except ValueError:
        print("Por favor ingrese un entero positivo.")
        sys.exit(1)

    fib = Fibonacci(n)
    x = list(range(1, fib.n_terms + 1))
    y = fib.sequence

    plt.figure()
    plt.plot(x, y, marker='o')
    plt.title(f'Sucesión de Fibonacci ({n} términos)')
    plt.xlabel('Término')
    plt.ylabel('Valor')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    main()
