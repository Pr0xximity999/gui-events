from tkinter import *

UpLastPressed = False
DownLastPressed = False

num = 0
window = Tk()
window.configure(bg='grey')
window.title('Clicker')
window.geometry('250x200')

#updates the background and text
def update(event=''):
    global text, window, num
    text.configure(text="%.2f" %num)

    #Updates the background depending on the number's value
    color = ''
    if num == 0:
        color = 'grey'
    elif num > 0:
        color = 'green'
    else:
        color = 'red'
    window.configure(bg=color)

#Some event functions
def yellow(event=''):
    window.configure(bg='yellow')

def triple(event=''):
    global num
    num *= 3
    update()

def deTriple(event=''):
    global num
    num /= 3
    update()


#The functions for handling the increment and decrement of the on screen number
def increment():
    global num, UpLastPressed, DownLastPressed
    UpLastPressed = True
    DownLastPressed = False
    num += 1
    update()

def decrement():
    global num, UpLastPressed, DownLastPressed
    UpLastPressed = False
    DownLastPressed = True
    num -= 1
    update()


#Sets up the top and bottom button and the number
upBtn = Button(text="up", width=32, height=1, command=increment)
upBtn.pack() 
upBtn.place(relx=0.5, rely=0.2, anchor=CENTER)    

text = Label(window, text=num, font=("Helvetica", 20), width= 14, height=1)
text.pack()
text.place(relx=0.5, rely=0.5, anchor=CENTER) 

downBtn = Button(text="down", width=32, height=1, command=decrement)
downBtn.pack() 
downBtn.place(relx=0.5, rely=0.8, anchor=CENTER)  

#Binds the button double click events
upBtn.bind('<Double-Button-1>', triple)
downBtn.bind('<Double-Button-1>', deTriple)

#When the mouse hovers over the label, fire the yellow function and else, just the regular
text.bind('<Enter>', yellow)
text.bind('<Leave>', update)

window.mainloop()