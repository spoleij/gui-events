from itertools import count
import tkinter
import random
window = tkinter.Tk()

window.title("Clicker")
window.configure(bg='grey')
window.resizable(False, False)
window.geometry('300x150')

countNumber = 0
prevColor = 'grey'
prevButton = None

def addOne():
    global countNumber
    global prevButton
    countNumber += 1
    intVar.set(countNumber)
    prevButton = button1
    checkCount()

def subtractOne():
    global countNumber
    global prevButton
    countNumber -= 1
    intVar.set(countNumber)
    prevButton = button2
    checkCount()

def checkCount():
    global prevColor
    if countNumber == 0:
        window.configure(bg='grey')
        prevColor = 'grey'
    elif countNumber >0:
        window.configure(bg='green')
        prevColor = 'green'
    else:
        window.configure(bg='red')
        prevColor = 'red'

def tripleLabel(event):
    global prevButton
    global countNumber
    if prevButton == button1:
        countNumber *= 3
    elif prevButton == button2:
        countNumber /= 3
    intVar.set(countNumber)
    

def onLabelEnter(event):
    window.configure(bg='yellow')

def onLabelLeave(event):
    window.configure(bg=prevColor)

options = {'fill': 'both', 'padx': 10, 'pady': 10, 'ipadx': 5}
button1 = tkinter.Button(text='up', bg="white", fg="black", font=("Arial", 10), command=addOne)                      
button1.pack(options)

intVar = tkinter.IntVar(value=0)
countLabel = tkinter.Label(window)
countLabel.configure(textvariable=intVar,bg="white", fg="black", font=("Arial", 10))
countLabel.bind("<Enter>", onLabelEnter)
countLabel.bind("<Leave>", onLabelLeave)
countLabel.bind("<Double-Button>", tripleLabel)

countLabel.pack(options)

button2 = tkinter.Button(text='down', bg="white", fg="black", font=("Arial", 10), command=subtractOne)                      
button2.pack(options)

window.mainloop()