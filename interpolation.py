import numpy as np
from linsys import solve_linear_system
from bisect import bisect_left

class Interpolation:
    '''
    Object that stores interpolation parameters.
    '''
    def __init__(self, tabulated_function, interpolation_coefficients):
        self.coefficients = interpolation_coefficients
        self.function = tabulated_function

    def _evaluate_polynomial(x, x_left, poly):
        t = x - x_left
        return poly[0] + poly[1] * t + poly[2] * t**2 / 2 + poly[3] * t**3 / 6

    def __call__(self, x):
        position = bisect_left(self.function.grid, x) - 1
        if position < 0:
            return self.function[0]
        return Interpolation._evaluate_polynomial(x,
                self.function.grid[position],
                self.coefficients[position])


def interpolate(tabulated_function):
    '''
    Construct interpolation for given tabulated function.
    '''
    n = len(tabulated_function.grid) - 1
    grid = tabulated_function.grid
    matrix = np.zeros((n-1, n-1))
    values = np.zeros((n-1,))
    for i in range(1, n):
        h0 = grid[i] - grid[i-1]
        h1 = grid[i+1] - grid[i]

        df0 = tabulated_function[i] - tabulated_function[i-1]
        df1 = tabulated_function[i+1] - tabulated_function[i]

        matrix[i-1, i-1] = 2 * (h0 + h1)
        if i > 1:
            matrix[i-1, i-2] = h0
        if i+1 < n:
            matrix[i-1, i] = h1

        values[i-1] = 6 * (df1/h1 - df0/h0)
    zs = solve_linear_system(matrix, values)

    polynomials = []
    for i in range(n):
        f0 = tabulated_function[i]
        f1 = tabulated_function[i+1]
        h = grid[i+1] - grid[i]
        z0 = (zs[i-1] if i > 0 else 0)
        z1 = (zs[i] if i+1 < n else 0)
        polynomials.append([
            f0,
            (f1-f0)/h - z1*h/6 - z0*h/3,
            z0,
            (z1-z0)/h
            ])

    return Interpolation(tabulated_function, polynomials)
