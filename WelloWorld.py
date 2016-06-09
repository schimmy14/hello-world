# This is a practice code for github

import numpy as np


A = np.arange(1,7).reshape(2,3)

print A
B = np.arange(1,7).reshape(3,2)
print B

print np.dot(A,B)
print np.dot(B,A)