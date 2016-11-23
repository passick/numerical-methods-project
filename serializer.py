from tabulate import TabulatedFunction
from interpolation import Interpolation

def save_interpolation_to_file(interpolation, filename):
    '''
    Write interpolation parameters to file.
    '''
    with open(filename, 'w') as fout:
        function = interpolation.function
        print(serialize_tabulated_function(function), end='', file=fout)
        print('-----', file=fout)
        print('\n'.join(map(lambda coefs : ' '.join(map(str, coefs)),
            interpolation.coefficients)),
            file=fout)


def read_interpolation_from_file(interpolation, filename):
    '''
    Read interpolation coefficients from file.
    '''
    with open(filename, 'r') as fin:
        lines = fin.readlines()
        split = lines.index('-----\n')

        function = deserialize_tabulated_function(lines[:split])
        coefficients = map(lambda line : list(map(float, line.split())), lines[split+1:])

        return Interpolation(tabulated_function=function,
                interpolation_coefficients=coefficients)
        

def save_tabulated_function_to_file(function, filename):
    '''
    Write tabulated function to file.
    '''
    with open(filename, 'w') as fout:
        print(serialize_tabulated_function(function), end='', file=fout)


def serialize_tabulated_function(function):
    '''
    Serialize tabulated function into a string.
    '''
    result = ''
    for (argument, value) in zip(function.grid, function.values):
        result += '{} {}\n'.format(argument, value)
    return result


def read_tabulated_function_from_file(filename):
    '''
    Read tabulated function from file.
    '''
    with open(filename, 'r') as fin:
        return deserialize_tabulated_function(fin.readlines())


def deserialize_tabulated_function(string):
    '''
    Get tabulated function out of its serialization in string.
    String may be a list of strings.
    '''
    if type(string) is str:
        lines = string.split('\n')[:-1]
    else:
        lines = string

    grid, values = [], []
    for line in lines:
        splitted = line.split()
        grid.append(float(splitted[0]))
        values.append(float(splitted[1]))

    return TabulatedFunction(grid=grid, values=values)
