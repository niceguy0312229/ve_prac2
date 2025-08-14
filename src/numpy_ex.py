import numpy as np

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