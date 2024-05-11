import numpy as np


a = np.array([1, 2, 3, 4, 5, -5, -4])
b = np.array([1, 2, 3, 4, 5, -5.000001, -4.000010])

print(np.equal(a, b))
print(np.allclose(a, b))
