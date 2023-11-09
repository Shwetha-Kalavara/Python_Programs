###########################################
#printing n times
# import sys
# sys.setrecursionlimit(10)
# print(sys.getrecursionlimit())

def print_(count):

    if count == 0:
        return
    else:
        print("something")
        count -= 1
    print_(count)


# print_(3)
#############################################
#count numbers 1-10

def con_():
    for i in range(1,11):
        print(i)

#con_()

#counting numbers from 1 - userinput

def conn_(n):
    for i in range(1, n + 1):
        print(i)


# user_ = int(input("enter the value: "))
#conn_(user_)

#using recursion

def rec_con(n):
    if n >= 1:
        #print(n)
        rec_con(n-1)
        print(n)
        # return
    # else :
        # print(n)
        # rec_con(n+1)
        #return


# user_ = int(input("enter the value: "))
# rec_con(user_)

#############################################
#reversing a string

def rev_():
    s = "hello"
    i = ""
    for item in s:
        i = item + i
    print(i, end=" ")

#rev_()

#using recursion
x = "hello"
def rec_rev(s):
    if len(s) ==0 :
        return s
    else:
        return rec_rev(s[1:]) + s[0]

# print(rec_rev(x))

################################################
#factorial

def fact_(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        #print(fact)
    print(fact)


#fact_(5)

#using while

n = 5
i = 1
fact = 1
while i <= n:
    fact = fact * i
    i += 1

# print(fact)



def fact_(n, i=1, fact=1):
    if i <= n:
        fact = fact * i
        i += 1
        return fact_(n, i, fact)
    else:
        return fact

# print(fact_(5))

#using recursion

def rec_fact_(n, i = 1):
    if n > 1:
        i *= n
        n = n - 1
        return rec_fact_(i,n)

# print(rec_fact_(3))


# string reversal

i = 0
s = "hello"
res = ""

while i < len(s):
    res = s[i] + res
    i += 1

print(res)


def string_reversal(string, i=0, res=""):
    if i < len(string):
        res = s[i] + res
        return string_reversal(string, i+1, res)
    return res

    # if not (i < len(string)):
    #     return res
    #
    # res = s[i] + res
    # return string_reversal(string, i+1, res)


#print(string_reversal("hello"))

################################################
#fibonacci series
def recursive_fibonacci(n):
    if n <= 1:
        return n
    else:
        return (recursive_fibonacci(n - 1) + recursive_fibonacci(n - 2))


n_terms = int(input("enter the range of fibonacci series: "))

# check if the number of terms is valid
if n_terms < 0:
    print("Invalid input ! Please input a positive value")
else:
    print("Fibonacci series:")
    for i in range(n_terms):
        print(recursive_fibonacci(i))



##################################################







