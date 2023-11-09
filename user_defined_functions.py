def length_of_iterable(iterable):
    count = 0
    for _ in iterable:
        count += 1
    return count


# length = length_of_iterable("hello")
# print(length)

####################################################################
def display(name, age):
    print(f"My name is {name}, I am {age} years old")
    
# positional arguments
display("John", 30)
display(30, "john")

# keyword arguments
display(age=30, name="John")

# combination of positional and keyword arguments
display("John", age=30)

###############################################################
# positional only arguments
def add(a, b, c, /):
    print(a + b + c)

# add(1, 2, 3)          # 6
# add(a=1, b=2, c=3)    # TypeError
# add(1, b=2, c=3)      # TypeError

def add(a, b, c, /, d):
    print(a + b + c + d)

add(1, 2, 3, 4)
add(1, 2, 3, d=4)

####################################################################
# keyword only arguments

def add(*, a, b, c):
    print(a + b + c)
    
# add(1, 2, 3)          # TypeError
# add(a=1, b=2, c=3)    # 6
# add(1, b=2, c=3)      # TypeError

def add(a, *, b, c):
    print(a + b + c)

add(1, b=2, c=3)        # 6        
add(a=1, b=2, c=3)      # 6

##############################################################
# combination of keyword only and positional only parameters
def add(a, b, /, *, c, d):
    print(a + b + c + d)

add(1, 2, c=3, d=4)

#############################################################
# default parameter

def add(a, b, c, d=0):
    print(a + b + c + d)

add(1, 2, 3)        # 6
add(1, 2, 3, 4)     # 10

# default values cannot be initialized twice.
a = 7
def spam(x=a):
    print(x)

a = 10
spam()

##################################################################
# *args and **kwargs

# variable positional arguments
def add(*args):
    print(args)
    print(sum(args))

add(1, 2, 3, 4, 5, 6, 7, 8)
add()

# variable keyword arguments
def display(**kwargs):
    print(kwargs)

display(a=1, b=2, c=3)

# combination of variable positional and keyword arguments
def display(*args, **kwargs):
    print(args, kwargs)

display(1, b=2, c=3)

#################################################################
# function annotations

def add(a: int, b: int) -> int:
    print(a + b)

add("hai", "hello")
add(1, 2)

#########################################################################
""" Activity """

# count the number of positional and keyword arguments passed.

def display(*args, **kwargs):
    print("Positional arguments:", len(args))
    print("Keyword arguments:", len(kwargs))

# display(1, 2, 3, a=10, b=20)

###################################################################
# Write a function to print message “Hai Everyone” if the user input is not present and
# if the user input is present print the user input.

def greet(msg="hai everyone"):
    print(msg)

# greet("hello")

####################################################################
# A function takes variable number of positional arguments as input.
# How to check if the arguments that are passed are more than 5

def check_pos(*args):
    if len(args) > 5:
        print("there are more than 5 positional arguments")
    else:
        print("there are less than 5 positional arguments")

# check_pos(1, 2, 3, 4, 5, 6, 6)



















































