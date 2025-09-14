class Employee:
    language = "python" 
    salary = 10000

    def getInfo(self):
        print(f"The language is {self.language}.The salary is {self.salary}")
    
    def greet(self):
        print("Good Morning")

harry = Employee()
harry.greet()
harry.getInfo()
