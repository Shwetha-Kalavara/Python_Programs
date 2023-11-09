from collections import defaultdict
#******************* default dict *********************************
"""
# create a dictionary with length and words pair in the given sentence

sentence = "hi how are you doing today"
d = dict()
words = sentence.split()

# normal dictionary
for word in words:
    key = len(word)
    if key not in d:
        d[key] = [word]
    else:
        d[key].append(word)     # d[key] += [word]
print(d)

# default dict
dd = defaultdict(list)

for word in words:
    dd[len(word)].append(word)
# print(dd)

#############################################################
# word and its count pair

sentence = "hello hai hello how are you how are you hai hello"
d = {}
words = sentence.split()

# normal dictionary
for word in words:
    if word not in d:
        d[word] = 1
    else:
        d[word] += 1
print(d)

# default dict
dd = defaultdict(int)

for word in words:
    dd[word] = dd[word] + 1

print(dd)

##############################################################
# index and word pair
sentence = "hello hai hello how are you how are you hai hello"
d = {}
words = sentence.split()

# using range
for i in range(len(words)):
    d[i] = words[i]
print(d)

# using enumerate
d1 = {}
for index, item in enumerate(words):
    d1[index] = item
print(d1)

####################################################
# convert 2 lists into a dictionary

l1 = ["hello", "world"]
l2 = [10, 20]
d = {}

#
for i in range(len(l1)):
    d[l1[i]] = l2[i]
print(d)

d1 = {}
for item1, item2 in zip(l1, l2):
    d1[item1] = item2
print(d1)

###############################################################
# reversing an iterable

s = "hello"

# slicing
print(s[::-1])

# concatenation
res = ""
for char in s:
    res = char + res
print(res)

# reversed()
for i in reversed(s):
    print(i, end="")
"""
################################################################
"""
# Activity

# 1
l1 = [1, 2, 3]
l2 = [4, 5, 6]

# print(dict(zip(l1, l2)))

# 2(a)
temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}
# print(list(temperatures.items()))

l = []
for item in temperatures.items():
    l.append(item)
print(l)

l = []
for key, value in temperatures.items():
    l.append((key, value))
print(l)

# 2(b)

temperatures = {"Bangalore": (26, 32), "Chennai": (29, 35), "Delhi": (31, 36)}

# temperatures.items() = [("Bangalore", (26, 32)), ("Chennai",(29, 35)), ("Delhi", (31, 36))]

l = []
for key, (value1, value2) in temperatures.items():  # deep unpacking
    l.append((key, value1, value2))

print(l)

"""















































