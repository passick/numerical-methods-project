from tabulate import tabulate, generate_uniform_grid, \
        TabulatedFunction

def integrate(f, left, right):
    '''
    Compute integral of f on segment from left to right.
    '''
    return 1


def integrate_tabulated(f, left, right, n_nodes):
    '''
    Compute tabulated integral of f for uniform grid with n_nodes nodes.
    '''
    grid = generate_uniform_grid(left, right, n_nodes)
    values = [0.0]
    for i in range(1, len(grid)):
        a = grid[i-1]
        b = grid[i]
        value = (f(a) + 4 * f((a+b)/2) + f(b)) * (b - a) / 6
        values.append(value + values[-1])
    return TabulatedFunction(grid=grid, values=values)
