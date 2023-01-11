from functools import wraps
def only_int_allow(function):
    @wraps(function)
    def wrapper(*args,**kwargs):
        datatypes = []
        for arg in args:
            datatypes.append(type(arg)==int)
            

        if all(datatypes):
            return function(*args, **kwargs)
        else:
            print("invalid arguments")
    return wrapper

@only_int_allow
def add_all(*args):
    total =0 
    for i in args:
        total+=i
    return total

print(add_all(1,2,3,4,5,6))