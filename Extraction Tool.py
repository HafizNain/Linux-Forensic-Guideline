#####################################################################
# START
#####################################################################

import os
import shutil
import customtkinter
from tkinter import messagebox
from tkinter import filedialog
from datetime import datetime

#####################################################################
# Get Bash History
#####################################################################

def getHistory():

    newFolder = "Process Execution"
    fileToSearch = ".bash_history"
    directoryToSearch = "home"

    path = os.path.join(mainFolder,newFolder)

    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    messagebox.showinfo("Info", "File Process Execution extracted at: " + path) 

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

    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    messagebox.showinfo("Info", "File OS Information extracted at: " + path)        
              
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
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    messagebox.showinfo("Info", "File User and Group extracted at: " + path)
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
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    messagebox.showinfo("Info", "File Recently Used Application extracted at: " + path)

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
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    messagebox.showinfo("Info", "File Important Logs extracted at: " + path)
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
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    shutil.copytree(lastDirectory, path, dirs_exist_ok=True)
    
    messagebox.showinfo("Info", "File Trash Bin extracted at: " + path)
    return

#####################################################################
# Deleted Data
#####################################################################

def deletedData():

    newFolder = "Deleted Data"
    lostFoundDirectory = "lost+found"

    path = os.path.join(mainFolder,newFolder)
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
        os.mkdir(path)

    for relPath,dirs,files in os.walk(rootDirectory):
        if(lostFoundDirectory in dirs):
            lostfoundFiles = os.path.join(rootDirectory,relPath,lostFoundDirectory)
            lostfound = os.listdir(lostfoundFiles)
            break
    
    with open(path + "\lost+found.txt", "w") as output:
        output.write("Extracted from mount point: " + rootDirectory + "\n\n")
        output.write('\n'.join(lostfound))

    shutil.copytree(lostfoundFiles, path, dirs_exist_ok=True)

    messagebox.showinfo("Info", "File Deleted Data extracted at: " + path)
    return

#####################################################################
# Thumbnails
#####################################################################

def getThumbnail():

    newFolder = "Thumbnails"
    homeDirectory = "home"
    cacheDirectory = ".cache"
    thumbDirectory = "thumbnails"
    failFolder = "fail"
    largeFolder = "large"
    normalFolder = "normal"

    path = os.path.join(mainFolder,newFolder)
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    shutil.copytree(lastDirectory, path, dirs_exist_ok=True)

    messagebox.showinfo("Info", "File Thumbnails extracted at: " + path)
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
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    shutil.copytree(htmlFiles, path, dirs_exist_ok=True)

    messagebox.showinfo("Info", "File Web Folder extracted at: " + path)
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
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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

    messagebox.showinfo("Info", "File Mozilla Browser Artifact extracted at: " + path)
    return

#####################################################################
# Basic Home Folders
#####################################################################

def homeFolder():

    newFolder = "Basic Home Folders"
    desktopFolder = "Desktop"
    docFolder = "Documents"
    downloadFolder = "Downloads"
    musicFolder = "Music"
    picFolder = "Pictures"
    vidFolder = "Videos"
    homeDirectory = "home"
    desktopDirectory = "Desktop"
    docDirectory = "Documents"
    downloadDirectory = "Downloads"
    musicDirectory = "Music"
    picDirectory = "Pictures"
    vidDirectory = "Videos"

    path = os.path.join(mainFolder,newFolder)
    
    if os.path.exists(path):
        messagebox.showinfo("Info", "Folder already exists at: " + path)
        return
    else: 
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


    newPath = path
    newPath = os.path.join(path,desktopFolder)
    os.mkdir(newPath)
    shutil.copytree(desktopFiles, newPath, dirs_exist_ok=True)

    newPath = path
    newPath = os.path.join(path,docFolder)
    os.mkdir(newPath)
    shutil.copytree(docFiles, newPath, dirs_exist_ok=True)

    newPath = path
    newPath = os.path.join(path,downloadFolder)
    os.mkdir(newPath)
    shutil.copytree(downloadFiles, newPath, dirs_exist_ok=True)

    newPath = path
    newPath = os.path.join(path,musicFolder)
    os.mkdir(newPath)
    shutil.copytree(musicFiles, newPath, dirs_exist_ok=True)

    newPath = path
    newPath = os.path.join(path,picFolder)
    os.mkdir(newPath)
    shutil.copytree(picFiles, newPath, dirs_exist_ok=True)

    newPath = path
    newPath = os.path.join(path,vidFolder)
    os.mkdir(newPath)
    shutil.copytree(vidFiles, newPath, dirs_exist_ok=True)
 
    messagebox.showinfo("Info", "File Basic Home Folders extracted at: " + path)      
    return

#####################################################################
# Get Directory
#####################################################################

def getDirectory():

    global currentWorkingDirectory
    global rootDirectory
    global mainFolder

    currentWorkingDirectory_global = os.getcwd()
    rootDirectory_global = filedialog.askdirectory()

    dateName = datetime.now().strftime("%Y_%m_%d_%H_%M_%S")
    folderName = "Linux Extraction Tool Acquisition Result"

    combinedName = os.path.join(currentWorkingDirectory_global,dateName)
    os.mkdir(combinedName)
    mainFolder_global = os.path.join(combinedName,folderName)
    os.mkdir(mainFolder_global)

    if (rootDirectory_global == ""):
        exit()

    currentWorkingDirectory = currentWorkingDirectory_global
    rootDirectory = rootDirectory_global
    mainFolder = mainFolder_global

    return menu()

#####################################################################
# Main Menu
#####################################################################

def menu():
    frame.pack_forget()

    main_frame = customtkinter.CTkFrame(master=root)
    main_frame.pack(pady=20, padx=60, fill="both", expand=True)

    label = customtkinter.CTkLabel(master=main_frame, text="Main Menu")
    label.pack(pady=12, padx=10)

    button_frame = customtkinter.CTkFrame(master=main_frame)
    button_frame.pack(pady=12, padx=10)

    buttons = [
        customtkinter.CTkButton(master=button_frame, text="OS Information", command=getInfo),
        customtkinter.CTkButton(master=button_frame, text="Process Execution", command=getHistory),
        customtkinter.CTkButton(master=button_frame, text="Account and Group", command=getUser),
        customtkinter.CTkButton(master=button_frame, text="Trash Bin", command=getTrash),
        customtkinter.CTkButton(master=button_frame, text="Deleted Data", command=deletedData),
        customtkinter.CTkButton(master=button_frame, text="Recently Used Application", command=recentlyUsed),
        customtkinter.CTkButton(master=button_frame, text="Thumbnails", command=getThumbnail),
        customtkinter.CTkButton(master=button_frame, text="Important Logs", command=logs),
        customtkinter.CTkButton(master=button_frame, text="Basic Home Folders", command=homeFolder),
        customtkinter.CTkButton(master=button_frame, text="Mozilla Browser Artifacts", command=getMozilla),
        customtkinter.CTkButton(master=button_frame, text="Web Folder", command=getWebFolder),
        customtkinter.CTkButton(master=button_frame, text="Exit", command=exit),
    ]

    for i, button in enumerate(buttons):
        button.grid(row=i // 2, column=i % 2, padx=10, pady=20)

    root.mainloop()

    return


#####################################################################
# Exit Function
#####################################################################

def exit():

    messagebox.showinfo("Info", "Thank you for using Linux Extraction Tool!") 
    root.destroy()

    return

#####################################################################
# Startup
#####################################################################

customtkinter.set_appearance_mode("dark")
customtkinter.set_default_color_theme("dark-blue")

root = customtkinter.CTk()
root.title("Linux Artifacts Extraction Tool")
root.geometry("900x550")

frame = customtkinter.CTkFrame(master=root)
frame.pack(pady=20, padx=60, fill="both", expand=True)

label = customtkinter.CTkLabel(master=frame, text="Linux Artifacts Extraction Tool", font=("Helvetica", 24))
label.pack(pady=12, padx=10, anchor="center")

label = customtkinter.CTkLabel(master=frame, text="Discover the power of efficient forensic investigation with our Linux Forensic Analysis tool", font=("Helvetica", 16))
label.pack(pady=12, padx=10, anchor="center")

center_frame = customtkinter.CTkFrame(master=root)
center_frame.place(relx=0.5, rely=0.5, anchor="center")

label = customtkinter.CTkLabel(master=center_frame, text="Please enter the location path for the mounted image:", font=("Helvetica", 16))
label.pack(pady=12, padx=10, anchor="center")

button_frame = customtkinter.CTkFrame(master=center_frame)
button_frame.pack(pady=12, padx=10, anchor="center")

path_label = customtkinter.CTkLabel(master=button_frame, text=" No directory selected", font=("Helvetica", 16))
path_label.pack(side="left")

button = customtkinter.CTkButton(master=button_frame, text="Choose Directory", command=getDirectory, font=("Helvetica", 16))
button.pack(side="left", padx=10)

root.mainloop()

#####################################################################
# END
#####################################################################