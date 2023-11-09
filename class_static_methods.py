class Calculator:
    a = 10
    b = 4

    def add(self):
        print(self)
        print(Calculator)
        return self.a + self.b

    def sub(self):
        return self.a - self.b

    def multiply(self):
        return self.a * self.b

    def division(self):
        return self.a / self.b


# calci1 = Calculator()

# calling add() using object
# print(calci1.add())

# calling add() using class
# print(Calculator.add(calci1))

##############################################################################
# class method
class Employee:
    name = "John"
    id = 10

    @classmethod
    def display(cls):
        print(cls.name, cls.id)

    def spam(self):
        print("in spam method")


e = Employee()
# e.display()
# Employee.display()
# Employee.spam(Employee())

#########################################################################
# modifying class variables using object address

class Employee:
    company_name = "TYSS"

    @classmethod
    def change_of_company(cls, new_company):
        cls.company_name = new_company


hr = Employee()
emp = Employee()
# print("before modification")
# print(emp.company_name)     # TYSS
# print(hr.company_name)      # TYSS
#
# emp.change_of_company("Infosys")
# print("\nafter modification")
# print(emp.company_name)     # Infosys
# print(hr.company_name)      # Infosys

##############################################################################
# creating alternate constructor

class Sample:

    def __init__(self, date, month, year):
        self.date = date
        self.month = month
        self.year = year

    @classmethod
    def split_date(cls, date_string):
        date, month, year = date_string.split("-")
        object_ = cls(date, month, year)
        return object_


s1 = Sample.split_date("18-4-2020")
print(s1.date)
print(s1.month)
































