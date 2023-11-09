l = [1, 2, 3, 4]

# iterable      # __iter__
# for item in l:
#     print(item)

# print(dir(l))

# converting an iterable into iterator object

a = iter(l)
print(a)

# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))
# print(next(a))

# for item in l:
#     print(item)
#
#
# # iterator protocol
#
# a = iter(l)
#
# while True:
#     try:
#         item = next(a)
#
#     except StopIteration:
#         break
#
#     print(item)


# from sketchpy import library as lib


# o = lib
print(bin(10))

l = [4, 6, 3, 5, 7]
c = 0
for i in l:
    for j in l:
        if i | j == i:
            c += 1
print(c)




print(4 | 6)






