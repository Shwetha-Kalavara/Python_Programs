# anagrams

def anagram(string1, string2):
    return sorted(string1) == sorted(string2)


# print(anagram("tea", "teaa"))

# list of dictionaries

data = [
    {"name": "John", "age": 30},
    {"name": "Aman", "age": 19},
    {"name": "Gita", "age": 15}
]
def function(item):
    if item["age"] > 18:
        return item["age"]

res = list(filter(function, data))
print(res)
print(sorted(res, key=lambda item: item["age"]))


# s = ["flipkart", "apple", "google"]

# sorted(s, key=lambda item: item[-1])
# data[0]["name"]
# print(sorted(data, key=lambda dict_: dict_["age"]))


shares = {"ACME": 45.23, "AAPL": 612.78, "IBM": 205.55, "HPQ": 37.20}

def func(item):
    if item[1] > 40:
        return item

res = list(filter(func, shares.items()))
# print(res)

# print(sorted(res, key=lambda item: item[-1]))

# grouping anagrams

l = ["tea", "eat", "silent", "hello", "listen", "ate"]

d = {}

for item in l:      # tea
    key = "".join(sorted(item))    # ["a", "e", "t"]    --> "aet"
    if key not in d:
        d[key] = [item]
    else:
        d[key] += [item]

# print(d)
#######################################################################################################
l1 = [1, 2]
l2 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]


def zip_(a, b):
    res = []

    if len(a) == len(b):
        return list(zip(a, b))

    else:
        if len(a) > len(b):
            max, min = a, b
        else:
            max, min = b, a

        while max:
            res += list(zip(min, max))
            del max[:len(min)]

        return res

print(zip_(l1, l2))







































