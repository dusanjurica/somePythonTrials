'''
Created on Dec 15, 2017

@author: juricdu
'''

from tkinter import *
from sources.functions import *


mainWindow = Tk()

mainWindow.title("Configuration thingy")

if __name__ == '__main__':
    print ("debug info {}".format(__name__))
    
    btn01 = Button(mainWindow, text='sample text', padx=3, pady=2)
    
    menuStrip = Menu(mainWindow)
    fileMenu = Menu(menuStrip, tearoff=0)
    editMenu = Menu(menuStrip, tearoff=0)
    
    fileMenu.add_command(label="Don't do a thing")
    fileMenu.add_command(label="Exit", command=mainWindow.quit)
    
    editMenu.add_command(label="Publish configuration", command=commPublish)
    editMenu.add_separator()
    editMenu.add_command(label="Repair configuration", command=commRepair)
    
    menuStrip.add_cascade(label="File", menu=fileMenu)
    menuStrip.add_cascade(label="Operations", menu=editMenu)
    
    btn01.grid(row=0, column=0)
    mainWindow.geometry("800x600")
    mainWindow.config(menu=menuStrip)
    mainWindow.mainloop()