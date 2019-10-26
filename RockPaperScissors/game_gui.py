import random
from tkinter import *
points = 0


def ck_win(user_input):
    options = ['r', 'p', 's']
    n = random.randrange(0, 3)
    comp = options[n]
    global points
    win = False
    if user_input == 'r' and comp == 's':
        win = True
        points += 1
    elif user_input == 'p' and comp == 'r':
        win = True
        points += 1
    elif user_input == 's' and comp == 'p':
        win = True
        points += 1

    if user_input==comp:
        var.set("Tie!")
    elif win:
        var.set("You Won!")
    else:
        var.set("You Lost!")
    pr.set("%d" % points)


if __name__ == "__main__":
    t = Tk()
    t.configure(bg="#eb4334")
    r = PhotoImage(file=r"C:\Users\anthi\rockpapersissors\images\rock.png")
    p = PhotoImage(file=r"C:\Users\anthi\rockpapersissors\images\paper.png")
    s = PhotoImage(file=r"C:\Users\anthi\rockpapersissors\images\scissors.png")
    b1 = Button(t, height=150 ,width=150 , image = r, command= lambda : ck_win('r'))
    b2 = Button(t, height=150 ,width=150 , image = p, command= lambda : ck_win('p'))
    b3 = Button(t, height=150 ,width=150 , image = s, command= lambda : ck_win('s'))
    b1.configure(bg="#eb4334")
    b2.configure(bg="#eb4334")
    b3.configure(bg="#eb4334")
    var = StringVar()
    pr = StringVar()
    l = Label(t, textvariable =var)
    l.configure(bg="#eb4334")
    l2 = Label(t, textvariable=pr)
    l2.configure(bg="#eb4334")
    var.set("Click")
    b1.pack()
    b2.pack()
    b3.pack()
    l.pack()
    l2.pack()
    t.mainloop()
