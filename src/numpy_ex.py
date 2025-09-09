import numpy as np


list_len = [1, 2, 3, 4]
print(f"To check the size of the list, use len() : {len(list_len)}") 
#print(list_len.shape)

matrix1 = np.array([[1, 2],
                   [3, 4]])

print(matrix1.shape)  # (2, 2) → (rows, columns)
print(matrix1.size)   # 4     → total elements
print(matrix1[0][1])  # Outputs 2 (row 1, column 2 in MATLAB)
print(matrix1[1][0])  # Outputs 3 (row 2, column 1 in MATLAB)
print(len(matrix1))   # Only shows the number of low

matrix2 = np.array([[1, 2, 3 ], 
                    [4, 5, 6 ]])
print(matrix2.shape)

# MATLAB vs. NumPy Default Ordering
# MATLAB uses column-major order (Fortran order) by default. This means when you use reshape in MATLAB, it reads and fills the matrix column-wise.
# NumPy (Python) uses row-major order (C order) by default. This means reshape reads and fills the matrix row-wise.

reshaped_matrix = matrix2.reshape(1, -1)
reshaped_matrix_matlablike = matrix2.reshape(1, -1, order ='F')  # order = 'F' fortran like has be to written 
print(reshaped_matrix)
#print(reshaped_matrix.shape)
print(reshaped_matrix_matlablike)
#print(reshaped_matrix_matlablike.shape)

a = np.array([1, 2, 3])
b = np.array([8, 9, 10])

#Option 1: Stack as columns (each array is a column)
matrix = np.column_stack((a, b))

print(matrix)
print(matrix.shape)

#Option 2: Stack as rows
matrix = np.vstack((a, b))

print(matrix)
print(matrix.shape)

#Option 3: Concatenate and reshape
combined = np.concatenate((a, b))
matrix = combined.reshape(3, 2)

print(matrix)

# 1 - dimensional matrix
np.array([1, 2 ])
# 2 - dimensional matrix
np.array([[1, 2 ]])




# matrix mutliplication 
A = np.array([ [1,2],[3,4] ])
B = np.array([ [1,0],[1,1] ])

C = A * B                   # element x element 
C_matrix  = np.dot(A,B)     # matrix calculation
print(C)                
print(C_matrix)

