def elimination(a,b):
    n = len(a)

#find the maximum element in current coloumn 
    for i in range(n):
        max_row = max(range(i,n),key = lambda r: abs(a[r][i]))
        if a[max_row][i] ==0:
            raise ValueError("No unique solution exists")
        # swap any row if needed     
        a[i],a[max_row]=a[max_row],a[i]
        b[i],b[max_row]=b[max_row],b[i]

        #removing the entries below the pivot
        for j in range(i+1,n):
            factor = a[j][i]/a[i][i]
            for k in range (i,n):
                a[j][k] -=factor*a[i][k]
            b[j]-=factor * b[i]

    x = [0] * n
    for i in reversed(range(n)):
        temp = b[i]
        for j in range(i + 1, n):
            temp -= a[i][j] * x[j]
        x[i] = temp / a[i][i]

    return x

n = int(input("Enter number of variables: "))

print("Enter coefficient matrix A row by row:")
a = [list(map(float, input().split())) for _ in range(n)]

print("Enter constant vector b (space separated):")
b = list(map(float, input().split()))
if len(b) != n:
    raise ValueError("Length of b must match number of equations.")

# ---------- SOLUTION --------------
solution = elimination(a, b)

# ---------- OUTPUT ----------------
print("\n🔢 Solution:")
for i in range(n):
    print(f"x{i+1} = {solution[i]:.4f}")