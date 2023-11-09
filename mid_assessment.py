# Write a decorator to count the number of decorated functions
"""
count = 0
def counter(func):
    global count
    count += 1
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs)
    return wrapper


@counter        # add = counter(add)
def add(a, b):
    return a + b


@counter        # sub = counter(sub)
def sub(a, b):
    return a - b

# add(1, 2)
# add(1, 2)
# sub(1, 2)
# print(count)

# Write a program to print only even lines in a file( consider filename as sample.txt)

# with open("file") as f:
#     for line_no, line in enumerate(f, start=1):
#         if line_no % 2 == 0:
#             print(line)

# Write a function that returns the nth line and last n lines from a file.
from itertools import islice
from collections import deque

n = 2
with open("file") as file:
    # method 1
    for line_no, line in enumerate(file, start=1):
        if line_no == n:
            # print(line)
            break

    # method 2
    line = islice(file, n-1, n)

    # last n lines
    lines = deque(file, n)

###########################################################################
# Write a program to print longest non repeated word in the sentence,
s = "see and saw went to see a sea"
words = s.split()
d = {word: len(word) for word in words if words.count(word) == 1}
# print(sorted(d.items(), key=lambda item: item[-1])[-1])

##########################################################################

# sort the dictionary based on the last character of the key.
prices = {'ACME': 45.23, 'AAPL': 612.78, 'IBM': 205.55, 'HPQ': 37.20, 'FB': 10.75 }

res = sorted(prices.items(), key=lambda item: item[0][-1])
# print(dict(res))
#########################################################################
# Build a list with only  even length string using filter function
names = ['apple', 'google', 'yahoo', 'facebook', 'yelp', 'flipkart', 'gmail', 'instagram', 'microsoft']

def even_(item):
    if len(item) % 2 == 0:
        return item

# print(list(filter(even_, names)))

############################################################################
# Write a dictionary comprehension to create a dictionary with word as its key
# and if the word is of numeric type reverse it else add the word as it is in
# the value.

sentence = "12 plus 18 equals to 30"
words = sentence.split()

d = {word: word[::-1] if word.isdigit() else word for word in words}
# print(d)
"""
############################################################################
# Write a program to get the following output.
# o/p : 2A2B3C1D2A1C1D

s = "AABBCCCDAACDA"
i = 0
res = s
op = ""

while i < len(s):
    res = res.lstrip(s[i])
    count = len(s) - len(res) - i
    op += str(count) + s[i]
    i += count


# print(op)
###########################################################################
# Write a program to get the following output from the list                             [1, 2, 3, 4, 5, 6, 7, 8, 9]
#     [1, 2]
#     [3, 4]
#     [5, 6]
#     [7, 8]
#     [9]

l = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(0, len(l), 2):
    print(l[i: i+2])

#########################################################################
# Find all max numbers from the below list
numbers = [1, 2, 3, 0, 4, 3, 2, 4, 2, 1, 0, 4]

max_num = max(numbers)
print(max_num)

for num in numbers:
    if num == max_num:
        print(num)








































