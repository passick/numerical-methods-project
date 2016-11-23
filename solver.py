import math
from tabulate import generate_uniform_grid, tabulate
from diffeq import solve_cauchy
from serializer import save_tabulated_function_to_file,\
        read_tabulated_function_from_file,\
        save_interpolation_to_file, read_interpolation_from_file
from integrate import integrate_tabulated
from interpolation import interpolate

def get_S_function(parameters):
    return lambda t: parameters['S_c'] * t + math.exp(parameters['S_d'] * t) - 1


def get_z_function(parameters):
    return lambda t: parameters['z_e'] * (t + t ** 2) + \
            math.exp(parameters['z_f'] * t) - 1


def get_rho_function(parameters):
    return lambda w: parameters['rho_a'] * w * (parameters['rho_b']  - w)


def test1(rho_function, z_function, S_function, T):
    tabulated_rho = tabulate(rho_function, generate_uniform_grid(0, 1, 21))
    tabulated_z = tabulate(z_function, generate_uniform_grid(0, T, 21))
    tabulated_S = tabulate(S_function, generate_uniform_grid(0, T, 21))

    save_tabulated_function_to_file(tabulated_rho, 'txts/tabulated_rho.txt')
    save_tabulated_function_to_file(tabulated_z, 'txts/tabulated_z.txt')
    save_tabulated_function_to_file(tabulated_S, 'txts/tabulated_S.txt')


def test2():
    tabulated_rho = read_tabulated_function_from_file('txts/tabulated_rho.txt')
    tabulated_integral = integrate_tabulated(interpolate(tabulated_rho), 0, 1, 1000)
    integral_interpolation = interpolate(tabulated_integral)
    save_interpolation_to_file(integral_interpolation, 'txts/U_interpolation.txt')


def test3(x_0, y_0, beta, T):
    tabulated_z = read_tabulated_function_from_file('txts/tabulated_z.txt')
    tabulated_S = read_tabulated_function_from_file('txts/tabulated_S.txt')
    U = lambda t : 1.0
    f = lambda z, x, S, beta : beta * (x - z)
    
    cauchy_solution = solve_cauchy(x_0, y_0, beta, f, T, U, tabulated_S, tabulated_z)


def solve(**parameters):
    rho_function = get_rho_function(parameters)
    S_function = get_S_function(parameters)
    z_function = get_z_function(parameters)
    beta = parameters['beta']
    T = parameters['T']
    x_0 = parameters['x_0']
    y_0 = parameters['y_0']
    test1(rho_function, z_function, S_function, T)
    test2()
    test3(x_0, y_0, beta, T)

