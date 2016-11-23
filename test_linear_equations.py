from linsys import solve_linear_system
import numpy as np
import scipy.linalg

def info(matrix_name, matrix, y):
    solution = solve_linear_system(matrix, y)
    print(matrix_name + " condition number: ", np.linalg.cond(matrix, p=np.inf))
    print("Solution for {}: ".format(matrix_name), solution)
    print("Residue for {}: ".format(matrix_name),
            np.linalg.norm(np.dot(matrix, solution) - y))
    print("{} ∞-norm: {:.20f}".format(matrix_name, np.linalg.norm(matrix, ord=np.inf)))
    print("det({}) = {:.20f}".format(matrix_name, np.linalg.det(matrix)))
    print()

def test():
    A = np.matrix(
            [[1,      2,     3],
             [2.0001, 3.999, 6],
             [15,     3,     6]]
            )
    B = scipy.linalg.hilbert(8)
    C = np.matrix(
            [[1e6,  2],
             [1e13, 2]]
            )
    b1 = np.array([1, 5, 25])
    b2 = np.arange(0, 8) + 1
    b3 = np.array([1, 5])

    info('A', A, b1)
    info('B', B, b2)
    info('C', C, b3)

test()
