# adding elements to the list

# append
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.append("instagram")
# print(names)

# names.append([1, 2, 3])
# print(names)

# extend
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.extend("instagram")
# print(names)
# names.extend([1, 2, 3])
# print(names)

# insert
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.insert(3, "facebook")
# print(names)

# removing elements from a list
# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']

# pop
# print(names.pop(2))
# print(names)

# print(names.pop())
# print(names)
# names.pop(10)

# remove
# names.remove("amazon")
# print(names)

# names.remove("flipkart")
# print(names)

# del

# names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# del names[2:]
# print(names)

# copy
# names = ['apple', 'google', ['yahoo', 'amazon'], 'microsoft']
# print(id(names))
# print(id(names[2]))
# list_ = names[::]
# print(id(list_))

# l = names.copy()
# print(list_)
# print(id(l))
# print(id(l[2]))


# sorting a list
names = ['apple', 'google', 'yahoo', 'amazon', 'microsoft']
# names.sort()    # ASCII
# print(names)

# names.sort(key=len)
# print(names)
# names.sort(reverse=True)
# print(names)

# using split and join
s = "hai how are you"
l = s.split()
print(l)

s1 = " ".join(l)
print(s1)

# using list constructor and join
s = "hai how are you"
l = list(s)
print(l)

# s2 = "".join(l)
s2 = str().join(l)
print(s2)







