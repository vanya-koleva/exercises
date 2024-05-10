import numpy as np


a = np.array([1+1j, 1+0j, 4.5, 3, 2, 2j])
print(np.iscomplex(a))
print(np.isreal(a))
print(np.isscalar(a[4]))
print(np.isscalar([3.1]))
