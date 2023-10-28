import numpy as np

ar = np.array([1,22,3,5,4,6,8,])

max = ar.argsort()[-3:][::-1]

print(ar[1])