""

a = 4

if a > 5:
    print("a is greater than 5")

print("end of if condition")

######################################################
# even or odd

a = 4
if a % 2 == 0:
    print(f"{a} is an even number")

else:
    print(f"{a} is an odd number")

############################################################
# iterable even length or not

s = "hello"

if len(s) % 2 == 0:     # bool(len(s) % 2 == 0)
    print("iterable has even number of elements")
else:
    print("iterable has odd number of elements")

# inline if else statement
print("even length" if len(s) % 2 == 0 else "odd length")

#################################################################
# greatest of 2 numbers

x = int(input("enter value of x: "))
y = int(input("enter value of y: "))

if x > y:
    print("x is the greater number")
else:
    print("y is the greater number")

# inline if else
print("x is greater" if x > y else "y is greater")

##########################################################
# palindrome or not

s = "hello"

if s[::-1] == s:
    print(f"the string {s} is a palindrome")
else:
    print(f"the string {s} is not a palindrome")

# inline if else
print("palindrome" if s[::-1] == s else "not a palindrome")

################################################################
# check whether the given number is palindrome or not

n = 1221
x = str(n)      # "1221"

if x[::-1] == x:
    print(f"{n} is a palindrome")
else:
    print(f"{n} is not a palindrome")

# inline if else
print("palindrome" if str(n)[::-1] == str(n) else "not a palindrome")

#####################################################################
# check if the string is starting with vowels

s = "apple"

if s[0] in "aeiouAEIOU":
    print("string is starting with vowel")
else:
    print("string is not starting with vowel")

# inline if else
print("vowel" if s[0].lower() in "aeiou" else "not vowel")

###############################################################
# check if the string is ending with vowel or not
s = "apple"

if s[-1] in "aeiouAEIOU":
    print("string is ending with vowel")
else:
    print("string is not ending with vowel")

# inline if else
print("ends with vowel" if s[-1].lower() in "aeiou" else "not ending with vowel")

###############################################################
# checking if the iterable is empty or not

iterable = ""

if iterable:      # bool(bool(iterable))
    print("iterable is not empty")
else:
    print("iterable is empty")

# inline if else
print("not empty" if iterable else " empty")

##################################################################
# check if the first digit of the number is divisible by 3 or not

n = 1234
x = str(n)  # "1234"

if int(x[0]) % 3 == 0:
    print("number is divisible by 3")
else:
    print("number is divisible by 3")

# inline if else
print("divisible by 3" if int(x[0]) % 3 == 0 else "not divisible by 3")

##############################################################
# to print greatest of 3 numbers

a = 10
b = 30
c = 20

if (a > b) and (a > c):
    print("a is the greatest number")

elif b > c:
    print("b is the greatest number")

else:
    print("c is the greatest number")


################################################################
# to check if the number is divisible by 3 or 9
a = 18
if a % 3 == 0:
    print("divisible by 3")

elif a % 9 == 0:
    print("divisible by 9")

############################################################
# to check if the number is divisible by 3 and 9
a = 18
if a % 3 == 0:
    print("divisible by 3")

if a % 9 == 0:
    print("divisible by 9")

############################################################
# to check if the given character is an alphabet ot digit or spl character

# using inbuilt method
char = "n"

if char.isalpha():
    print("character is an alphabet")

elif char.isdigit():
    print("character is a number")

else:
    print("character is a special character")

# without using inbuilt method
char = "n"

if "a" <= char <= "z" or "A" <= char <= "Z":
    print("character is an alphabet")

elif "0" <= char <= "9":
    print("character is a number")

else:
    print("character is a special character")

####################################################################
# to convert to uppercase and vice-versa

# using inbuilt methods
char = "b"

if char.isupper():
    print(char.lower())

elif char.islower():
    print(char.upper())

else:
    print("character is not an alphabet")

#without using inbuilt method
char = "B"

if "a" <= char <= "z":
    upper_ = chr(ord(char) - 32)
    print(upper_)

elif "A" <= char <= "Z":
    print(chr(ord(char) + 32))

else:
    print("character is not an alphabet")

#################################################################
# check if the string is starting with vowels or not

s = "hello"

if s[0] not in "aeiouAEIOU":
    print("starts with consonant")
else:
    print("starts with vowels")

# inline if else
print("starts with consonant" if s[0].lower() not in "aeiou" else "starts with vowels")
###########################################################
s = "eve"
d = {}

if s[0].lower() in "aeiou":
    # d[key] = value
    d[s] = len(s)

# print(d)


########################################################################
# create a dictionary of word and ascii value of first character pair, if 
# the word is of even length else create a dictionary with word and its length pair

s = "apple"
d = {}

if len(s) % 2 == 0:
    d[s] = ord(s[0])
else:
    d[s] = len(s)
print(d)

# inline if else
d[s] = ord(s[0]) if len(s) % 2 == 0 else d[s] = len(s)
print(d)

##########################################################################
# inline conditional statements
n = 6

if n % 2 == 0:
    print("even num")
else:
    print("odd")

# (True block if condition else False block)
print("even num" if n % 2 == 0 else "odd num")




























































































































