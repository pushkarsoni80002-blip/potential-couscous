class Employee:
    language = "python" #This is a class attribute
    salary = 10000


harry = Employee()
harry.language = "Java" #This is a object/instance attribute
print(harry.language,harry.salary)

#its firstly check object object attributes, if object attribute didn't exist it print class attribute
#but firstly it prints object attributes