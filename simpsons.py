import numpy as np

def simpsons_1_3_rule(f, a, b, n):
    """
    Approximate the integral of f(x) from a to b using Simpson's 1/3 Rule with n subintervals.
    
    Parameters:
    f : function
        The function to integrate.
    a : float
        The lower bound of the integration.
    b : float
        The upper bound of the integration.
    n : int
        The number of subintervals (must be even).
        
    Returns:
    float
        The estimated integral value.
    """
    # Ensure n is even
    if n % 2 != 0:
        raise ValueError("The number of subintervals (n) must be even.")
    
    # Step size (h)
    h = (b - a) / n  # This is where h is calculated
    
    # Initialize the sum for Simpson's 1/3 rule
    sum_odd = 0  # Sum for odd indices
    sum_even = 0  # Sum for even indices
    
    # Evaluate the function at the endpoints (y0 and yn)
    integral = f(a) + f(b)
    
    # Evaluate the function at the odd indices (multiply by 4)
    for i in range(1, n, 2):
        sum_odd += f(a + i * h)
    
    # Evaluate the function at the even indices (multiply by 2)
    for i in range(2, n, 2):
        sum_even += f(a + i * h)
    
    # Apply the Simpson's 1/3 Rule formula
    integral += 4 * sum_odd + 2 * sum_even
    
    # Multiply by h / 3 to finalize the result
    integral *= h / 3
    
    return integral

# Example usage
import math

def get_user_function():
    """
    Prompt the user to input a mathematical function to integrate.
    The user can input a function in terms of x (e.g., "sin(x)", "x**2").
    """
    func_input = input("Enter the function to integrate (in terms of 'x', e.g., 'sin(x)', 'x**2'): ")
    # Replace the user's input with a valid function for eval
    return lambda x: eval(func_input)

# Get user inputs for the function and the limits
user_function = get_user_function()

# Get the integration limits from the user
a = float(input("Enter the lower limit of integration (a): "))
b = float(input("Enter the upper limit of integration (b): "))

# Get the number of subintervals (n) from the user (must be even)
n = int(input("Enter the number of subintervals (must be even): "))

# Approximate the integral using Simpson's 1/3 Rule
result = simpsons_1_3_rule(user_function, a, b, n)

# Print the result
print(f"Approximate integral result: {result}")
