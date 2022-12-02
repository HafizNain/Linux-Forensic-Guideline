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
13) All in one
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
            getTrash()
        case "6":
            deletedData()
        case "7":
            recentlyUsed()
        case "8":
            getThumbnail()
        case "9":
            logs()
        case "10":
            return 0
        case "11":
            getMozilla()
        case "12":
            getWebFolder()
        case "13":
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
# Recently Used Application
#####################################################################

def recentlyUsed():

    homeDirectory = "home"
    localDirectory = ".local"
    shareDirectory = "share"
    recentToSearch = "recently-used.xbel"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(homeDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,homeDirectory)
            break
    
    for relPath,dirs,files in os.walk(firstDirectory):
        if(localDirectory in dirs):
            secDirectory = os.path.join(rootDirectory,relPath,localDirectory)
            break
    
    for relPath,dirs,files in os.walk(secDirectory):
        if(shareDirectory in dirs):
            targetDirectory = os.path.join(rootDirectory,relPath,shareDirectory)
            break

    for relPath,dirs,files in os.walk(targetDirectory):
        if(recentToSearch in files):
            targetPath = os.path.join(targetDirectory,relPath,recentToSearch)
            break
        else:
            targetPath = False
    
    bool(targetPath)
    if targetPath is False:
        with open("Recently Used Application.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /home/.local/share")
        print("\nFile not found! Try search manually at: /home/.local/share")
        print("\nFile Recently Used Application extracted at: " + currentWorkingDirectory)
        return
    
    with open(targetPath, "r") as input:
        with open("Recently Used Application.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile Recently Used Application extracted at: " + currentWorkingDirectory)

    return
#####################################################################
# Important Logs
#####################################################################

def logs():
     
    varDirectory = "var"
    logDirectory = "log"
    authToSearch = "auth.log"
    sysToSearch = "syslog"
     
    # auth.log

    for relPath,dirs,files in os.walk(rootDirectory):
        if(varDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,varDirectory)
            break

    for relPath,dirs,files in os.walk(firstDirectory):
        if(logDirectory in dirs):
            targetDirectory = os.path.join(firstDirectory,relPath,logDirectory)
            break
    
    for relPath,dirs,files in os.walk(targetDirectory):
        if(authToSearch in files):
            targetPath = os.path.join(targetDirectory,relPath,authToSearch)
            break
        else:
            targetPath = False
    
    bool(targetPath)
    if targetPath is False:
        with open("authLog.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /var/log")
        print("\nFile not found! Try search manually at: /var/log")
        print("\nFile Important Logs extracted at: " + currentWorkingDirectory)
        return
    
    with open(targetPath, "r") as input:
        with open("authLog.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)
    
    # syslog

    for relPath,dirs,files in os.walk(rootDirectory):
        if(varDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,varDirectory)
            break

    for relPath,dirs,files in os.walk(firstDirectory):
        if(logDirectory in dirs):
            targetDirectory = os.path.join(firstDirectory,relPath,logDirectory)
            break
    
    for relPath,dirs,files in os.walk(targetDirectory):
        if(sysToSearch in files):
            targetPath = os.path.join(targetDirectory,relPath,sysToSearch)
            break
        else:
            targetPath = False
    
    bool(targetPath)
    if targetPath is False:
        with open("syslog.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /var/log")
        print("\nFile not found! Try search manually at: /var/log")
        print("\nFile Important Logs extracted at: " + currentWorkingDirectory)
        return
    
    with open(targetPath, "r", errors="ignore") as input:
        with open("sys.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile Important Logs extracted at: " + currentWorkingDirectory)
    return

#####################################################################
# Trash Bin
#####################################################################

def getTrash():

    homeDirectory = "home"
    localDirectory = ".local"
    shareDirectory = "share"
    trashDirectory = "Trash"
    expungedFolder = "expunged"
    filesFolder = "files"
    infoFolder = "info"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(homeDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,homeDirectory)
            break

    for relPath,dirs,files in os.walk(firstDirectory):
        if(localDirectory in dirs):
            secDirectory = os.path.join(firstDirectory,relPath,localDirectory)
            break

    for relPath,dirs,files in os.walk(secDirectory):
        if(shareDirectory in dirs):
            thirdDirectory = os.path.join(secDirectory,relPath,shareDirectory)
            break
    
    for relPath,dirs,files in os.walk(thirdDirectory):
        if(trashDirectory in dirs):
            lastDirectory = os.path.join(thirdDirectory,relPath,trashDirectory)
            break
    
    # files
    for relPath,dirs,files in os.walk(lastDirectory):
        if(filesFolder in dirs):
            trashFiles = os.path.join(lastDirectory,relPath,filesFolder)
            trash = os.listdir(trashFiles)
            break
    
    with open("files.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(trash))
    
    # expunged
    for relPath,dirs,files in os.walk(lastDirectory):
        if(expungedFolder in dirs):
            expungedFiles = os.path.join(lastDirectory,relPath,expungedFolder)
            expunged = os.listdir(expungedFiles)
            break
    
    with open("expunged.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(expunged))
    
    # info
    for relPath,dirs,files in os.walk(lastDirectory):
        if(infoFolder in dirs):
            infoFiles = os.path.join(lastDirectory,relPath,infoFolder)
            info = os.listdir(infoFiles)
            break
    
    with open("info.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(info))
    
    print("\nFile Trash Bin extracted at: " + currentWorkingDirectory)
    return

#####################################################################
# Deleted Data
#####################################################################

def deletedData():

    lostFoundDirectory = "lost+found"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(lostFoundDirectory in dirs):
            lostfoundFiles = os.path.join(rootDirectory,relPath,lostFoundDirectory)
            lostfound = os.listdir(lostfoundFiles)
            break
    
    with open("lost+found.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(lostfound))

    print("\nFile Deleted Data extracted at: " + currentWorkingDirectory)
    return

#####################################################################
# Thumbnails
#####################################################################

def getThumbnail():

    homeDirectory = "home"
    cacheDirectory = ".cache"
    thumbDirectory = "thumbnails"
    failFolder = "fail"
    largeFolder = "large"
    normalFolder = "normal"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(homeDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,homeDirectory)
            break
    
    for relPath,dirs,files in os.walk(firstDirectory):
        if(cacheDirectory in dirs):
            secDirectory = os.path.join(firstDirectory,relPath,cacheDirectory)
            break
    
    for relPath,dirs,files in os.walk(secDirectory):
        if(thumbDirectory in dirs):
            lastDirectory = os.path.join(secDirectory,relPath,thumbDirectory)
            break

    # large

    for relPath,dirs,files in os.walk(lastDirectory):
        if(largeFolder in dirs):
            largeFiles = os.path.join(lastDirectory,relPath,largeFolder)
            large = os.listdir(largeFiles)
            break
    
    with open("large.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(large))
    
    # normal

    for relPath,dirs,files in os.walk(lastDirectory):
        if(normalFolder in dirs):
            normalFiles = os.path.join(lastDirectory,relPath,normalFolder)
            normal = os.listdir(normalFiles)
            break
    
    with open("normal.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(normal))
    
    # fail

    for relPath,dirs,files in os.walk(lastDirectory):
        if(failFolder in dirs):
            failFiles = os.path.join(lastDirectory,relPath,failFolder)
            fail = os.listdir(failFiles)
            break
    
    with open("fail.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(fail))

    print("\nFile Thumbnails extracted at: " + currentWorkingDirectory)
    return

#####################################################################
# Web Folder
#####################################################################

def getWebFolder():

    varDirectory = "var"
    wwwDirectory = "www"
    htmlDirectory = "html"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(varDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,varDirectory)
            break
    
    for relPath,dirs,files in os.walk(firstDirectory):
        if(wwwDirectory in dirs):
            lastDirectory = os.path.join(firstDirectory,relPath,wwwDirectory)
            break
    
    for relPath,dirs,files in os.walk(lastDirectory):
        if(htmlDirectory in dirs):
            htmlFiles = os.path.join(lastDirectory,relPath,htmlDirectory)
            html = os.listdir(htmlFiles)
            break
    
    with open("html.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(html))

    print("\nFile Web Folder extracted at: " + currentWorkingDirectory)
    return

#####################################################################
# Mozilla Browser Artifacts
#####################################################################

def getMozilla():

    homeDirectory = "home"
    mozillaDirectory = ".mozilla"
    firefoxDirectory = "firefox"

    for relPath,dirs,files in os.walk(rootDirectory):
        if(homeDirectory in dirs):
            firstDirectory = os.path.join(rootDirectory,relPath,homeDirectory)
            break
    
    for relPath,dirs,files in os.walk(firstDirectory):
        if(mozillaDirectory in dirs):
            lastDirectory = os.path.join(firstDirectory,relPath,mozillaDirectory)
            break
    
    for relPath,dirs,files in os.walk(lastDirectory):
        if(firefoxDirectory in dirs):
            firefoxFiles = os.path.join(lastDirectory,relPath,firefoxDirectory)
            firefox = os.listdir(firefoxFiles)
            break
    
    with open("Mozilla.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(firefox))


    print("\nFile Mozilla Browser Artifact extracted at: " + currentWorkingDirectory)
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

choice = getchoice()

while(choice != 0):
    getchoice()
else:
    quit("Thank you for using Linux Artifacts Extraction Tool!")

#####################################################################
# END
#####################################################################