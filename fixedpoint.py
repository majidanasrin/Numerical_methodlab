import sympy as sp
import numpy as np

x = sp.symbols('x')
f = x**3 + 2*x - 2

def g_func(x):
    return (x**3 - 2) / 2

f_func = sp.lambdify(x, f, 'numpy')

def fixed_point_iteration(a, tol, max_it):
    for i in range(1, max_it+1):
        c = g_func(a)
        
        if abs(c) > tol:  
            print(f"Value {c} too large. Stopping iteration.")
            return None
        
        if abs(f_func(c)) < tol:
            return c
        
        a = c

    print("Maximum iterations are reached. Solution may not have converged.")
    return None 

initial_guess = float(input("Enter the initial guess: "))
tol = 0.000001
max_it = 100

root = fixed_point_iteration(initial_guess, tol, max_it)
if root is not None:
    print(f"Root found: {root}")
else:
    print("Failed to converge to a root")
