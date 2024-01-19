"""
Forcing datatypes with decorators.

Creating a decorator to forcing.

Remembering zip():

a = (1, 3, 5)
b = (2, 4, 6)

c = zip(a, b)

(1, 2), (3, 4), (5, 6)

"""


# Example_1 -------------------------------------------

def force_type(*types):
    def decorator(function):
        def converse(*args, **kwargs):  # Args are immutable. Need create a new_args.
            new_args = []
            for (value, type_1) in zip(args, types):
                new_args.append(type_1(value))
            return function(*new_args, **kwargs)

        return converse

    return decorator


@force_type(str, int)  # Here I inform the type specific.
def repeat_msg(msg, qt):
    for q in range(qt):
        print(msg)


repeat_msg('Hello World.', 3)  # Repeat 3x.


# Example_2 -------------------------------------------

@force_type(float, float)
def division(a, b):
    print(a / b)


division('1', 5)
