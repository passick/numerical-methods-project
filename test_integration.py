from integrate import integrate_tabulated
from math import *

import matplotlib.pyplot as plt
import matplotlib
import numpy

def get_integrals(f, left, right, ns):
    return numpy.array([integrate_tabulated(f, left, right, n).values[-1] for n in ns])

def test():
    left, right = -1, 1

    f1 = lambda t : sin(exp(2*t))
    # f1 = lambda t : exp(-5*(t-0.5)**2) - exp(-10*(t+0.1)**2) + exp(-t**2)
    f2 = lambda t : sin(1.0/(t**3)) if t != 0 else 0
    # f3 = lambda t : 1 if t > 0 else -1
    f3 = lambda t : (1 if t > 0 else -1) * exp(t**2)

    f1_value = 0.68091029684056252
    f2_value = 0
    f3_value = 0

    ns = numpy.arange(10, 3001, 10)

    errors1 = numpy.log2(numpy.abs(get_integrals(f1, left, right, ns) - f1_value) + 2**-100)
    errors2 = numpy.log2(numpy.abs(get_integrals(f2, left, right, ns) - f2_value) + 2**-100)
    errors3 = numpy.log2(numpy.abs(get_integrals(f3, left, right, ns) - f3_value) + 2**-100)
    # print(errors1[0])

    plt.rc('text', usetex=True)
    plt.xlabel('$\log n$')
    plt.ylabel('$\log E$')
    plt.plot(numpy.log2(ns), errors1, label=r'$\sin(e^{2t})$')
    plt.plot(numpy.log2(ns), errors2, label=r'$\sin(t^{-3})$')
    plt.plot(numpy.log2(ns), errors3, 'k', label=r'$sign(t) e^{t^2}$')
    plt.legend(loc=4)
    plt.savefig('img/integration_error_plot.eps', bbox_inches='tight', dpi=500)
    plt.clf()
    # plt.show()

test()
