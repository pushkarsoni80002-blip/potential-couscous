class Employee:
    language = "python" #This is a class attribute
    salary = 10000


harry = Employee()
harry.name = "Harry" #This is a object/instance attribute
print(harry.name,harry.language,harry.salary)

rohan = Employee()
rohan.name = "Rohan"
print(rohan.name,rohan.language,rohan.salary)

