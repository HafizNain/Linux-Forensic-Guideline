import os
import tkinter as tk
from tkinter import filedialog

#####################################################################
# Get Choice
#####################################################################

def getchoice():

    menu = """
These are some of the artifacts that can be extracted instantly!

1) OS Information
2) Network Configurations
3) Process Execution
4) Account and Group
5) Trash Bin
6) Deleted Data
7) Recently Used Application
8) Thumbnails
9) Important Logs
10) Basic Home Folders
11) Mozilla Browser Artifacts Path
12) Web Folder
0) Exit
"""
    print(menu)

    choice = input("Please enter your choice: ")

    match choice:
        case "1":
            getInfo()
        case "2":
            return 0
        case "3":
            getHistory()
        case "4":
            return 0
        case "5":
            return 0
        case "6":
            return 0
        case "7":
            return 0
        case "8":
            return 0
        case "9":
            return 0
        case "10":
            return 0
        case "11":
            return 0
        case "12":
            return 0
        case "0":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
    
    return choice

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
        else:
            targetPath = False
    
    bool(targetPath)
    if targetPath is False:
        with open("Bash History.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /home/user/._bashhistory")
        print("\nFile not found! Please do manual search!")
        return

    with open(targetPath, "r") as input:
        with open("Bash History.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile ._bashhistory extracted at: " + currentWorkingDirectory)

    return

#####################################################################
# OS Information
#####################################################################

def getInfo():

    usrDirectory = "usr"
    libDirectory = "lib"
    fileToSearch = "os-release"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(usrDirectory in dirs):
            firstLayer = os.path.join(rootDirectory,relPath,usrDirectory)
            break

    for relPath,dirs,files in os.walk(firstLayer):
        if(libDirectory in dirs):
            targetedLayer = os.path.join(firstLayer,relPath,libDirectory)
            break
    
    for relPath,dirs,files in os.walk(targetedLayer):
        if(fileToSearch in files):
            targetPath = os.path.join(targetedLayer,relPath,fileToSearch)
            break

    with open(targetPath, "r") as input:
        with open("os-release.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile os-release extracted at: " + currentWorkingDirectory)        
              
    return

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

choice = getchoice()

while(choice != 0):
    getchoice()
else:
    quit("Thank you for using Linux Artifacts Extraction Tool!")

#####################################################################
# END
#####################################################################