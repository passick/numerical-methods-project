from tabulate import TabulatedFunction
from differentiate import differentiate

def solve_cauchy(x_0, y_0, beta, f, T, U, S, z):
    '''
    Solve Cauchy problem for functions x and y.
    x(t_0) = x_0
    y(t_0) = y_0
    x'(t) = z'(t) * U(y)
    y'(t) = f(z, x, S, beta)
    '''

    x_current, y_current = x_0, y_0
    computed_xs, computed_ys = [x_0], [y_0]

    for i in range(len(S.grid) - 1):
        current_t = S.grid[i]
        next_t = S.grid[i+1]

        x_current += differentiate(z, current_t) * U(y_current) * (next_t - current_t)
        y_current += f(z[i], x_current, S[i], beta) * (next_t - current_t)

        computed_xs.append(x_current)
        computed_ys.append(y_current)

    return (TabulatedFunction(grid=S.grid, values=computed_xs),
            TabulatedFunction(grid=S.grid, values=computed_ys))
