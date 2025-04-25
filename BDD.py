import math

def FDD(f,x,h):
    return ((f(x)-f(x-h))/h)

func = input("enter the funcation in terms of x (eg: x**3-2*x,math.sin(x)) : ")
x0 = float(input("enetr the point at which to be determined : "))
h = float(input("Enter the stepsize :  "))

f = lambda x: eval(func)

result = FDD(f,x0,h)
print(f"FDD at x ={x0} is approximately {result}")
