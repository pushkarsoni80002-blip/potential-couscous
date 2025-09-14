n = int(input("Enter a number:"))

def factorial(n):
    if(n == 1 or n == 0):
        return 1
    return n* factorial(n-1)


#recursion vo hota h jo khud ko hi call kerta hai!


print(f"The factorial of this number is: {factorial(n)}")
print("The factorial of this number is:" , factorial(n))