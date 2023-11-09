# without context manager

path = r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\sample.txt"

# file = open(path)
# print(file)
# print(file.closed)  # False
# file.close()
# print(file.closed)  # True

# with context manager

import os
os.chdir(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files")

# with open("sample.txt") as file:
#     print(file)
#     print(file.mode)
#     print(file.name)
#     print(file.readable())
#     print(file.writable())
    # print(file.closed)      # False
# print(file.closed)      # True

###################################################################
# with open("sample.txt", "w") as file:
#     print(file)
#     print(file.readable())
#     print(file.writable())

# with open("sample.txt", "a") as file:
#     print(file)
#     print(file.writable())

# os.remove("sample1.txt")
# with open("sample1.txt", "x") as file:
#     print(file.readable())
#     print(file.writable())

# with open("sample.txt", "r+") as file:
#     print(file.writable())
#     print(file.readable())

#############################################################




















