Linux Artifacts Extraction Tool by Muhammad Zul Akmal Bin Shafiee

List of Artifacts:

1) OS Information (hostname, os-release, zoneinfo)
2) Network Configurations (KIV)
3) Process Execution (.bash_history)
4) Account and Group (passwd, shadow, sudoers) /etc
5) Trash Bin (expunged, files, info)- ~/.local/share/trash/.
6) Deleted Data (lost+found)
7) Recently Used Application (recently-used.xbel) - ~/.local/share/
8) Thumbnails (fail, large, normal) - ~/.cache/thumbnails/.
9) Important Logs (auth.log, dpkg.log, sys.log)
10) Basic Home Folders (Desktops, Documents, Downloads, Music, Pictures, Videos)
11) Mozilla Browser Artifacts Path - (home.mozilla)
12) Web Folder (var/www/html)

Things left to do:

1) Function 2,8,10,11,12
2) Creating a folder for each class of artifacts
3) Finding necessary artfiacts for network
4) Creating nested function for error handling in OS information