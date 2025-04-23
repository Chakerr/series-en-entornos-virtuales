# taylor.py
import math

def taylor_exp(x: float, n_terms: int) -> float:
    """
    Aproxima e^x usando n_terms de la serie de Taylor:
      e^x ≈ sum_{k=0..n_terms-1} x^k / k!
    """
    suma = 0.0
    for k in range(n_terms):
        suma += x**k / math.factorial(k)
    return suma
