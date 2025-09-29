import numpy as np

# A = np.array([[8, 6, 11], [7, 5, 9],[6, 10, 6]])
# A_inv = np.linalg.inv(A)
# print(np.round(A_inv, 1))

v1 = np.array([9, 10, 7, 7, 9])
v2 = np.array([2, 0, 5, 1, 4])
v3 = np.array([4, 0, 0, 4, 1])
v4 = np.array([3, -4, 3, -1, -4])

A_main = np.array([v1, v2, v3, v4]).T
print(A_main, '\n')

rk_main = np.linalg.matrix_rank(A_main)
print(rk_main,'\n')

Gram_main = np.dot(A_main.T, A_main)
print(Gram_main, '\n')

Gram_opred = np.linalg.det(Gram_main)
print(int(Gram_opred), '\n')

Gram_inv = np.linalg.inv(Gram_main)
print(np.round(Gram_inv, 3))