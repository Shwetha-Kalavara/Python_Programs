# upper()
s = "hello python"
res = s.upper()
print(res)
print(s)

# lower()
s1 = "HELLO"
print(s1.lower())
print(s1)

# count()
print(s.count("l"))
print(s.count("hello"))
print(s.count("hello", 3))

# find(), rfind()
s = "hello python"
print(s.find("e"))
print(s.find("o", 5))
print(s.find("hello"))
print(s.find("d"))

print(s.rfind("o"))
print(s.rfind("u"))

print()
# index(), rindex()
s = "hello python"

print(s.index("l"))
# print(s.index("u"))

print(s.rindex("l"))
print(s.rindex("py"))

print()
# replace()
s = "hai"
# s[2] = "y"
print(s.replace("i", "y"))
# print(s)

s = "hai how are you"
print(s.replace("a", "z", 1))


# startswith(), endswith()
s = "hai how are you"
print(s.startswith("hai"))
print(s.startswith("h"))
print(s.startswith("a", 1))

print(s.endswith("h"))
print(s.endswith("h", 0, 5))
print()

# split()
s = "hai how are you"

print(s.split())
print(s.split("a"))
print(s.split("a", 1))
print(s.split(" ", 2))

print()
# join()
s = "hai"

print("-".join(s))

s = "hai how are you"
res = s.split()
print(res)
print(" ".join(res))

print()
# strip(), lstrip(), rstrip()
s = "__hai__"

print(s.strip("_"))
print(s.lstrip("_"))
print(s.rstrip("_"))

s = "_@__hai_@$_"
print(s.strip("_"))
print(s.strip("_$@"))

s = "    hai    "
print(s.strip())

print()
# boolean methods
s = "hai"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print()

s = "12hai"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())
print(s.islower())
print(s.isupper())
print()

s = "hai hello"
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

s = "      "
print(s.isspace())

print()
s = "123"
print(s.isdigit())

































