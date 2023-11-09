# making an object callable
class Sample:

    def display(self):
        print("in display")

    def __call__(self):
        print("calling object.....")


# obj = Sample()

# checks if any object is callable or not
# print(callable(obj))        # True

# __new__ -> creation of object
# __init__ -> initializing variable in object dictionary
# callables - functions, lambda functions, classes

#############################################################################
# Create a callable object to log a message “hello everyone”
class Log:
    def __call__(self):
        print("hello everyone")

l = Log()
# l()

#############################################################################
# Create a callable object to print “hello {name}” by passing name
# as an argument.

class Greet:

    def __call__(self, name):
        print(f"hello {name}")

g = Greet()
# g("Ram")

#############################################################################
# to log a message before any function

class LogDecorator:

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            print(f"executing {func.__name__} function")
            return func(*args, **kwargs)
        return wrapper


l = LogDecorator()
@l                  # add = l(add)
def add(a, b):
    return a + b

# print(add(1, 2))

##############################################################################
# parameterized class decorator
import time

class Delay:

    def __init__(self, n):
        self.n = n

    def __call__(self, func):
        def wrapper(*args, **kwargs):
            time.sleep(self.n)
            return func(*args, **kwargs)
        return wrapper


@Delay(5)
def add(a, b):
    return a + b

# print(add(1, 2))

#################################################################################
































