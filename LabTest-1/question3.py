"""
WAP in Python to display the graph of function x**2 * sin(x) + e ^ x= 3.
Use red color for 
"""

import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return x**2 * np.sin(x) + np.exp(x) -3 


plt.figure(figsize=(8,6))
x = np.linspace(-10,10,400)
y = f(x)
plt.plot(
    x,
    y,
    color='red',
    label=r'$x^2\sin(x) + e^x -3$'
)

plt.tick_params('x',colors='green')
plt.tick_params('y',colors='green')

plt.xlabel('X-axix',color='green')
plt.ylabel('Y-axis',color='green')

plt.grid(True,linestyle='--',alpha=0.7)
plt.title("Graph of r'$x^2\sin(x) + e^x -3$'")
plt.legend(loc='upper right')

plt.show()
