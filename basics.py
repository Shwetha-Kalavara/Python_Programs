# creating class variables

class Employee:
    fname = "steve"
    lname = "jobs"


emp1 = Employee()
emp2 = Employee()

# accessing class variables using objects
# print(emp1.fname)
# print(emp2.lname)

# accessing class variables using classname
# print(Employee.fname)

# checking the attributes of class
# print(Employee.__dict__)

# checking the attributes of objects
# print(emp1.__dict__)

###########################################################################
# creating instance/object variables in class

class Employee:

    def __init__(self, fname, lname):     # initializer - initializes object variables
        self.fname = fname
        self.lname = lname


emp1 = Employee("mark", "zuckerberg")
emp2 = Employee("Rangnath", "swamy")

# accessing instance variables using objects
# print(emp1.fname)   # mark
# print(emp2.fname)   # Rangnath

# accessing instance variables using class
# print(Employee.fname)   # AttributeError

# checking the attributes of class
# print(Employee.__dict__)    # {__init__: address, other inbuilt attributes of class}

# checking the attributes of instances
# print(emp1.__dict__)        # {"fname": "mark", "lname": "zuckerberg"}
# print(emp2.__dict__)        # {"fname": "Rangnath", "lname": "swamy"}

###############################################################################################
# creating both class and instance variables with same name

class Employee:
    fname = "steve"         # class variables
    lname = "jobs"

    def __init__(self, fname, lname):
        self.fname = fname          # object/instance variables
        self.lname = lname


e1 = Employee("tata", "birla")
e2 = Employee("Mukesh", "Ambani")

# print(e1.fname)     # tata

############################################################################################
class Employee:
    fname = "steve"         # class variables
    lname = "jobs"

    def __init__(self, age, salary):
        self.age = age          # object/instance variables
        self.salary = salary


emp1 = Employee(20, 30000)
emp2 = Employee(30, 40000)

# modification w.r.t objects
# emp1.fname = "Einstien"
# print(emp1.fname)   # Einstien
# print(emp2.fname)   # steve
# print(Employee.fname)   # steve

# modification w.r.t class
# Employee.fname = "Ratan"
# print(Employee.fname)   # Ratan
# print(emp1.fname)       # Ratan
# print(emp2.fname)       # Ratan













































