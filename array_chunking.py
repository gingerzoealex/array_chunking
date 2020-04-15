import numpy as np
from math import floor


def section_array(array, integer_n):
    if not isinstance(integer_n, int):
        raise TypeError(
            'integer_n should be an integer, not a string')
    try:
        if (len(array) % integer_n) == 0:
            return np.array_split(array, (len(array) / integer_n))
        else:
            return np.array_split(array, floor(len(array) % integer_n))
    except ZeroDivisionError as error:
        print('Division by 0 error: {}'.format(error))
    except Exception as exception:
        print('Exception caught: {}'.format(exception))
