"""
# to check even and odd numbers
num = [1, 2, 3, 4, 5]   # num[0], num[1], num[2]
length = len(num)   # 5
i = 0

while i < len(num):     # i = 0, 1

    if num[i] % 2 == 0:
        print("even number")
    else:
        print("odd number")

    i += 1

#####################################################################
# program to print all the vowels in the given string

string = "hello world"
i = 0

while i < len(string):
    if string[i] in "aeiouAEIOU":
        print(string[i])

    i += 1

#################################################################
# to print numbers from 10 to 1

i = 10

while i >= 1:
    print(i)

    i -= 1

##################################################################
# to print even numbers in the range 1 to 50
i = 1

while i <= 50:
    if i % 2 == 0:
        print(i)

    i += 1  # i = i + 1

####################################################################
# to print the numbers from -1 to -10

i = -1

while i >= -10:
    print(i)
    i -= 1  # i = i - 1

#####################################################################
# to traverse through the iterables

# string
s = "hello" # [10, 20, 30, 40]  # (1, 2, 3, 4)
i = 0

while i < len(s):
    print(s[i])
    i += 1

####################################################################
# to print characters in the string in reversed order
s = "hello"
i = len(s) - 1  # 5-1 = 4

while i >= 0:
    print(s[i], end="")
    i -= 1

# string concatenation
s = "hello"
i = 0
res = ""

while i < len(s):
    res = s[i] + res
    i += 1
print(res)

##################################################################
# print index and element

l = ["walmart", "google", "flipkart", "amazon", "gmail", "yahoo"]
i = 0

while i < len(l):
    print(i, l[i])
    i += 1

###################################################################
# print odd indexed characters in the string
s = "hello world"
i = 0

while i < len(s):
    if i % 2 == 1:
        print(s[i])
    i += 1

# method 2
i = 1

while i < len(s):
    print(s[i])
    i += 2

######################################################################
# to print the numeric values in the given string

# using inbuilt method
s = "abc1983jkhs234"
i = 0

while i < len(s):
    if s[i].isdigit():
        print(s[i])
    i += 1

# without using inbuilt method
i = 0

while i < len(s):
    if "0" <= s[i] <= "9":
        print(s[i])
    i += 1

################################################################
# count of lowercase alphabets
s = "Today's Date Is 08-03-2022"
i = 0
count = 0

while i < len(s):
    if "a" <= s[i] <= "z":
        count += 1
        print(s[i], end=" ")
    i += 1
print()
print(count)

####################################################################
# sum of all the digits

s = "Today's Date Is 08-03-2022"
i = 0
sum_ = 0

while i < len(s):
    if "0" <= s[i] <= "9":  #s[i].isdigit()
        sum_ += int(s[i])
    i += 1
print(sum_)


################### FOR LOOPS ###########################
# Traversing through iterables

s = "hello world"
i = 0

while i < len(s):
    print(s[i], end="")
    i += 1
print()

# string
s = "hello world"
for element in s:
    print(element, end="")  # prints all the characters in the string
print()

# list
l = [1, 2, 3, 4]
for item in l:
    print(item, end=" ")    # prints all the elements in the list
print()

# tuple
t = (123, 456, 789)
for item in t:
    print(item, end=" ")    # prints all the elements in the tuple
print()

# set
set_ = {12, 34, 56, 78, 12, 34}
for item in set_:
    print(item, end=" ")    # prints all the elements in the set
print()

# dictionary
d = {"a": 1, "b": 2, "c": 3}
for item in d:
    print(item, end=" ")    # prints only keys

###################################################################
# print 1 to 10
for num in range(1, 11):
    print(num, end=" ")
print()

###################################################################
# print 10 to 1
for num in range(10, 0, -1):
    print(num, end=" ")
print()

###################################################################
# even numbers
for num in range(1, 51):
    if num % 2 == 0:
        print(num, end=" ")
print()

# using range()
for num in range(2, 51, 2):
    print(num, end=" ")

####################################################################
# index and item

s = "hello"

# using while
i = 0
while i < len(s):
    print(i, s[i])
    i += 1
print()

# using for loop
for i in range(len(s)):
    print(i, s[i])

##################################################################
# to convert lower case to upper and vice versa

s = "123Hai WOrLd!!!"
res = ""

for char in s:
    if "a" <= char <= "z":
        res = res + chr(ord(char)-32)

    elif "A" <= char <= "Z":
        res += chr(ord(char) + 32)

    else:
        res += char

print(res)

#####################################################################
# number of elements present in the iterable

iterable = "hello"
count = 0

for ele in iterable:
    count += 1

print(count)

#####################################################################
# count of words in the sentence

sentence = "hai how are you"
words = sentence.split()
count = 0

for word in words:
    count += 1

# print(count)

##########################################################
# print all repeated characters
s = "hello world"

for char in s:
    if s.count(char) > 1:
        print(char, end=" ")

############################################################
# to remove the duplicate/repeated characters in the given string

s = "hello world"
# print(set(s))
res = ""

for char in s:
    if s.count(char) == 1:
        res += char

print(res)

for char in s:
    if char not in res:
        res += char
print(res)

###############################################################
# print duplicate characters without using inbuilt methods

s = "hello world"
non_duplicates = ""
duplicates = ""

for char in s:
    if char not in non_duplicates:
        non_duplicates += char
    else:
        duplicates += char

# print(non_duplicates)
# print("".join(set(duplicates)))

################################################################
# to print all the indices of the given substring

s = "hello world"
character = "o"

for i in range(len(s)):
    if s[i] == character:
        print(i)

#################################################################
# to print first occurrence of the given substring

s = "hello world"
char = "o"

for i in range(len(s)):
    if s[i] == char:
        print(i)
        break

###################################################################
# to print second occurrence of the given substring

s = "hello world"
char = "o"
count = 0

for i in range(len(s)):
    if s[i] == char:
        count += 1
        if count == 2:
            print(i)

###################################################################
# to print words starting with vowels

sentence = "It is Tuesday"
words = sentence.split()

for word in words:
    if word[0] in "aeiouAEIOU":
        print(word)

############################################################
# loop control statements

# break

for i in range(10):
    if i == 5:
        break
    print(i, end=" ")
print()

# continue
for i in range(10):
    if i == 5:
        continue
    print(i, end=" ")


for i in range(10):
    pass

###########################################################
# create a list with even length words
sentence = "hai good afternoon , welcome to afternoon session"
l = []
words = sentence.split()

for word in words:
    if len(word) % 2 == 0:
        l.append(word)  # l += [word]
# print(l)

###########################################################
# create a list with words ending with vowels

sentence = "hai good afternoon , welcome to afternoon session"
l = []
words = sentence.split()

for word in words:
    if word[-1] in "aeiouAEIOU":
        l.append(word)

print(l)

###########################################################
# create a set with words ending with vowels

sentence = "hai good afternoon , welcome to afternoon session"
s = set()
words = sentence.split()

for word in words:
    if word[-1] in "aeiouAEIOU":
        s.add(word)

print(s)

##################################################################
# to create a list of tuples with word and its length pair

sentence = "hai good afternoon , welcome to afternoon session"
l = []
words = sentence.split()
for word in words:
    item = word, len(word)
    l.append(item)
print(l)

#################################################################
# create a dictionary with word and length pair only if the word is starting
# with vowels

sentence = "hai good afternoon , welcome to afternoon session"
d = {}
words = sentence.split()

for word in words:
    if word[0] in "aeiouAEIOU":
        d[word] = len(word)

print(d)

##################################################################
# create a dictionary with letter and the word starting with that letter pair

sentence = "python is a programming language"
d = {}
words = sentence.split()

for word in words:
    if word[0] in d:
        d[word[0]].append(word)
    else:
        d[word[0]] = [word]

print(d)

#################################################################
# create a dictionary of character and its indices pair

s = "hello world"
d = {}

for i in range(len(s)):
    if s[i] not in d:
        d[s[i]] = [i]
    else:
        d[s[i]].append(i)
print(d)

#####################################################################
# WAP to create a dictionary with character and its ascii value pair
s = "hello world"
d = {}

for i in s:
    d[i] = ord(i)
print(d)

#####################################################################
# to create a dictionary with values of integer data type

d = {"a": 1, "b": "hello", "c": 85, "d": 12.3, "e": [1, 2, 3]}
res = {}

# 1
for i in d:
    if isinstance(d[i], int):
        res[i] = d[i]
print(res)

# 2
for key, value in d.items():
    if isinstance(value, int):
        res[key] = value
print(res)

#################################################################

d = {"a": 1, "b": "hello", "c": 85, "d": 12.3, "e": [1, 2, 3]}
res = {}

for key, value in d.items():
    if isinstance(value, str):
        res[key] = value[::-1]
    else:
        res[key] = value
# print(res)

"""
################################################################







































































































































































































































































































































