#!/usr/bin/python3
matrix_mul = __import__('100-matrix_mul').matrix_mul

print(matrix_mul([[1, 2], [3, 4]], [[1, 2], [3, 4]]))
print(matrix_mul([[5]], [[2]]))
print(matrix_mul([[1.0, 2, 3.5], [4, 5.5, 6]], [[7, 8.2], [9, 10], [11.1, 12]]))
print(matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]]))
print(matrix_mul([[1, 2], [3, 4]], [[5, 6, 7], [8, 9, 10]]))
print(matrix_mul([[1, 2, 3], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))
print(matrix_mul([['a', 'b'], ['c', 'd']], [['e', 'f'], ['g', 'h']]))
print(matrix_mul([[0]], [[34]]))
print(matrix_mul([[1, 2, 'a'], [4, 5, 6]], [[7, 8], [9, 10], [11, 12]]))
print(matrix_mul([[1, 2, 3], [4, 5, 6], [7, 8]], [[9, 10], [11, 12]]))
print(matrix_mul([[]], [[]]))
