import os
import tkinter as tk
from tkinter import filedialog

#####################################################################
# Get Choice
#####################################################################

def getchoice():

    menu = """
These are some of the artifacts that can be extracted instantly!

1. Bash History
2. Trash Bin
3. Recently Used Application
4. Users
0. Exit
"""
    print(menu)

    choice = input("Please enter your choice: ")

    match choice:
        case "1":
            getHistory()
        case "2":
            getHistory()
        case "3":
            getHistory()
        case "4":
            getHistory()
        case "0":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")

#####################################################################
# Get Bash History
#####################################################################

def getHistory():

    fileToSearch = ".bash_history"
    directoryToSearch = "home"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(directoryToSearch in dirs):
            targetDirectory = os.path.join(rootDirectory,relPath,directoryToSearch)
            break

    for relPath,dirs,files in os.walk(targetDirectory):
        if(fileToSearch in files):
            targetPath = os.path.join(targetDirectory,relPath,fileToSearch)
            with open(targetPath, "r") as input:
                with open("Bash History.txt", "w") as output:
                    for line in input:
                        output.write(line)
    print("\nBash History.txt extracted at: " + currentWorkingDirectory)
    return getchoice()

#####################################################################
# Main Program
#####################################################################

print("\nWelcome! Thank you for using Linux Artifacts Extraction Tool!\n")
print("\nPlease enter the location path for the mounted image: \n")

root = tk.Tk()
root.withdraw()

currentWorkingDirectory = os.getcwd()
rootDirectory = filedialog.askdirectory()
# dirList = os.listdir(targetDirectory)

# print("Current working directory is: " + currentWorkingDirectory)
# print("Root directory for the mounted image is: " + rootDirectory)
# print(dirList)

getchoice()

#####################################################################
# END
#####################################################################