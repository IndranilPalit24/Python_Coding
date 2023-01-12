from functools import wraps
def only_datatype_allowed(datatypes):
    def decorator(function):
        @wraps(function)
        def inside_datatype(*args):
            for arg in args:
                if all(type(arg)==datatypes for arg in args):
                    return function(*args)
            return f"Only {datatypes} argument are callable"

        return inside_datatype
    return decorator

@only_datatype_allowed(int)
def add(*args):
    total = 0
    for arg in args:
        total+=arg 

    return total

print(add(1,2,3,4,5,6, 'harshit'))