##############################
a = 10
# print(a)

def fub():
    a = 10
    print(a + 10)

# fub()
# print(a)
######################################

# a = 1
# print(id(a))
# def fun():
#     global a
#     a = a + 1
#     print(a)
#
# # fun()
# # print(a)
# #####################################
#
# def fun():
#     global b
#     b = 20
# # fun()
# # print(b)
####################################################

# def spam():
#     c = 10
#     def wrapper():
#         b = 20
#         nonlocal c
#         c += 10
#         print(c)
#     wrapper()
####################################

l = [1, 2, 3, 4]
l1 = []
def square():
    for i in l:
        l1.append(i**2)
    print(l1)
square()
print(l1)

s = ""
string_ = "hai"
def rev(x):
    global s
    for i in x:
        s = i + s
    print(s)
rev(string_)

