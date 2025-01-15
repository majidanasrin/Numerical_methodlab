def f(x):
    return x**3 -2*x -1

def false_position(a,b,tol,max_it):
    if f(a) * f(b) > 0 :
        print("the function has the same sign at points a and b,so choose different values ")
        return None 
    for i in range (1,max_it+1):
        c = (a * f(b) - b*f(a))/(f(b) - f(a))

        if abs(f(c)) < tol:
            print(f"Root found: {c}")  
            return c
        
        if f(c) * f(a) < 0:  
            b = c
        else:  
            a = c
    print("Maximum iterations are reached .Solution may not have converged .")
    return None

def interval(start,end,stepsize):
    a = start
    b = a + stepsize

    while b <= end :
        if f(a) * f(b) < 0:
            return a, b
        a = b
        b+= stepsize
    return None,None

if __name__ == "__main__":

        start = float(input("Enter the start of the range for thr interval :"))
        end = float(input("Enter the end of the range for thr interval :"))
        stepsize = float(input("Enter the step size for searching the interval (eg : 1): "))
        tol = 0.000001
        max_it = int(input("Enter the maximum number of iteration : "))

        a,b = interval(start,end,stepsize)

        if a is None or b is None :
            print ("No valid intervals in given range ")
        else:
            print(f"inerval found : a = {a} , b= {b}")
            false_position(a,b,tol,max_it) 


