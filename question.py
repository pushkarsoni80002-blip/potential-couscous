marks1 = int(input("Enter marks1:"))
marks2 = int(input("Enter marks2:"))
marks3 = int(input("Enter marks3:"))

total_precentage = (marks1+marks2+marks3)/300*100

if(total_precentage>33 and marks1>33 and marks2>33 and marks3>33):
  if(marks1>33 and marks2>33 and marks3>33):
    print("You are pass,",total_precentage)
    print("Congratulations")

else:
    print("You are fail,",total_precentage)
    print("Try again next year")