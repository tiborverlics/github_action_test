import numbers


def square_number(inp: float) -> float:

    if not isinstance(inp, numbers.Number):
        raise TypeError('Type error - Input should be numerical')

    return inp * inp
