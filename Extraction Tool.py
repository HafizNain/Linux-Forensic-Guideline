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
            getUser()
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
            break
        else:
            targetPath = False
    
    bool(targetPath)
    if targetPath is False:
        with open("Bash History.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /home/user/._bashhistory")
        print("\nFile not found! Try search manually at: /home/user/._bashhistory")
        print("\nFile Process Execution extracted at: " + currentWorkingDirectory)
        return
    
    with open(targetPath, "r") as input:
        with open("Bash History.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile Process Execution extracted at: " + currentWorkingDirectory)

    return

#####################################################################
# OS Information
#####################################################################

def getInfo():

    usrDirectory = "usr"
    libDirectory = "lib"
    etcDirectory = "etc"
    osToSearch = "os-release"
    hostToSearch = "hostname"
    timeToSearch = "localtime"

    # os-release

    for relPath,dirs,files in os.walk(rootDirectory):
        if(usrDirectory in dirs):
            firstLayer = os.path.join(rootDirectory,relPath,usrDirectory)
            break

    for relPath,dirs,files in os.walk(firstLayer):
        if(libDirectory in dirs):
            targetedLayer = os.path.join(firstLayer,relPath,libDirectory)
            break
    
    for relPath,dirs,files in os.walk(targetedLayer):
        if(osToSearch in files):
            osPath = os.path.join(targetedLayer,relPath,osToSearch)
            break
        else:
            osPath = False
    
    bool(osPath)
    if osPath is False:
        with open("OS Information.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /usr/lib/os-release")
        print("\nFile not found! Try search manually at: /usr/lib/os-release")
        print("\nFile OS Information extracted at: " + currentWorkingDirectory)  
        return

    with open(osPath, "r") as input:
        with open("OS Information.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)
    
    # hostname

    for relPath,dirs,files in os.walk(rootDirectory):
        if(etcDirectory in dirs):
            targetDirectory = os.path.join(rootDirectory,relPath,etcDirectory)
            break
    
    for relPath,dirs,files in os.walk(targetDirectory):
        if(hostToSearch in files):
            hostPath = os.path.join(targetDirectory,relPath,hostToSearch)
            break
        else:
            hostPath = False
    
    bool(hostPath)
    if hostPath is False:
        with open("OS Information.txt", "a") as output:
            output.write("\n")
            output.write("File not found! Try search manually at: /etc/hostname")
        print("\nFile not found! Try search manually at: /etc/hostname")
        print("\nFile OS Information extracted at: " + currentWorkingDirectory)  
        return

    with open(hostPath, "r") as input:
        with open("OS Information.txt", "a") as output:
            output.write("Hostname= ")
            for line in input:
                output.write(line)

    # zoneinfo

    for relPath,dirs,files in os.walk(rootDirectory):
        if(etcDirectory in dirs):
            timeDirectory = os.path.join(rootDirectory,relPath,etcDirectory)
            break
    
    for relPath,dirs,files in os.walk(timeDirectory):
        if(timeToSearch in files):
            timePath = os.path.join(timeDirectory,relPath,timeToSearch)
            break
        else:
            timePath = False
    
    bool(timePath)
    if timePath is False:
        with open("OS Information.txt", "a") as output:
            output.write("\n")
            output.write("File not found! Try search manually at: /etc/localtime")
        print("\nFile not found! Try search manually at: /etc/localtime")
        print("\nFile OS Information extracted at: " + currentWorkingDirectory)  
        return

    with open(timePath, "r") as input:
        with open("OS Information.txt", "a") as output:
            output.write("Time Zone= ")
            for line in input:
                output.write(line)

    print("\nFile OS Information extracted at: " + currentWorkingDirectory)        
              
    return

#####################################################################
# Account and Group
#####################################################################

def getUser():

    etcDirectory = "etc"
    passwdToSearch = "passwd"
    groupToSearch = "group"

    # Users

    for relPath,dirs,files in os.walk(rootDirectory):
        if(etcDirectory in dirs):
            targetDirectory = os.path.join(rootDirectory,relPath,etcDirectory)
            break

    for relPath,dirs,files in os.walk(targetDirectory):
        if(passwdToSearch in files):
            passwdPath = os.path.join(targetDirectory,relPath,passwdToSearch)
            break
        else:
            passwdPath = False
    
    bool(passwdPath)
    if passwdPath is False:
        with open("Users.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /etc/passwd")
        print("\nFile not found! Try search manually at: /etc/passwd")
        print("\nFile User and Group extracted at: " + currentWorkingDirectory)
        return

    with open(passwdPath, "r") as input:
        with open("Users.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    # group

    for relPath,dirs,files in os.walk(rootDirectory):
        if(etcDirectory in dirs):
            targetDirectory = os.path.join(rootDirectory,relPath,etcDirectory)
            break

    for relPath,dirs,files in os.walk(targetDirectory):
        if(groupToSearch in files):
            groupPath = os.path.join(targetDirectory,relPath,groupToSearch)
            break
        else:
            groupPath = False
    
    bool(groupPath)
    if groupPath is False:
        with open("Groups.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /etc/group")
        print("\nFile not found! Try search manually at: /etc/group")
        print("\nFile User and Group extracted at: " + currentWorkingDirectory)
        return

    with open(groupPath, "r") as input:
        with open("Groups.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile User and Group extracted at: " + currentWorkingDirectory)
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