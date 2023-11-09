s1 = {1, 2, 3, 10, 20, 30}
s2 = {10, 20, 40, 100}

# union, update

# print(s1.union(s2))
# print(s1, s2)

# s1.update(s2)
# print(s1)

# s1.update("hello")
# print(s1)

# s1.update([11, 12, 13])
# print(s1)

# intersection, intersection_update()

s1 = {1, 2, 3, 10, 20, 30}
s2 = {10, 20, 40, 100}

# print(s1.intersection(s2))

# s1.intersection_update(s2)
# print(s1)

# difference, difference_update

s1 = {1, 2, 3, 10, 20, 30}
s2 = {10, 20, 40, 100}

# print(s1.difference(s2))

# s1.difference_update(s2)
# print(s1)

# print(s1 - s2)

# symmetric_difference, symmetric_difference_update

s1 = {1, 2, 3, 10, 20, 30}
s2 = {10, 20, 40, 100}
# print(s2.symmetric_difference(s1))

s1.symmetric_difference_update(s2)
# print(s1)

# adding elements to a set
s1 = {1, 2, 3, 10, 20, 30}
# s1.add(40)
# s1.add("hello")
# s1.add([1, 2, 3])
# s1.add({100, 200})
# print(s1/)

# s1.update("hello")      # s1 -> {1, 2, 3, 10, 20, 30, "h", "e", "l", "o"}
# s1.update({100, 200, [3], 300}) # TypeError
# print(s1)

# pop(), remove(), discard()

s1 = {1, 2, 3, 10, 20, 30}
# print(s1.pop())
# print(s1)

# s1.remove(100)
# print(s1)

# print(s1.discard(100))
# print(s1)

# isdisjoint()
s1 = {1, 2, 3}
s2 = {4, 5, 6, 2}
print(s1.isdisjoint(s2))


# issuperset()
a = {1, 2, 3, 4, 5, 6, 7, 8}
b = {1, 2, 3}

print(a.issuperset(b))
print(b.issuperset(a))



print(b.issubset(a))






