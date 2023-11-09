# generate square numbers of given list
l = [1, 2, 3, 4]

def squares(list_):
    for item in list_:
        yield item ** 2

res = squares(l)
# print(list(res))

# list comprehension
sq_ = [item ** 2 for item in l]
# print(sq_)

# generator expression
square = (item ** 2 for item in l)
# print(list(square))

##############################################################################
# generate only the strings with odd length in the given list

names = ["bob", "steve", "alex", "maya", "john"]

def odd_length(list_):
    for item in list_:
        if len(item) % 2:
            yield item

x = odd_length(names)
# print(list(x))

# generator expression
odd_ = (item for item in names if len(item) % 2)
# print(list(odd_))

#############################################################################
# generate a tuple of only numeric values in the given list

items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]

def num_(iterable):
    for item in iterable:
        if isinstance(item, (int, float, complex)):
            yield item

a = num_(items)
# print(tuple(a))

# generator expression

num = tuple(item for item in items if isinstance(item, (int, float, complex)))
# print(num)

##############################################################################
# generate a list -> if individual datatype, reverse it else keep it as it is
items = ["flipkart", 2021, "gmail", 1.2, [1, 2, 3], 2+3j, True]

def gen_list(list_):
    for item in list_:
        if isinstance(item, (int, float, complex)):
            yield str(item)[::-1]
        else:
            yield item

d = gen_list(items)
print(list(d))

# generator expression
g = (str(item)[::-1] if isinstance(item, (int, float, complex)) else item
     for item in items)

# print(list(g))

##########################################################################################
# Generating List of PI values with increasing decimal point numbers up to user defined number

import math
PI = math.pi
print(PI)

def pi_gen(num_of_decimals):
    for i in range(num_of_decimals):
        yield round(PI, i)

# print(list(pi_gen(4)))















































