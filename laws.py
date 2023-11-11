import numpy as np
import random

def life(matrix) :
    matrix_new = matrix.copy()
    a, b = matrix.shape
    for i in range(a-2) :
        for j in range(b-2) :
            if matrix[i, j] == 1:
                if np.sum(matrix[i-2:i+3, j-2:j+3]) -1 < 2 :
                    matrix_new[i, j] = 0
                if np.sum(matrix[i-2:i+3, j-2:j+3]) -1 == 2 :
                    matrix_new[i, j] = 1
                if np.sum(matrix[i-2:i+3, j-2:j+3]) -1 > 3 :
                    matrix_new[i, j] = 0
            elif matrix_new[i, j] == 0:
                if np.sum(matrix[i-2:i+3, j-2:j+3]) == 3 :
                    matrix_new[i, j] = 1
    return matrix_new