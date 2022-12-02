#####################################################################
# START
#####################################################################

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
2) Process Execution
3) Account and Group
4) Trash Bin
5) Deleted Data
6) Recently Used Application
7) Thumbnails
8) Important Logs
9) Basic Home Folders
10) Mozilla Browser Artifacts Path
11) Web Folder
12) All in one
0) Exit
"""
    print(menu)

    choice = input("Please enter your choice: ")

    match choice:
        case "1":
            getInfo()
        case "2":
            getHistory()
        case "3":
            getUser()
        case "4":
            getTrash()
        case "5":
            deletedData()
        case "6":
            recentlyUsed()
        case "7":
            getThumbnail()
        case "8":
            logs()
        case "9":
            homeFolder()
        case "10":
            getMozilla()
        case "11":
            getWebFolder()
        case "12":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
        case "0":
            quit("\nThank you for using Linux Artifacts Extraction Tool!\n")
    
    return choice

#####################################################################
# Get Bash History
#####################################################################

def getHistory():

    newFolder = "Process Execution"
    fileToSearch = ".bash_history"
    directoryToSearch = "home"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
        with open(path + "/Bash History.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /home/user/._bashhistory")
        print("\nFile not found! Try search manually at: /home/user/._bashhistory")
        print("\nFile Process Execution extracted at: " + path)
        return

    with open(targetPath, "r") as input:
        with open(path + "/Bash History.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile Process Execution extracted at: " + path)

    return

#####################################################################
# OS Information
#####################################################################

def getInfo():

    newFolder = "OS Information"
    usrDirectory = "usr"
    libDirectory = "lib"
    etcDirectory = "etc"
    osToSearch = "os-release"
    hostToSearch = "hostname"
    timeToSearch = "localtime"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
        with open(path + "\OS Information.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /usr/lib/os-release")
        print("\nFile not found! Try search manually at: /usr/lib/os-release")
        print("\nFile OS Information extracted at: " + path)  
        return

    with open(osPath, "r") as input:
        with open(path + "\OS Information.txt", "w") as output:
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
        with open(path + "\OS Information.txt", "a") as output:
            output.write("\n")
            output.write("File not found! Try search manually at: /etc/hostname")
        print("\nFile not found! Try search manually at: /etc/hostname")
        print("\nFile OS Information extracted at: " + path)  
        return

    with open(hostPath, "r") as input:
        with open(path + "\OS Information.txt", "a") as output:
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
        with open(path + "\OS Information.txt", "a") as output:
            output.write("\n")
            output.write("File not found! Try search manually at: /etc/localtime")
        print("\nFile not found! Try search manually at: /etc/localtime")
        print("\nFile OS Information extracted at: " + path)  
        return

    with open(timePath, "r") as input:
        with open(path + "\OS Information.txt", "a") as output:
            output.write("Time Zone= ")
            for line in input:
                output.write(line)

    print("\nFile OS Information extracted at: " + path)        
              
    return

#####################################################################
# Account and Group
#####################################################################

def getUser():

    newFolder = "User and Group"
    etcDirectory = "etc"
    passwdToSearch = "passwd"
    groupToSearch = "group"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
        with open(path + "/Users.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /etc/passwd")
        print("\nFile not found! Try search manually at: /etc/passwd")
        print("\nFile User and Group extracted at: " + path)
        return

    with open(passwdPath, "r") as input:
        with open(path + "/Users.txt", "w") as output:
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
        with open(path + "/Groups.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /etc/group")
        print("\nFile not found! Try search manually at: /etc/group")
        print("\nFile User and Group extracted at: " + path)
        return

    with open(groupPath, "r") as input:
        with open(path + "/Groups.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile User and Group extracted at: " + path)
    return

#####################################################################
# Recently Used Application
#####################################################################

def recentlyUsed():

    newFolder = "Recently Used Application"
    homeDirectory = "home"
    localDirectory = ".local"
    shareDirectory = "share"
    recentToSearch = "recently-used.xbel"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
        with open(path + "\Recently Used Application.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /home/.local/share")
        print("\nFile not found! Try search manually at: /home/.local/share")
        print("\nFile Recently Used Application extracted at: " + path)
        return
    
    with open(targetPath, "r") as input:
        with open(path + "\Recently Used Application.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile Recently Used Application extracted at: " + path)

    return
#####################################################################
# Important Logs
#####################################################################

def logs():
     
    newFolder = "Important Logs"
    varDirectory = "var"
    logDirectory = "log"
    authToSearch = "auth.log"
    sysToSearch = "syslog"
    
    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
        with open(path + "\AuthLog.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /var/log")
        print("\nFile not found! Try search manually at: /var/log")
        print("\nFile Important Logs extracted at: " + path)
        return
    
    with open(targetPath, "r") as input:
        with open(path + "\AuthLog.txt", "w") as output:
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
        with open(path + "\syslog.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n")
            output.write("File not found! Try search manually at: /var/log")
        print("\nFile not found! Try search manually at: /var/log")
        print("\nFile Important Logs extracted at: " + path)
        return
    
    with open(targetPath, "r", errors="ignore") as input:
        with open(path + "\sys.txt", "w") as output:
            output.write("Extracted from mount point: " + rootDirectory + "\n\n")
            for line in input:
                output.write(line)

    print("\nFile Important Logs extracted at: " + path)
    return

#####################################################################
# Trash Bin
#####################################################################

def getTrash():

    newFolder = "Trash Bin"
    homeDirectory = "home"
    localDirectory = ".local"
    shareDirectory = "share"
    trashDirectory = "Trash"
    expungedFolder = "expunged"
    filesFolder = "files"
    infoFolder = "info"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)


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
    
    with open(path + "\Files.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(trash))
    
    # expunged
    for relPath,dirs,files in os.walk(lastDirectory):
        if(expungedFolder in dirs):
            expungedFiles = os.path.join(lastDirectory,relPath,expungedFolder)
            expunged = os.listdir(expungedFiles)
            break
    
    with open(path + "\expunged.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(expunged))
    
    # info
    for relPath,dirs,files in os.walk(lastDirectory):
        if(infoFolder in dirs):
            infoFiles = os.path.join(lastDirectory,relPath,infoFolder)
            info = os.listdir(infoFiles)
            break
    
    with open(path + "\info.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(info))
    
    print("\nFile Trash Bin extracted at: " + path)
    return

#####################################################################
# Deleted Data
#####################################################################

def deletedData():

    newFolder = "Deleted Data"
    lostFoundDirectory = "lost+found"
    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

    for relPath,dirs,files in os.walk(rootDirectory):
        if(lostFoundDirectory in dirs):
            lostfoundFiles = os.path.join(rootDirectory,relPath,lostFoundDirectory)
            lostfound = os.listdir(lostfoundFiles)
            break
    
    with open(path + "\lost+found.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(lostfound))

    print("\nFile Deleted Data extracted at: " + path)
    return

#####################################################################
# Thumbnails
#####################################################################

def getThumbnail():

    newFolder = "Thumbails"
    homeDirectory = "home"
    cacheDirectory = ".cache"
    thumbDirectory = "thumbnails"
    failFolder = "fail"
    largeFolder = "large"
    normalFolder = "normal"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
    
    with open(path + "\large.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(large))
    
    # normal

    for relPath,dirs,files in os.walk(lastDirectory):
        if(normalFolder in dirs):
            normalFiles = os.path.join(lastDirectory,relPath,normalFolder)
            normal = os.listdir(normalFiles)
            break
    
    with open(path + "\ normal.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(normal))
    
    # fail

    for relPath,dirs,files in os.walk(lastDirectory):
        if(failFolder in dirs):
            failFiles = os.path.join(lastDirectory,relPath,failFolder)
            fail = os.listdir(failFiles)
            break
    
    with open(path + "\Fail.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(fail))

    print("\nFile Thumbnails extracted at: " + path)
    return

#####################################################################
# Web Folder
#####################################################################

def getWebFolder():

    newFolder = "Web Folder"
    varDirectory = "var"
    wwwDirectory = "www"
    htmlDirectory = "html"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
    
    with open(path + "\html.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(html))

    print("\nFile Web Folder extracted at: " + path)
    return

#####################################################################
# Mozilla Browser Artifacts
#####################################################################

def getMozilla():

    newFolder = "Mozilla Browser Artifact"
    homeDirectory = "home"
    mozillaDirectory = ".mozilla"
    firefoxDirectory = "firefox"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

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
    
    with open(path + "\Mozilla.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(firefox))


    print("\nFile Mozilla Browser Artifact extracted at: " + path)
    return

#####################################################################
# Basic Home Folders
#####################################################################

def homeFolder():

    newFolder = "Basic Home Folders"
    homeDirectory = "home"
    desktopDirectory = "Desktop"
    docDirectory = "Documents"
    downloadDirectory = "Downloads"
    musicDirectory = "Music"
    picDirectory = "Pictures"
    vidDirectory = "Videos"

    path = os.path.join(mainFolder,newFolder)
    os.mkdir(path)

    for relPath,dirs,files in os.walk(rootDirectory):
        if(homeDirectory in dirs):
            targetDirectory = os.path.join(rootDirectory,relPath,homeDirectory)
            break
    
    # Desktop

    for relPath,dirs,files in os.walk(targetDirectory):
        if(desktopDirectory in dirs):
            desktopFiles = os.path.join(targetDirectory,relPath,desktopDirectory)
            desktop = os.listdir(desktopFiles)
            break
    
    with open(path + "\desktop.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(desktop))
    
    # Documents

    for relPath,dirs,files in os.walk(targetDirectory):
        if(docDirectory in dirs):
            docFiles = os.path.join(targetDirectory,relPath,docDirectory)
            doc = os.listdir(docFiles)
            break
    
    with open(path + "\documents.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(doc))

    # Download

    for relPath,dirs,files in os.walk(targetDirectory):
        if(downloadDirectory in dirs):
            downloadFiles = os.path.join(targetDirectory,relPath,downloadDirectory)
            download = os.listdir(downloadFiles)
            break
    
    with open(path + "\download.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(download))
    
    # Music

    for relPath,dirs,files in os.walk(targetDirectory):
        if(musicDirectory in dirs):
            musicFiles = os.path.join(targetDirectory,relPath,musicDirectory)
            music = os.listdir(musicFiles)
            break
    
    with open(path + "\music.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(music))
    
    # Pictures

    for relPath,dirs,files in os.walk(targetDirectory):
        if(picDirectory in dirs):
            picFiles = os.path.join(targetDirectory,relPath,picDirectory)
            pic = os.listdir(picFiles)
            break
    
    with open(path + "\pictures.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(pic))
    
    # Videos

    for relPath,dirs,files in os.walk(targetDirectory):
        if(vidDirectory in dirs):
            vidFiles = os.path.join(targetDirectory,relPath,vidDirectory)
            vid = os.listdir(vidFiles)
            break
    
    with open(path + "\Videos.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(vid))

    print("\nFile Basic Home Folders extracted at: " + path)        
    return

#####################################################################
# Main Program
#####################################################################

print("\nWelcome! Thank you for using Linux Artifacts Extraction Tool!\n")
print("\nPlease enter the location path for the mounted image: \n")

root = tk.Tk()
root.withdraw()

folderName = "Linux Extraction Tool Acquisition Result"

currentWorkingDirectory = os.getcwd()
rootDirectory = filedialog.askdirectory()

mainFolder = os.path.join(currentWorkingDirectory,folderName)
os.mkdir(mainFolder)

if (rootDirectory == ""):
    quit("Thank you for using Linux Artifacts Extraction Tool!")

choice = getchoice()

while(choice != 0):
    getchoice()

#####################################################################
# END
#####################################################################