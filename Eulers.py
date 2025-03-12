
def Eulermethod(f,x0,y0,x_final, h):
    x = x0
    y = y0
    
    while x< x_final:
        y = y+h*f(x,y)
        x = x+h
    return y

def f(x, y):
    return x**3 - 2*y

x0 , y0 = 0, 0
x_final = 2
h = 0.2

y_approx = Eulermethod(f,x0,y0,x_final, h)
print(f"Approximate value of y({x_final}) = {y_approx}")