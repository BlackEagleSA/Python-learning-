import numpy as np 
from scipy import linalg

variables = np.array([[1,1], [4,9]])
eq = np.array([30,150])

sol = linalg.solve(variables, eq)

print(sol)

