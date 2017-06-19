#!/bin/env python3
# REF: https://www.datacamp.com/community/blog/python-scipy-cheat-sheet
# Matrix Algebra


import numpy as np


A =  np.array([(1, 2, 3), (2, 7, 4)])
print('A = ' + repr(A))

B = np.array([(1, -1), (0, 1)])
print('B = ' + repr(B))

C = np.array([(5, -1), (9, 1), (6,0)])
print('C = ' + repr(C))

D = np.array([(3, -2, -1), (1, 2, 3)])
print('D = ' + repr(D))

u = np.array([(6, 2, -3, 5)])
print('u = ' + repr(u))

v = np.array([(3, 5, -1, 4)])
print('v = ' + repr(v))

w = np.array([[1], [8], [0], [5]])
print('w = ' + repr(w))

print('C.T = ' + repr(C.T))

print('A.T = ' + repr(A.T))

print('D.T = ' + repr(D.T))

def get_dim( A ):
    num_rows =  len(A)
    num_cols =  len(A[0])
    return ( num_rows, num_cols )

print('Matrix Dimensions:')
print('A dimensions are: ' + repr(get_dim(A)))
print('B dimensions are: ' + repr(get_dim(B)))
print('C dimensions are: ' + repr(get_dim(C)))
print('D dimensions are: ' + repr(get_dim(D)))
print('u dimensions are: ' + repr(get_dim(u)))
print('w dimensions are: ' + repr(get_dim(w)))

print('Vector Operations:')
print('u + v: ' + repr(u + v))
print('u - v: ' + repr(u - v))
print('alpha u: ' + repr( 6 * u))
print('u dot v: ' + repr(np.dot(u[0], v[0])))
print('||u||: ' + repr(np.linalg.norm(u)))

print('Matrix Operations:')
try:
    ans = A + C
except ValueError:
    ans = 'not defined'
print('A + C: ' + ans)
print('A - C.T: ' + repr(A - C.T))
print('C.T + 3D: ' + repr(C.T + 3*D))
print('BA: ' + repr(B @ A))
try:
    ans = B @ A.T
except ValueError:
    ans = 'not defined'
print('BA.T: ' + ans)

print('Optional:')
try:
    ans = B @ C
except ValueError:
    ans = 'not defined'
print('BC: ' + ans)

try:
    ans = C @ B
except ValueError:
    ans = 'not defined'
print('CB: ' + repr(ans))

B = np.matrix('1 -1 ; 0 1')
print('B**4: ' + repr(B ** 4))
print('B @ B @ B @ B: ' + repr(B @ B @ B @ B))
print('A @ A.T: ' + repr(A @ A.T))
print('D.T @ D: ' + repr(D.T @ D))

