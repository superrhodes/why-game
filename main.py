from tkinter import *
import tkinter.messagebox as box
import threading
from sys import exit

def runGame():
    cfg.close()
    root.withdraw()
    import game
    box.showerror("Death", "You have died!")
    exit()

def settingsOption():
    mainFrame.pack_forget()

    if ss == 0:
        smbtn.config(state = DISABLED)
    else:
        labtn.config(state = DISABLED)

    if lf == 0:
        fpsl.deselect()
    else:
        fpsl.select()

    if ms == 0:
        slbtn.config(state = DISABLED)
    else:
        fabtn.config(state = DISABLED)   

    settingsFrame.pack()

def back():
    settingsFrame.pack_forget()
    mainFrame.pack()

def creditBox():
    root.withdraw()
    box.showinfo("credits", "This game was made by Johnathan.")
    root.deiconify()

def frlock(fpsl):
    global lf
    fpsl.flash()

    if lf == 0:
        lf = 1
    else:
        lf = 0

def ssize(btns, nbtns):
    global ss
    btns.flash()
    btns.config(state = DISABLED)
    nbtns.config(state = ACTIVE)

    if ss == 0:
        ss = 1
    else:
        ss = 0

def mspeed(btns, nbtns):
    global ms
    btns.flash()
    btns.config(state = DISABLED)
    nbtns.config(state = ACTIVE)

    if ms == 0:
        ms = 1
    else:
        ms = 0
    
def save(btns):
    global cfg
    btns.flash()
    cfg.truncate(0)
    cfg.write(str(ss)+"\n"+str(lf)+"\n"+str(ms)+"\n")
    cfg.close()
    cfg = open("configure.cfg", mode = 'r+')
    cfg.truncate(0)
    cfg.write(str(ss)+"\n"+str(lf)+"\n"+str(ms)+"\n")
    cfg.close()
    cfg = open("configure.cfg", mode = 'r+')
    box.showinfo("Saved", "Your changes have been saved.")


w = 250
h = 200

cfg = open("configure.cfg", mode = 'r+')
values = cfg.readlines()

ss = int((values[0])[0])
lf = int((values[1])[0])
ms = int((values[2])[0])

root = Tk()
root.title("A terrible game")
icon = PhotoImage(file = "assets/button1.png")
root.iconphoto(False, icon)

ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()

x = (ws/2) - (w/2)
y = (hs/2) - (h/2)

root.geometry('%dx%d+%d+%d' % (w, h, x, y))

mainFrame = Frame(root, width = 300, height = 200)
mainFrame.pack()
titlelbl = Label(mainFrame, text = "This Game Sucks!")
playbtn = Button(mainFrame, text = "Play Game", command = lambda:runGame())
settingsbtn = Button(mainFrame, text = "Settings", command = lambda:settingsOption())
creditsbtn = Button(mainFrame, text = "Credits", command = lambda:creditBox())
exitbtn = Button(mainFrame, text = "Quit", command = lambda:exit())

titlelbl.pack()
playbtn.pack()
settingsbtn.pack()
creditsbtn.pack()
exitbtn.pack()

settingsFrame = Frame(root, width = 300, height = 200)
sslbl = Label(settingsFrame, text = "Sceen size:")
smbtn = Button(settingsFrame, text = "Small", anchor = E, command = lambda:ssize(smbtn, labtn))
labtn = Button(settingsFrame, text = "Big", anchor = W, command = lambda:ssize(labtn, smbtn))

if ss == 0:
    smbtn.config(state = DISABLED)
else:
    labtn.config(state = DISABLED)

fpsl = Checkbutton(settingsFrame, text = "Lock framerate:", onvalue = 1, offvalue = 0, command = lambda:frlock(fpsl))

if lf == 0:
    fpsl.deselect()
else:
    fpsl.select()

mslbl = Label(settingsFrame, text = "Movement Speed:")
slbtn = Button(settingsFrame, text = "Slow", anchor = E, command = lambda:mspeed(slbtn, fabtn))
fabtn = Button(settingsFrame, text = "Fast", anchor = W, command = lambda:mspeed(fabtn, slbtn))

if ms == 0:
    slbtn.config(state = DISABLED)
else:
    fabtn.config(state = DISABLED)

sep = Label(settingsFrame, text = "________________________________")

sbtn = Button(settingsFrame, text = "Save", command = lambda:save(sbtn))
bbtn = Button(settingsFrame, text = "Exit", command = lambda:back())

sslbl.grid(row = 1, column = 1, columnspan = 4)
smbtn.grid(row = 2, column = 1, columnspan = 2)
labtn.grid(row = 2, column = 3, columnspan = 2)
fpsl.grid(row = 3, column = 1, columnspan = 4)
mslbl.grid(row = 4, column = 1, columnspan = 4)
slbtn.grid(row = 5, column = 1, columnspan = 2)
fabtn.grid(row = 5, column = 3,columnspan = 2)
sep.grid(row = 6, column = 1, columnspan = 4)
sbtn.grid(row = 7, column = 1, columnspan = 2)
bbtn.grid(row = 7, column = 3, columnspan = 2)

root.mainloop()