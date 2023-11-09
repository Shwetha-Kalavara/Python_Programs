# def display(x):     # monkey patching add function's address with x
#     print("Executing display")
#     return x        # returning function address from a function
#
#
# def add(a, b):
#     print(a + b)


# add = display(add)      # passing function as argument
# add(1, 2)

#############################################################################

def display(x):
    def wrapper(*args, **kwargs):
        print("executing display")
        return x(*args, **kwargs)
    return wrapper      # add -> wrapper


@display    # add = display(add)
def add(a, b):
    return a + b

# add = display(add)        # x --> add
print(add(1, 2))



@ display   # sub = display(sub)
def sub(a, b, c):
    print(a - b - c)

sub(1, 2, 3)












