d = {"a": 1, "b": "hello", "c": 85, "d": 12.3, "e": [1, 2, 3]}

# printing keys
for item in d:
    print(item, end=" ")
print()

for key in d.keys():
    print(key, end=" ")
print()

for key, value in d.items():
    print(key, end=" ")
print()

# printing values
d = {"a": 1, "b": "hello", "c": 85, "d": 12.3, "e": [1, 2, 3]}

for i in d:
    print(d[i], end=", ")
    # print(d.get(i))
print()

for value in d.values():
    print(value, end=", ")
print()

for key, value in d.items():
    print(value, end=", ")





