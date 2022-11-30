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
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "2":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "3":
            getHistory()
        case "4":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "5":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "6":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "7":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "8":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "9":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "10":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "11":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "12":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
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
                    output.write("Extracted from mount point: " + rootDirectory + "\n\n")
                    for line in input:
                        output.write(line)
                    print("\nBash History.txt extracted at: " + currentWorkingDirectory)
       
    return getchoice()

#####################################################################
# Change Mount Point
#####################################################################



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