#lambda func that adds 15 to a given number
def _add(a):
    return a+15
print(_add(10))

# lambda expression
add = lambda a: a+15
print(add(10))

########################################################################
# lambda expression to check the given num is even or not
def even_(n):
    if n%2==0:
        return "even number"
print(even_(20))

# lambda expression
evn = lambda n:f"even number" if n%2==0 else f"odd number"
print(evn(20))

#####################################################################
# checks if the given string is palindrome or not
palin = lambda s: f"palindrome" if s==s[::-1] else f"not a palindrome"
print(palin("mam"))

####################################################################
# returns the last element of the sequence
last_element = lambda item: item[-1]
print(last_element("hello"))

#####################################################################
# to solve the expression a**2+b**2+2*a*b
exp = lambda a, b: a ** 2 + b ** 2 + 2 * a * b
print(exp(2, 4))

######################################################################
# print both squares as well as cubes of the number
s_c = lambda n: [n**2, n**3]
print(s_c(2))
