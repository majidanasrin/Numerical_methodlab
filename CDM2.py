import math

def sec_der(f,x,h):
    return((f(x+h)-2*f(x) + f(x-h))/(h**2))

func_input = input("Enter the function in terms of x (eg = x**3 + 2*x**2+x , math.sin(x)) :")
x0 = float(input("Enter the point at which to compute : "))
h = float(input("Enter the stepsize : "))


f = lambda x: eval(func_input)

result = sec_der(f , x0 , h)
print(f"The second derivative of f at x = {x0} is approximately {result}")