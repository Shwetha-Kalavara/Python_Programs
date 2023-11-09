# to sort the list in ascending order without using inbuilt method

l = [98, 14, 62, 17, 56, 1, 5, 96]

for _ in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] > l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
print(l)

###################################################################
# nth smallest number
l = [98, 14, 62, 17, 56, 1, 5, 96]
n = 5
for _ in range(len(l)-1):
    for i in range(len(l)-1):
        if l[i] < l[i+1]:
            l[i], l[i+1] = l[i+1], l[i]
print(l[-n])

###################################################################
# longest word
sentence = "python is a programming language"
l = sentence.split()

for _ in range(len(l)-1):
    for i in range(len(l) - 1):
        if len(l[i]) > len(l[i+1]):
            l[i], l[i+1] = l[i+1], l[i]
print(l[-1])

###################################################################
# longest non repeated word
sentence = "python is a programming language and programming is fun"
l = sentence.split()
max_word = ""

for word in l:
    if len(word) > len(max_word) and l.count(word) == 1:
        max_word = word
print(max_word)

####################################################################
# tuple of word and its count
sentence = "python is a programming language and programming is fun"
words = sentence.split()
l = []

for word in set(words):
    l.append((word, words.count(word)))
print(l)

###################################################################
# factorial from 1 to 5
num = 5
fact = 1
l = []

for i in range(1, num+1):
    fact = fact * i
    l.append(fact)
print(l)

# list comprehension
from math import factorial
l = [factorial(i) for i in range(1, num + 1)]
print(l)