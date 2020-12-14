
import tkinter
import os
from tkinter import filedialog

root = tkinter.Tk()
root.withdraw() #use to hide tkinter window

def search_for_file_path ():
    currdir = os.getcwd()
    tempdir = filedialog.askopenfilename(parent=root, initialdir=currdir, title='Please select a directory')
    filename = os.path.basename(tempdir)

    if len(tempdir) > 0:
        print ("You chose: %s" % tempdir)
        print("Filename : %s" % filename)
    return tempdir



