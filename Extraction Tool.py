import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

currentWorkingDirectory = os.getcwd()
rootDirectory = filedialog.askdirectory()
# dirList = os.listdir(targetDirectory)

print("Current working directory is: " + currentWorkingDirectory)
print("Root directory for the mounted image is: " + rootDirectory)
# print(dirList)


#####################################################################
# Get Bash History
#####################################################################
fileToSearch = ".bash_history"

for relPath,dirs,files in os.walk(rootDirectory):
    if(fileToSearch in files):
        targetPath = os.path.join(rootDirectory,relPath,fileToSearch)
        print("Bash History is at: " + targetPath)
        with open(targetPath, "r") as input:
            with open("Bash History.txt", "w") as output:
                for line in input:
                    output.write(line)
