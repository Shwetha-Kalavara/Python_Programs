# create a dictionary with word and its length pair
sentence = "hello good afternoon"
words = sentence.split()
d = {}

for word in words:
    d[word] = len(word)
print(d)

# comprehension
d = {word: len(word) for word in words}
print(d)

#############################################################################
# create a dictionary with word and its length pair only if it is of even length
sentence = "hello good afternoon"
words = sentence.split()

d = {}
for word in words:
    if len(word) % 2 != 0:
        d[word] = len(word)
print(d)

d = {word: len(word) for word in words if len(word) % 2 != 0}
print(d)

########################################################################
# index and word -> if the word is even, keep it as it is else reverse it

sentence = "hello good afternoon"
words = sentence.split()
d = {}

# using range()
for i in range(len(words)):
    if len(words[i]) % 2 == 0:
        d[i] = words[i]
    else:
        d[i] = words[i][::-1]

# using enumerate()
for index, item in enumerate(words):
    if len(item) % 2 == 0:
        d[index] = item
    else:
        d[index] = item[::-1]
print(d)

# comprehension
d = {index: item if len(item) % 2 == 0 else item[::-1] for index, item in enumerate(words)}
print(d)

























