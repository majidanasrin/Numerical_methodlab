def f(x):
    return x**2 + x - 2  

def bisection(a, b, it, tol):
    if f(a) * f(b) >= 0: 
        print("The function must have opposite signs at the endpoints a and b.")
        return None
    
    count = 0
    
    while (b - a) / 2.0 > tol and count < it:
        c = (a + b) / 2.0  
        
        if abs(f(c)) < tol:  
            return c
        
        if f(c) * f(a) < 0:  
            b = c
        else:  
            a = c
        
        count += 1
        
    return (a + b) / 2  

if __name__ == "__main__":
    
    a = float(input("Enter the lower bound a: "))
    b = float(input("Enter the upper bound b: "))
    tol = .00001
    it = 20  

   
    root = bisection(a, b, it, tol)

    
    if root is not None:
        print(f"The root is approximately: {root}")
    else:
        print("No root found.")
