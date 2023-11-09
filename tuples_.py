# single value tuple
t = ()
t = tuple()

t = (1,)

# Activity

t1 = (1, 2, 3, 4)
t2 = (10, 20, 30)

c = (*t1, *t2)
# print(c)

t = (1, 2, 3, 4, ["hai", "hello", 23], "python")
t[4][0] = "y"
print(t)

a = [1, 2, 3]
b = [4, 5, 6]
print([a, b])
print((a, b))













