import numpy as np

def gauss_jordan(A, b):
    A = np.array(A, dtype=float)
    b = np.array(b, dtype=float).reshape(-1, 1)

    n = len(b)

    aug_matrix = np.hstack((A, b))

    for i in range(n):
        pivot = aug_matrix[i, i]
        if pivot == 0:
            raise ValueError("Zero pivot encountered, solution may not exist or be unique.")
        aug_matrix[i] = aug_matrix[i] / pivot

        for j in range(n):
            if i != j:
                factor = aug_matrix[j, i]
                aug_matrix[j] -= factor * aug_matrix[i]

    solution = aug_matrix[:, -1]
    return solution

A = [[2, -1, 1], [1, 3, 2], [1, -1, 3]]
b = [3, 12, 8]
solution = gauss_jordan(A, b)
print("Solution:", solution)
