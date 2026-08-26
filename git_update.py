#Import relevant modules
import subprocess
import os

#Ask user for message to post
message = input("Enter message explaining upload: ")

#Define relevant working directory
directory = r"C:\Users\johnr\Desktop\Grad School Doucments\08-Ongoing Research\Learning and Practice\Python Practice\Online Practice Course\python-practice-course"

#Execute updates
os.chdir(directory)
subprocess.run(["git", "add", "."])
subprocess.run(["git", "commit", "-m", message])
subprocess.run(["git", "push"])