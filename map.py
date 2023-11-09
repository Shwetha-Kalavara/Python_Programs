# check if the given list of numbers are even and odd

l = [2, 3, 5, 6, 7, 8]
e_o = lambda num: "even number" if num % 2 == 0 else "odd number"
y = map(e_o, l)
print(list(y))

######################################################################
# convert -ve numbers to +ve numbers

l = [2, -3, -4, -5]
convert = lambda num: abs(num)
print(list(map(convert, l)))

print(list(map(abs, l)))

########################################################################
# find if a given string starts with a vowels

l = ['apple', 'orange', 'gmail', 'yahoo']
def vowels(string):
    if string[0].lower() in 'aeiou':
        return string
    else:
        return "not vowel"
print(list(map(vowels,l)))

#####################################################################
# square and cube every number in a given list of integer

l = [2, 3, 4, 5]
s_c = lambda i: [i**2, i**3]
print(list(map(s_c, l)))

#####################################################################
# return list of elements raised power of their indices

l = [2, 3, 4, 5]
l_ = []
for index, item in enumerate(l):
    res = item**index
    l_.append(res)
print(l_)

def power(num):
    for index, item in enumerate(num):
        res = item**index
        print(res)
power(l)

l = [2, 3, 4, 5]
def power(num):
    index, item = num
    return item ** index
print(list(map(power,enumerate(l))))

"""
deep unpacking
((a, b),) = ((1, 2),)
print(a)
print(b)
"""

l = [2, 3, 4, 5]
def power_index(element):
    index, item = element
    return item ** index

print(list(map(power_index, enumerate(l))) )    # (0, 2)

########################################################################
# l1 = [1,2,3,4] l2 = [5,6,7,8] add  the following list simultaneously
l1 = [1, 2, 3, 4]
l2 = [5, 6, 7, 8]

def sum_(x,y):
    return x + y
print(list(map(sum_, l1, l2)))

##########################################################################
# s = "hi good afternoon" print the list of length of each word

s = "hi good afternoon"
l = s.split()
print(list(map(len, l)))

#####################################################################
#s = "hi good afternoon" returns all the words in upper case

s = "hi good afternoon"
l = s.split()
def upper_(n):
    return n.upper()

print(list(map(str.upper,l)))



