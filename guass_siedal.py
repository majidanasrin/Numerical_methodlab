import numpy as np

def gauss_seidel(A, b, tol=1e-6, max_iter=1000):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float)
    n = len(b)
    
    x = np.zeros_like(b)  
    for k in range(max_iter):
        x_old = x.copy()
        
        for i in range(n):
            sum1 = np.dot(A[i, :i], x[:i])
            sum2 = np.dot(A[i, i+1:], x_old[i+1:])
            x[i] = (b[i] - sum1 - sum2) / A[i, i]
        
        if np.linalg.norm(x - x_old, ord=np.inf) < tol:
            return x  

    raise ValueError("Solution did not converge within the maximum number of iterations")

A = [[2, -1, 0], [-1, 2, -1], [0, -1, 2]]
b = [7, 1, 1]

solution = gauss_seidel(A, b)
print("Solution:", solution)
