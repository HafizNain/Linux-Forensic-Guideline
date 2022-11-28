import os
import tkinter as tk
from tkinter import filedialog

root = tk.Tk()
root.withdraw()

targetDirectory = filedialog.askopenfilename()
currentDirectory = os.getcwd()

print("Current working directory is: " + currentDirectory)
print("Targeted directory is: " + targetDirectory)

