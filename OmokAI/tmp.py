import numpy as np

a = np.zeros((2,3))
a2 = a.reshape(1,2,3,1)

print(a2)