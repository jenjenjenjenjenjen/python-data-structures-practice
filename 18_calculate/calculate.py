def calculate(operation, a, b, make_int=False, message='The result is'):
    """Perform operation on a + b, ()possibly truncating) & returning w/msg.

    - operation: 'add', 'subtract', 'multiply', or 'divide'
    - a and b: values to operate on
    - make_int: (optional, defaults to False) if True, truncates to integer
    - message: (optional) message to use (if not provided, use 'The result is')

    Performs math operation (truncating if make_int), then returns as
    "[message] [result]"

        >>> calculate('add', 2.5, 4)
        'The result is 6.5'

        >>> calculate('subtract', 4, 1.5, make_int=True)
        'The result is 2'

        >>> calculate('multiply', 1.5, 2)
        'The result is 3.0'

        >>> calculate('divide', 10, 4, message='I got')
        'I got 2.5'

    If a valid operation isn't provided, return None.

        >>> calculate('foo', 2, 3)
        
    """
    if operation == 'add':
        result = add(a,b)
        if make_int == True:
            return f"{message} {int(result)}"
        else:
            return f"{message} {result}"
    elif operation == 'subtract':
        result = subtract(a,b)
        if make_int == True:
            return f"{message} {int(result)}"
        else:
            return f"{message} {result}"
    elif operation == 'multiply':
        result = multiply(a,b)
        if make_int == True:
            return f"{message} {int(result)}"
        else:
            return f"{message} {result}"
    elif operation == 'divide':
        result = divide(a,b)
        if make_int == True:
            return f"{message} {int(result)}"
        else:
            return f"{message} {result}"
    else:
        return None

def add(a,b):
    return a+b
def subtract(a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    return a/b
