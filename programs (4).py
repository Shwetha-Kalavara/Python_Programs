# log decorator

def log(func):
    def wrapper(*args, **kwargs):
        print(func.__name__)
        return func(*args, **kwargs)
    return wrapper


@log        # print_ = log(print_)      : func -> print_, print_ - wrapper
def print_():
    print("This is main function")

# print_()

# counting the number of arguments given to a function

def count_(func):
    def wrapper(*args, **kwargs):
        print(f'total number of arguments: {len(args) + len(kwargs)}')
        return func(*args, **kwargs)
    return wrapper

@count_
def display(a, b):
    print(a, b)

# display(1, b=2)

# to input 5 seconds of delay before executing a function
import time

def delay(func):
    def wrapper(*args, **kwargs):
        print("executing wrapper")
        time.sleep(5)
        return func(*args, **kwargs)
    return wrapper

@delay
def display():
    print("In display")

# display()
############################################################################
# to calculate execution time of the function

def execution_time(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        return f"execution time: {end-start}", f"output of display: {res}"
    return wrapper


@execution_time
def display():
    return "In display"
# print(display())

############################################################################
# to execute a function for 3 times

def _3_times(func):
    def wrapper(*args, **kwargs):
        for _ in range(3):
            res = func(*args, **kwargs)
            print(res)
    return wrapper


@_3_times
def add(a, b):
    return a + b

# add(1, 2)

##########################################################################
# count the number of function calls
count = 0
def no_of_func_calls(func):
    def wrapper(*args, **kwargs):
        global count
        count += 1
        res = func(*args, **kwargs)
        return f"function calls: {count}", f"{res}"
    return wrapper

@no_of_func_calls
def add(a, b):
    return a + b

# print(add(1, 2))
# print(add(3, 4))

@no_of_func_calls
def sub(a, b):
    return a - b

# print(sub(3, 1))

###########################################################################
# to create a dictionary of each function's function call

d = {}
def function_call(func):
    def wrapper(*args, **kwargs):
        if func.__name__ not in d:
            d[func.__name__] = 1
        else:
            d[func.__name__] += 1
        res = func(*args, **kwargs)
        return res
    return wrapper

@function_call
def add(a, b):
    return a + b

# print(add(1, 2))
# print(add(3, 4))


@function_call
def sub(a, b):
    return a - b

# print(sub(3, 1))
#
# print(d)

###########################################################################
# to return the output of any subtraction function as a positive value

def positive(func):
    def wrapper(*args, **kwargs):
        return abs(func(*args, **kwargs))
    return wrapper


@positive
def sub(a, b):
    return a - b

# print(sub(1, 2))





























































































