import os

os.chdir(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files")

# to print the number of characters in a file

# using len()
with open("sample.txt") as file:
    ch_count = 0
    for line in file:
        ch_count += len(line)
# print(ch_count)

# without using len()
with open("sample.txt") as file:
    ch_count = 0
    for line in file:
        for char in line:
            ch_count += 1
# print(ch_count)

#######################################################################
# to count the number of words in a file

# using len()
with open("sample.txt") as file:
    word_count = 0
    for line in file:
        words = line.split()
        word_count += len(words)
# print(word_count)

# without len()
with open("sample.txt") as file:
    word_count = 0
    for line in file:
        words = line.split()
        for word in words:
            word_count += 1
# print(word_count)

########################################################################
# to print lines starting with vowels

# with open("sample.txt") as file:
#     for line in file:
#         if line.strip():    # checking blank lines
#             if line[0] in "aeiouAEIOU":
#                 print(line)

#######################################################################
# to print line_no and number of words in a line

# normal method
# with open("sample.txt") as file:
#     line_no = 0
#     for line in file:
#         line_no += 1
#         words = line.split()
#         print(line_no, len(words))

# enumerate()
# with open("sample.txt") as file:
#     for line_no, line in enumerate(file, start=1):
#         print(line_no, len(line.split()))

########################################################################
# to read a file from the last line

# using slicing
# with open("sample.txt") as file:
#     list_ = list(file)
#     for line in list_[::-1]:
#         print(line)

# reversed()
# with open("sample.txt") as file:
#     for line in reversed(list(file)):
#         print(line)

#####################################################################
# to count the number of lines without loading file into the memory

with open("sample.txt") as file:
    line_no = 0
    for _ in file:
        line_no += 1
# print(line_no)

########################################################################
# to count the number of spaces in the file

# using built in method
with open("sample.txt") as file:
    count = 0
    for line in file:
        count += line.count(" ")
# print(count)

# without using built in methods
with open("sample.txt") as file:
    count = 0
    for line in file:
        if line.strip():
            for char in line:
                if char == " ":
                    count = count + 1
# print(count)


with open("sample.txt") as file:
    count = 0
    for line in file:
        words = line.split()
        count += len(words)-1
# print(count)

#############################################################################
# to create a dictionary with each word and its count pair in the file

with open("sample.txt") as file:
    d = {}
    for line in file:
        if line.strip():
            for word in line.split():
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1

# print(d)
#################################################################################
# most occurring word in the file

with open("sample.txt") as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split()
            for word in words:
                if word not in d:
                    d[word] = 1
                else:
                    d[word] += 1

least, *rest, most = sorted(d.items(), key=lambda item: item[-1])
# print(most, least)

########################################################################
# to print nth line from a file
n = 4
# using enumerate
# with open("sample.txt") as file:
#     for line_no, line in enumerate(file, start=1):
#         if line_no == n:
#             print(line)

# normal method
# with open("sample.txt") as file:
#     count = 0
#     for line in file:
#         count += 1
#         if count == n:
#             print(line)

####################################################################
# to print first 5 lines

n = 5
# with open("sample.txt") as file:
    # count = 0
    # for line in file:
    #     count += 1
    #     if count <= n:
    #         print(line)

# using islice()
from itertools import islice

l = 5
# with open("sample.txt") as file:
#     lines = islice(file, l)
#     for line in lines:
#         print(line)

##################################################################
# to print 4th to 7th lines

# using islice
# with open("sample.txt") as file:
#     lines = islice(file, 4-1, 8)
#     for line in lines:
#         print(line)

# normal method
# with open("sample.txt") as file:
#     count = 0
#     for line in file:
#         count += 1
#         if 4 <= count < 8:
#             print(line)

######################################################################
# to print last 'n' lines from a file
# n = 2
# with open("sample.txt") as file:
#     count = 0
#     for _ in file:
#         count += 1
#     file.seek(0)
#     lines = islice(file, count - n, count)
#     for line in lines:
#         print(line)

# deque()
from collections import deque

# with open("sample.txt") as file:
#     d = deque(file, n)
#     for line in d:
#         print(line)
##################################################################

# ip addresses and their count

with open("access-log.txt") as file:
    d = {}
    for line in file:
        if line.strip():
            data = line.split()
            if data[0] not in d:
                d[data[0]] = 1
            else:
                d[data[0]] += 1
# print(d)
# print(dict(sorted(d.items(), key=lambda item: item[-1])))

# most occurring brand names
d = {}
with open("data.txt") as file:
    for line in file:
        if line.strip():
            words = line.split("\t")
            if words[0] not in d:
                d[words[0]] = 1
            else:
                d[words[0]] += 1

min_, *rest, max_ = sorted(d.items(), key=lambda item: item[-1])
# print(max_)

from collections import Counter, defaultdict

with open("data.txt") as file:
    l = []
    for line in file:
        if line.strip():
            words = line.split('\t')
            l.append(words[0])

c = Counter(l)
# print(c)
# print(c.most_common(1))

########################################################################

with open("sample.log") as file:
    d = {}
    for line in file:
        if line.strip():
            words = line.split()
            if words[2] not in d:
                d[words[2]] = 1
            else:
                d[words[2]] += 1

# print(d)

########################################################################
# names of the countries
with open("football.txt", encoding="UTF-8") as file:
    print(file)
    d = defaultdict(int)
    for line in file:
        if line.strip():
            words = line.split("\t")
            d[words[1]] += 1

# print(d)




























































































































































