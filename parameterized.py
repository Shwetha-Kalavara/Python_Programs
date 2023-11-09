import time

# delay decorator
def parameter_delay(time_):
    def delay(func):
        def wrapper(*args, **kwargs):
            time.sleep(time_)
            return func(*args, **kwargs)
        return wrapper
    return delay


@parameter_delay(5)     # @delay     # display = delay(display)
def display():
    print("something")

# display()

@parameter_delay(3)
def spam(string):
    return string[::-1]

# print(spam("python"))

##########################################################################
# calling a function "n" times

def n_parameter(n):
    def n_times(func):
        def wrapper(*args, **kwargs):
            for i in range(n):
                func(*args, **kwargs)
        return wrapper
    return n_times

@n_parameter(5)
def display():
    print("in display")
# display()























