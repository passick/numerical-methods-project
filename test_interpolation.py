from interpolation import interpolate
from tabulate import tabulate, generate_uniform_grid
from math import *

import numpy as np

import matplotlib.pyplot as plt
import matplotlib

def test():
    left, right = -1, 1

    f1 = lambda t : sin(exp(2*t))
    # f1 = lambda t : exp(-5*(t-0.5)**2) - exp(-10*(t+0.1)**2) + exp(-t**2)
    f2 = lambda t : sin(1.0/(t**3)) if t != 0 else 0
    f3 = lambda t : (1 if t > 0 else -1) * exp(t**2)

    main_grid = generate_uniform_grid(left, right, 10000)
    small_grid = generate_uniform_grid(left, right, 10)
    large_grid = generate_uniform_grid(left, right, 100)
    # larger_grid = generate_uniform_grid(left, right, 1000)

    plt.rc('text', usetex=True)
    for (f, f_name, filename) in [(f1, r'$\sin(e^{2t})$', 'spline_plot1'),
            (f2, r'$\sin(t^{-3})$', 'spline_plot2'),
            (f3, r'$sign(t) e^{t^2}$', 'spline_plot3')]:
        main_f = tabulate(f, main_grid)
        small_f = tabulate(interpolate(tabulate(f, small_grid)), main_grid)
        large_f = tabulate(interpolate(tabulate(f, large_grid)), main_grid)
        # larger_f = tabulate(interpolate(tabulate(f, larger_grid)), main_grid)

        plt.title(f_name)
        plt.plot(main_grid, main_f.values)
        plt.plot(main_grid, small_f.values)
        plt.plot(main_grid, large_f.values, 'k')
        # plt.plot(main_grid, larger_f.values, 'm', label='sign(t)')
        # plt.legend()
        plt.savefig('img/' + filename + '.eps', bbox_inches='tight', dpi=300)
        plt.clf()

        plt.title(f_name)
        plt.plot(main_grid, np.array(main_f.values) - np.array(large_f.values))
        plt.savefig('img/' + filename + '_error.eps', bbox_inches='tight', dpi=300)
        plt.clf()
        # plt.show()


test()
