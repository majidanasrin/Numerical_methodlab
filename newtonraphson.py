import sympy as sp
import numpy as np

x = sp.symbols('x')
f = x**3 +2*x-2
f_prime = sp.diff(f, x)

f_func = sp.lambdify(x, f, 'numpy')
f_prime_func = sp.lambdify(x, f_prime, 'numpy')

def newton_raphson(a, tol, max_it):
    for i in range(1, max_it+1):
        c = a - f_func(a) / f_prime_func(a)
        if abs(f_func(c)) < tol:
            return c
        a = c

    print("Maximum iterations are reached. Solution may not have converged.")
    return None 

initial_guess = float(input("Enter the initial guess: "))
tol = 0.000001
max_it = 100

root = newton_raphson(initial_guess, tol, max_it)
if root is not None:
    print(f"Root found: {root}")
else:
    print("Failed to converge to a root")
