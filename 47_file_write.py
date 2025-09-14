f = open("file2.txt","w")
string = "Hey! Harry how are you?\n"\
    "What's up!\n"

f.write(string)

f = open("file2.txt","a")
f.write("The file has more content now!")
f.close()


g = open("file2.txt","r")
print(g.read())
f.close()

#w is use for over write the data
#a(append) is use for add data in last