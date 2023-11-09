# check if the number is prime or not
num = 9

for i in range(2, num):
    if num % i == 0:
       print("number is not prime")
       break
else:
    print("number is prime ")

#################################################################
# prime number series
for num in range(10):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num, end=" ")

###############################################################
# print nth prime number
num = 0
count = 0
x = 5

while count < x:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            count += 1
            if count == x:
                print(num)
    num += 1

################################################################
# print first 10 fibonacci numbers
a = 0
b = 1

for _ in range(10):
    print(a, end=" ")
    c = a + b
    a = b
    b = c

###############################################################
# print nth fibonacci number
a = 0
b = 1
n = 5

for _ in range(n-1):
    a, b = b, a + b

print(f"The {n}th fibonacci number is: {a}")

################################################################
# to generate fibonacci series till the number 10
a = 0
b = 1

while a < 15:
    print(a, end=" ")
    a, b = b, a + b

####################################################################
# largest number in the given list
l = [98, 14, 62, 17, 56, 1, 5, 96]

"""
i = 0 : [14, 98, 62, 17, 56]
i = 1 : [14, 62, 98, 17, 56]
i = 2 : [14, 62, 17, 98, 56]
i = 3 : [14, 62, 17, 56, 98]

"""
for i in range(len(l)-1):
    if l[i] > l[i+1]:
        l[i], l[i+1] = l[i+1], l[i]
print(l[-1])

####################################################################
# print nth largest number

l = [98, 14, 62, 17, 56, 1, 5, 96]
n = 5

for _ in range(n):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
print(l[-n])









































































































