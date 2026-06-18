# Solution using "User Input"

import numpy as np
import matplotlib.pyplot as plt  # to plot Graph
import pandas as pd


# User input eqn
eqn = input("Enter the function of variable x using numpy syntax in Python : ")
a,b = map(float,input("Enter Two initial guesses using space: ").split())

def f(x):
    try:
        return eval(eqn)
    except(SyntaxError,NameError,ZeroDivisionError,TypeError):
        print("!! Invalid Syntax !!")
        exit(0)



a,b = -2,-1
fa, fb = f(a),f(b)
if fa * fb > 0:
    print(f"No root lies between {a} and {b}")
    exit(0)
else:
    E = float(input("Enter tolearable error : "))
    N = int(input("Enter the max no. of iterations : "))
    itr = 1

    T = []
    mid_points = []    # List of Mid Points

    while itr <= N:
        c = (a+b)/2
        fc = f(c)

        mid_points.append(c)
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
        mid_points = np.array(mid_points)
        y = np.zeros_like(mid_points)
        x = np.linspace(a-10,b+10,1000)   # 1000 denotes number of points

        plt.figure(figsize=(8,4))
        plt.plot(x,f(x),label='f(x)',color='red',linestyle='dotted')
        plt.axhline(0,label='x-axis',color='g')
        plt.axhline(0,label='y-axis',color='black')
        plt.grid(True)
        plt.legend(loc='upper right')
        plt.xlabel('x',color='orange')
        plt.xlabel('y',color='blue')
        plt.scatter('x','y',marker='o',color='blue')
        
        for i, v in enumerate(mid_points):
            plt.text(v,0,str(i+1))
        plt.scatter(mid_points,f(mid_points),color="purple")

        plt.show()
        table = pd.DataFrame(T,columns=['Iteration','a','b','c','fa','fb','fc','Error'])

        
        print(f"Iterations  : {itr}")
        print(f"Value       :{c}")


