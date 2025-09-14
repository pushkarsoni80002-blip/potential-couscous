#enter marks from user and do it in sort way 
#in this ques we use int() beacuse we entered numbers from user and we can do numbers in sort method
marks = []


s1 = int(input("Enter your number:"))
marks.append(s1)
s2 = int(input("Enter your number:"))
marks.append(s2)
s3 = int(input("Enter your number:"))
marks.append(s3)
s4 = int(input("Enter your number:"))
marks.append(s4)
s5 = int(input("Enter your number:"))
marks.append(s5)

marks.sort()

print(marks)