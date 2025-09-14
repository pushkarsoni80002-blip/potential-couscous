marks = {
    "Harry": 100,
    "Pranav": 60,
    "Aditya":95,
    "Rohan":50,
    "Kartik":65
}


print(marks.items()) #it returns value in form of tuple

print(marks.keys()) #it returns value as all first element(names)

print(marks.values()) #it returns value as all second element(marks)

marks.update({"Ram": 40, "Pranav":70}) #it adds new name and it can also update marks

print(marks)