import numpy as np

a = np.matrix([(1/3), (2/3)])
b = np.matrix('0.25 0.75 ; 1 0')

print(a * b ** 3)