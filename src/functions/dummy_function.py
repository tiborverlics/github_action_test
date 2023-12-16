import numbers

def square(inp:float) -> float:

    if not isinstance(inp, numbers.Number):
        raise TypeError('Type error - Input should be numerical')

    return inp * inp
