import csv
import os

path = r"C:\Users\Vidyashree M C\Desktop\sample.csv"

# reader()
with open(path) as file:
    obj = csv.reader(file)      # data in list
    print(obj)
    for data in obj:
        print(data)

#DictReader()
with open(path) as file:
    obj = csv.DictReader(file)
    for data in obj:
        print(data)


# writing into csv
os.chdir(r"C:\Users\Vidyashree M C\PycharmProjects\Alpha4\files\csv_files")

# writer()
with open("example.csv", "w") as file:
    obj = csv.writer(file)      # accepts data in the form list

    # writing single row
    obj.writerow(["Employee_name", "E_ID"])
    obj.writerow(["John", 10])

    # writing multiple rows
    data = ["sita", 3], ["ram", 1]
    obj.writerows(data)


# DictWriter()
with open("data.csv", "w") as file:
    obj = csv.DictWriter(file, ["E_name", "E_ID"])

    # writing header to the file
    obj.writeheader()

    # writing single row
    obj.writerow({"E_name": "John", "E_ID": 8})

    # writing multiple rows
    obj.writerows([{"E_name": "John", "E_ID": 8}, {"E_name": "John", "E_ID": 8}])












