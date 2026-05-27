from tkinter import *
import random

colours = ["Red", "Blue", "Yellow", "Green", "Orange", "Purple", "Black", "White", "Brown", "Pink"]

timeleft = 30
score = 0

def nextcol():
    global score
    global timeleft
    if timeleft > 0:
      if e.get().lower() == colours[1].lower():
          score +=1
      e.delete(0, END)
      random.shuffle(colours)
      lbls.config(text = "Score:" +str(score))
      lblword.config(fg = str(colours[1]) , text = str(colours[0]))



def cd():
    global timeleft
    if timeleft > 0:
        timeleft -= 1
        lbltim.config(text = "Time left:" + str(timeleft))
        lbltim.after(1000, cd)


def startgame(event):
    if timeleft == 30:
        cd()
    nextcol()


window = Tk()
window.title("pipis")

lblex = Label(window , text="Type in the colour of the words, NOT the word text!" , background="yellow" , width=40 , height=2 )
lblex.pack()

lbls = Label(window , text="Press ENTER to start" , background="purple" , width=15 , height=2 )
lbls.pack()

lbltim = Label(window , text="TIME LEFT: 30" , background="light green" , width=15 , height=2 )
lbltim.pack()

lblword = Label(window , text="" , font=('Helvetica', 60) , background="light yellow")
lblword.pack()


e = Entry(window, background="light blue")
window.bind('<Return>' , startgame)
e.pack()
e.focus_set()

window.geometry("650x650")
window.configure(bg="light yellow")
window.mainloop()