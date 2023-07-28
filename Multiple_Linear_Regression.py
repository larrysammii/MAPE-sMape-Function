# Explaination of the below pending
# Least squares estimation(Ordinary Least Squares Estimation), estimate model's coefficent
import numpy as np
from numpy.linalg import inv

x = np.array([[1, 2, 5], [1, 3, 5], [1, 4, 7]])
y = np.array([1, 1, 3])

# self.transpose()
x_transp = x.T

# Matrix product of two arrays.
x_transp_mult = np.matmul(x_transp, x)

# Inverse Matrix
x_transp_mult_inv = np.linalg.inv(x_transp_mult)

left_part = np.matmul(x_transp, y)

w = np.matmul(x_transp_mult_inv, left_part)

print(w.round(0))