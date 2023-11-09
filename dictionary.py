# creating a dictionary

d = {"a": 1, "b": 2}
d = dict({"a": 1, "b": 2})
d = dict([("a", 1), ("b", 2)])
d = dict(a=1, x=10)

# default value
d = {}
d = dict()


# composite keys

# d1 = {("march", 4): "Friday",
#       ("march", 5): "Saturday"
#       }

# accessing the values
d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}

# print(d["Bangalore"])
# print(d["Kolkata"])     # KeyError

# print(d.get("Bangalore", "Key is not present"))
# print(d.get("Kolkata", "Key is not present"))

# inserting values to a dictionary
d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}

# d["Kolkata"] = 40
# print(d)

# d["Bangalore"] = 27
# print(d)
#
# d.update(Mysore=26)
# print(d)
#
# d.update({"a": 1, "b": 1, "c": 2})
# print(d)

# print(d.setdefault("Rajasthan"))
# print(d)
#
# print(d.setdefault("Rajasthan", 50))
# print(d)


# delete values from a dictionary
d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}

# print(d.pop("Chennai"))
# print(d)
#
# print(d.popitem())
# print(d)

#

# s = "hello"
# l = [1, 2, 3, 4]
# print(d.fromkeys(s))
# print(dict.fromkeys(l))
# print(d)

d = {'Bangalore': 25, "Chennai": 35, "Delhi": 30}
# print(d.keys())
# print(d.values())
# print(d.items())

# merging two iterables

s1 = "hai"
s2 = "hello"
print(s1 + s2)
print(*s1, *s2)

l1 = [1, 2, 3]
l2 = [4, 5, 6]
print(l1 + l2)
print([*l1, *l2])

t1 = (1, 2, 3)
t2 = (4, 5, 6)
print(t1 + t2)
print((*t1, *t2))

s1 = {1, 2, 3}
s2 = {4, 5, 6, 2}
print({*s1, *s2})

d1 = {"a": 1, "b": 2}
d2 = {"c": 3, "d": 4}
print({**d1, **d2})
print(d1 | d2)
