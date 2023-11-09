import os

os.chdir(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files")

# read(no of characters)
with open("sample.txt") as file:
    print(file.read())     # reads entire file as a single string
    print(file.read(3))     # reads first 3 characters
    print(file.read(5))     # read next 5 characters
    print(file.read(10))


# readline(no of characters)
with open("sample.txt") as file:
    print(file.readline())      # read a single line as a string
    print(file.readline())
    print(file.readline(5))
    print(file.readline(30))
    print(file.readline())

# readlines()
with open("sample.txt") as file:
    print(file.readlines())
    print(file.readlines(10))


# tell() and seek()
with open("sample.txt") as file:
    for line in file:
        print(line)

    print(file.tell())
    file.seek(1)
    print(file.tell())

    for line in file:
        print(line)

####################################################################

# write(), writelines()
with open("example.txt", "a") as file:
    print(file.write("Today is Monday\n"))
    # file.write("Tomorrow is Tuesday")
    file.writelines(["Today is Monday\n", "Tomorrow is Tuesday\n"])


# read and write

with open("example.txt", "r+") as file:
    file.write("hello\n")
    for line in file:
        print(line)





































