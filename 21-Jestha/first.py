import numpy as np

def f(x):
    return x * x - 4 * x - 10 # f(x) = x2 + 4x - 10 

a,b = -2,-1
fa, fb = f(a),f(b)
if fa * fb > 0:
    print(f"No root lies between {a} and {b}")
    exit(0)
else:
    E = 1e-20 # Error Tolerance
    N = 100   # Max no. of Iterations
    itr = 1   # Begin Iteration Counter 

    while itr <= N:
        c = (a+b)/2
        fc = f(c)
        if fc ==0:
            break
        elif fa * fc > 0:
            a = c
            fa = fc
        else:
            b = c
        error = abs(a - b)
        if(error < E):
            break
        else:
            itr += 1

    if itr > N:
        print(f"Solution does not reach in {N} iterations !")
        
    else:
        print(f"Approximate Solution in : ")
        print(f"Iterations  : {itr}")
        print(f"Value       :{c}")