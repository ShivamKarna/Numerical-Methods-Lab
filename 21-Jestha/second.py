# Solution with "Table"

import numpy as np
import pandas as pd


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

    T = []    # Initialize list

    while itr <= N:
        c = (a+b)/2
        fc = f(c)

        T.append([itr,round(a,4),round(b,4),round(c,4),round(fa,4),round(fb,4),round(fc,4),abs(a-b)]) # List of List

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
        table = pd.DataFrame(T,columns=['Iteration','a','b','c','fa','fb','fc','Error'])
        print(table.to_string(index=False))
        print(f"Iterations  : {itr}")
        print(f"Value       : {np.round(c,7)}")