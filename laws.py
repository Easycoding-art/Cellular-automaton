import numpy as np

def random_matrix(matrix) :
    a, b = matrix.shape
    return np.random.randint (0, 25, (a, b))

def bactery(matrix) :
    a, b = matrix.shape
    for i in range(a) :
            for j in range(b) :
                if i > 2 and i < a - 2 and j > 2 and j < b - 2 :
                    if matrix[i,j] == 0 :
                        if (matrix[i+1, j+1] == 1 or matrix[i+2, j+2] == 1 or 
                            matrix[i-1, j-1] == 1 or matrix[i-2, j-2] == 1 or 
                            matrix[i+1, j-1] == 1 or matrix[i+2, j-2] == 1 or
                            matrix[i-1, j+1] == 1 or matrix[i-2, j+2] == 1 or 
                            matrix[i-1, j] == 1 or matrix[i-2, j] == 1 or 
                            matrix[i, j-1] == 1 or matrix[i, j-2] == 1 or
                            matrix[i+1, j] == 1 or matrix[i+2, j] == 1 or 
                            matrix[i, j+1] == 1 or matrix[i, j+2] == 1 or
                            matrix[i-2, j+1] == 1 or matrix[i+2, j+1] == 1 or
                            matrix[i-1, j+2] == 1 or matrix[i+1, j+2] == 1 or
                            matrix[i-2, j-1] == 1 or matrix[i+2, j-1] == 1 or
                            matrix[i-1, j-2] == 1 or matrix[i+1, j-2] == 1) :
                            matrix[i,j] = 1
                         
                    elif matrix[i,j] == 1 :
                        if (matrix[i+1, j+1] == 0 and matrix[i+2, j+2] == 0 and 
                            matrix[i-1, j-1] == 0 and matrix[i-2, j-2] == 0 and 
                            matrix[i+1, j-1] == 0 and matrix[i+2, j-2] == 0 and
                            matrix[i-1, j+1] == 0 and matrix[i-2, j+2] == 0 and 
                            matrix[i-1, j] == 0 and matrix[i-2, j] == 0 and 
                            matrix[i, j-1] == 0 and matrix[i, j-2] == 0 and
                            matrix[i+1, j] == 0 and matrix[i+2, j] == 0 and 
                            matrix[i, j+1] == 0 and matrix[i, j+2] == 0 and
                            matrix[i-2, j+1] == 0 and matrix[i+2, j+1] == 0 and
                            matrix[i-1, j+2] == 0 and matrix[i+1, j+2] == 0 and
                            matrix[i-2, j-1] == 0 and matrix[i+2, j-1] == 0 and
                            matrix[i-1, j-2] == 0 and matrix[i+1, j-2] == 0) :
                            matrix[i,j] = 0
                        elif (matrix[i+1, j+1] == 1 and matrix[i+2, j+2] == 1 and 
                            matrix[i-1, j-1] == 1 and matrix[i-2, j-2] == 1 and 
                            matrix[i+1, j-1] == 1 and matrix[i+2, j-2] == 1 and
                            matrix[i-1, j+1] == 1 and matrix[i-2, j+2] == 1 and 
                            matrix[i-1, j] == 1 and matrix[i-2, j] == 1 and 
                            matrix[i, j-1] == 1 and matrix[i, j-2] == 1 and
                            matrix[i+1, j] == 1 and matrix[i+2, j] == 1 and 
                            matrix[i, j+1] == 1 and matrix[i, j+2] == 1 and
                            matrix[i-2, j+1] == 1 and matrix[i+2, j+1] == 1 and
                            matrix[i-1, j+2] == 1 and matrix[i+1, j+2] == 1 and
                            matrix[i-2, j-1] == 1 and matrix[i+2, j-1] == 1 and
                            matrix[i-1, j-2] == 1 and matrix[i+1, j-2] == 1) :
                            matrix[i,j] = 0
    return matrix

def ray(matrix) :
    a, b = matrix.shape
    for i in range(a-2) :
            for j in range(b-3) :
                if matrix[i,j] == 1 :
                    if(matrix[i+2,j+2] == 0) :
                        matrix[i+2,j+2] = 1
                    if(matrix[i+2,j-2] == 0) :
                        matrix[i+2,j-2] = 1
                    if(matrix[i,j+3] == 0) :
                        matrix[i,j+3] = 1
    return matrix

def change(matrix) :
    a, b = matrix.shape
    for i in range(a - 1) :
        for j in range(b - 1) :
            matrix[i, j], matrix[i+1, j] = matrix[i+1, j], matrix[i, j]
            matrix[i, j], matrix[i, j+1] = matrix[i, j+1], matrix[i, j]
    return matrix