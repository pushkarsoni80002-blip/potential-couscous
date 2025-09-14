'''import os
os.remove("new_file.txt")'''


#if you want to check file:-
import os 
if os.path.exists("new_file.txt"):
    os.remove("new_file.txt")
else:
    print("Your file has been already deleted.")

'''
to delete a folder:-
import os
os.rmdir("my_folder")

'''