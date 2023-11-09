# to return a list of even numbers

def evens(start, end):
    l = []
    for i in range(start, end+1):
        if i % 2 == 0:
            l.append(i)
    return l

# print(evens(1, 10))
# print(evens(11, 30))

####################################################################
# to return a dictionary with element and its count in any sequence

def count_element(sequence):
    d = {}
    for item in sequence:
        if item not in d:
            d[item] = 1
        else:
            d[item] += 1

    return d

# print(count_element("hello"))
# print(count_element([1, 2, 3, 4, 5, 6, ]))

# to return a list of first "n" prime numbers

def first_n_prime(n):
    l = []
    count = 0
    num = 0

    while count < n:
        if num > 1:
            for i in range(2, num):
                if num % i == 0:
                    break
            else:
                count += 1
                l.append(num)
        num += 1
    return l


# print(first_n_prime(5))
# print(first_n_prime(10))

#################################################################
# to check if the given number is prime or not


def is_prime(number):

    for i in range(2, number):
        if number % i == 0:
            print("Number is not prime")
            break

    else:
        print("Number is prime")

# is_prime(8)

#####################################################################
# function to return last digit of the given number

def last_digit(num):
    return int(str(num)[-1])    # return num % 10

res = last_digit(1234)
# print(res)

######################################################################
# return last n elements from the sequence as the list

def tail(sequence, n):
    return list(sequence[-n:])

# print(tail("hello", 3))

########################################################################
# return a list of words starting with vowels

string = "It is very sunny today"

def vowels_list(iterable):
    l = []
    for i in iterable:
        if i[0].lower() in "aeiou":
            l.append(i)

    return l

list_ = string.split()
print(vowels_list(list_))
















































