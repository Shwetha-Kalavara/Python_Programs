import re
import csv
import os
from selenium.webdriver import Chrome




# path = r"C:\Users\Dell\OneDrive\Desktop\practice.txt"

# # reader()
# with open(path) as file:
#     obj = csv.reader(file)      # data in list
#     print(obj)
#     for data in obj:
#         print(data)
#
# #DictReader()
# with open(path) as file:
#     obj = csv.DictReader(file)
#     for data in obj:
#         print(data)

# os.chdir(r"C:\Users\Dell\OneDrive\Desktop")
# # writer()
# with open("example.csv", "w") as file:
#     obj = csv.writer(file)      # accepts data in the form list
#
#     # writing single row
#     obj.writerow(["Employee_name", "E_ID"])
#     obj.writerow(["John", 10])
#
#     # writing multiple rows
#     data = ["sita", 3], ["ram", 1]
#     obj.writerows(data)


# DictWriter()
# with open("data.csv", "w") as file:
#     obj = csv.DictWriter(file, ["E_name", "E_ID"])
#
#     # writing header to the file
#     obj.writeheader()
#
#     # writing single row
#     obj.writerow({"E_name": "John", "E_ID": 8})
#
#     # writing multiple rows
#     obj.writerows([{"E_name": "John", "E_ID": 8}, {"E_name": "John", "E_ID": 8}])


# l = [10, 2, 3, 45, 41, 12, 17, 58, 24, 1, 21, 15, 14]
# l = [0, 1, 0, 0, 0, 1, 1, 0, 0, 1,]
# for i in l:
#     for j in range(len(l)-1):
#         if l[j] > l[j+1]:
#             l[j], l[j+1] = l[j+1], l[j]
# print(l)


# s = "hi hello how are you"
# s1 = "".join(re.findall(r"\w+", s))
# s2 = ""
# print(s1)
# for i in range(len(s1)):
#     if i % 4 == 0:
#         s2 += " " + s1[i]
#     else:
#         s2 += s1[i]
#
# print(s2)


# driver = Chrome("./chromedriver")
# driver.get("https://www.flipkart.com/")


















# def dec(func):
#     def nest(m, n):
#         m = abs(m)
#         n = abs(n)
#         return func(m, n)
#     return nest
#
# @dec
# def sub(a, b):
#     return a - b
#
#
# print(sub(2, 3))



s="@#$abdc123"
l = [i for i in s if i >= "a" and i <= "z"]
l1 = [ord(i) for i in l]
l1.sort()
l2 = [chr(i) for i in l1]
print("".join(l2))



# a = 10
# b = set(a)
# print(type(b))

# def dec(func):
#     def nest(m, n):
#         c = abs(m - n)
#         return c
#     return nest
#
# @dec
# def sub(a, b):
#     return a - b


# print(sub(2, 3))


s = {10, 20}
b = int(s)
print(type(b))

s = "@#$bcad123"
l = re.findall(r"[a-z]", s)
l.sort()
print("".join(l))








