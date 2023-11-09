# comma separated string

# s = "hello welcome to python"

# separating each character
# list_ = list(s)

# words = s.split()
# print(words)
# print(*words, sep=",")

###############################################################################################
# s = "hello welcome to python"
# res = ""
# for char in s:
#     if s.count(char) > 1:   # if char in res:
#         res = res + "-"
#     else:
#         res = res + char


# **126 In the list below, find all the number pairs which results in 10 either when added or subtracted**

a = [3, 5, -4, 8, 11, 1, -1, 5, 6]
res = []
for i in range(len(a)):
    for j in range(i+1, len(a)):
        if abs(a[i]) + abs(a[j]) == 10 or a[i] - a[j] == 10:
            res.append([a[i], a[j]])


# print(res)
