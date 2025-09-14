age = int(input("Enter your age:"))

if(age>18):
    print("You are above the age,")
    print("Thanks")

elif(age == 0):
    print("0 is a invalid age,")
    print("Please enter a valid age") 

elif(age<0):
    print("You entered a negative age,")
    print("Please try again")
    
else:
    print("You are under the age,")
    print("Try again after",18-age,"year")
     