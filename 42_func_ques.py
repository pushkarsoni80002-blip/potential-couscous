def greatest(a,b,c):
    if(a>b and a>c):
        return a                
    
    elif(b>c and b>a):
        return b 
    
    else:
        return c 
    
a = int(input("Enter first digit:"))
b = int(input("Enter second digit:"))
c = int(input("Enter third digit:"))

print(greatest(a,b,c))