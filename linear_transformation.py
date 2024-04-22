#Importing numpy
import numpy as np
#Importing pyplot from matplotlib library
import matplotlib.pyplot as plt

#Asking User for linear transformation factors
a = float(input("Enter the x-direction scaling factor : "))
b = float(input("Enter the y-direction scaling factor : "))

#Extracts and construct a diagonal array
C = np.diag([a, b])
n = int(3)
# Lines below reads inputs from user using map() function
list1 = list(map(int, 
	input("\nEnter the numbers of x-axis of the vector, 3 numbers seperate by space : ").strip().split()))[:n]
list2 = list(map(int, 
	input("\nEnter the numbers of y-axis of the vector, 3 numbers seperate by space : ").strip().split()))[:n]
#Aplly points (X)
X = np.array([(list1), (list2)])

#Apply the scaling transformation
CX = np.matmul(C, X)

#Plot the original points and scaled points
plt.plot(X[0, :], X[1, :], '.-', alpha=0.2, label="Original points")
plt.plot(CX[0, :], CX[1, :], '.-', label="Scaled points")
plt.axis("equal")
plt.grid(True)
plt.legend()
plt.show()