# Explaination of the below pending

import numpy as np
from numpy.linalg import inv

x = np.array([[1, 2, 5], [1, 3, 5], [1, 4, 7]])
y = np.array([1, 1, 3])
x_transp = x.T
x_transp_mult = np.matmul(x_transp, x)
x_transp_mult_inv = np.linalg.inv(x_transp_mult)
left_part = np.matmul(x_transp, y)
w = np.matmul(x_transp_mult_inv, left_part)

print(w.round(0))