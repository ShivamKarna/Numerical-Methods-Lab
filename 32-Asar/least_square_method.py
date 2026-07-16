import numpy as np
import matplotlib.pyplot as plt

X = np.array(list(map(float, input("Enter all X values using space : ").split(" "))))
Y = np.array(list(map(float, input("Enter all Y values using space : ").split(" "))))
if len(X) != len(Y):
    print("Number of x-data and y-data must be equal!")
    exit(0)
n = len(X)
print("Data points are : ")
print("X :", end="\t")
for i in range(n):
    print(X[i], end="\t")
print("\n")
print("Y :", end="\t")
for i in range(n):
    print(Y[i], end="\t")
print("\n\n")
A = [
    [n, np.sum(X), np.sum(X**2)],
    [np.sum(X), np.sum(X**2), np.sum(X**3)],
    [np.sum(X**2), np.sum(X**3), np.sum(X**4)],
]
A = np.array(A)
B = [[np.sum(Y)], [np.sum(X * Y)], [np.sum(X**2 * Y)]]
B = np.array(B)

coeffs = np.linalg.solve(A, B)
a, b, c = coeffs[0, 0], coeffs[1, 0], coeffs[2, 0]

print(f"Curve of best fit : \n y ={a:.4f} + {b:.4}x + {c:.4f}x**2")

x = np.linspace(min(X) - 5, max(X) + 5, 1000)
y = a + b * x + c * x**2

plt.plot(x, y, label="Curve of best fit")
plt.scatter(X, Y, label="Data Points")
plt.grid(True)
plt.legend()
plt.axhline(0, color="r")
plt.axvline(0, color="r")
plt.show()
