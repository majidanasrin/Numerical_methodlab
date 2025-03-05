import numpy as np

# Define the function f(x) = sin(x)
def f(x):
    return np.sin(x)


x = np.pi / 4  
h = 0.05  

# Apply central difference method
derivative_approx = (f(x + h) - f(x - h)) / (2 * h)

print("value is : ",derivative_approx)
