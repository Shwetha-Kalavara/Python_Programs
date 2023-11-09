# to create a list of even numbers from 1 to 50
l = []
for i in range(1, 51):
    if i % 2 == 0:
        l.append(i)
print(l)

# list comprehension
l = [i for i in range(1, 51) if i % 2 == 0]
print(l)

#######################################################################
# create a list with the words starting with vowel in th string
string = "hello everyone it is Thursday"
words = string.split()
l = []

for word in words:
    if word[0] in "aeiouAEIOU":
        l.append(word)
print(l)

# comprehension
l = [word for word in words if word[0] in "aeiouAEIOU"]
print(l)

########################################################################
# create a list of tuples of word and length pair from the given string
string = "hello everyone it is Thursday"
l = []

for word in string.split():
    l.append((word, len(word)))
print(l)

# comprehension
l = [(word, len(word)) for word in string.split()]
print(l)

#########################################################################
# create a list with words - if even length add it as it is else reverse and add

string = "hello everyone it is Thursday"
words = string.split()
l = []

for word in words:
    if len(word) % 2 == 0:
        l.append(word)
    else:
        l.append(word[::-1])

print(l)

# comprehension
l = [word if len(word) % 2 == 0 else word[::-1] for word in words]
print(l)
