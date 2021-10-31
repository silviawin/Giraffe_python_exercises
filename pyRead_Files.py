# to read a file that is stores outside of your python files
# in the commant open use the either the absolute path, the relative path or the file name if it is in the same folder
# the second argument is which mode you want to open the file "r" or "w" or "a" ( append") and "r+" to read and write
# always close an opened file

employee_file = open("employees", "r")

# before doing anything check if the file is readable

# print(employee_file.readable())
# print("\n")
# print(employee_file.read())
# print("\n")
# print(employee_file.readline())
# print(employee_file.readline())
# the next command will put all the lines of the file in an array
# print(employee_file.readlines())

# the next for loop works with or without the .readlines() appended
for employee in employee_file.readlines():
    print(employee)

employee_file.close()
