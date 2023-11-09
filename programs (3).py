import csv, os
os.chdir(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\csv_files")

# to read all the names of the employees in employee.csv file

# reader()
with open("employees.csv") as csv_file:
    obj = csv.reader(csv_file)
    header = next(obj)
    # print(header)
    # for data in obj:
    #     print(data[0])

# DictReader()
with open("employees.csv") as csv_file:
    obj = csv.DictReader(csv_file)
    for data in obj:
        print(data)

#################################################################
# Write a program to print only the salaries that are > 70000

# reader()
with open("employees.csv") as csv_file:
    obj = csv.reader(csv_file)
    header = next(obj)

    for data in obj:
        if int(data[-1]) > 70000:
            print(data[-1])

# DictReader()
with open("employees.csv") as csv_file:
    obj = csv.DictReader(csv_file)

    for data in obj:
        if data["pay"] > "70000":
            print(data["pay"])









