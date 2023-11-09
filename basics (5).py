# try - except

# default except block
# a = 1
# b = 1
#
# try:
#     print("in try block")
#     z = a / b
#     print(z)
#
# except:
#     print("in except block")

#############################################################################
# specific except block
# a = 1
# b = 0
#
# try:
#     print("in try block")
#     # z = a / b       # zerodivision
#     l.append(10)    # NameError
#     print(z)
#
# except ZeroDivisionError:
#     print("in except block")

###########################################################################
# Multiple except block
a = 1
b = 0

# try:
#     print("in try block")
#     z = a / b       # zerodivision
#     # l.append(10)    # NameError
#     str().split(" ", 2, 3)
#     print(z)
#
# except (ZeroDivisionError, NameError) as msg:
#     print(msg)

###########################################################################
# generic exception block
# a = 1
# b = 2
# try:
#     print("in try block")
#     z = a / b       # zerodivision
#
#
# except Exception as msg:
#     print(msg)
#
# else:
#     print(z)
#
# finally:
#     print("process finished")

##########################################################################

class UserNotPresentException(Exception):
    pass

username = input("enter the username: ")

if username != "John":
    raise UserNotPresentException("username is not present")











