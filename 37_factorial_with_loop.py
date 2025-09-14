n = int(input("Enter a number:"))

number = 1

for i in range(1, n+1):
    number = number*i

print(f"The factorial of the {i} is {number} ")  
print("The factorial of the" , n ,"is",number)  