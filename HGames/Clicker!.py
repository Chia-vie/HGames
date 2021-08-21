import tkinter as tk
import random
from time import *

def clicked(*args):
    global random_rectangley1
    global random_rectanglex1
    global random_rectangley2
    global random_rectanglex2
    global random_rectangle2y1
    global random_rectangle2x1
    global random_rectangle2y2
    global random_rectangle2x2
    colour_random = random.randint(1, 10)
    if colour_random == 1:
        colour = "red"
    elif colour_random == 2:
        colour = "green"
    elif colour_random == 3:
        colour = "SteelBlue1"
    elif colour_random == 4:
        colour = "honeydew2"
    elif colour_random == 5:
        colour = "tomato2"
    elif colour_random == 6:
        colour = "cyan2"
    elif colour_random == 7:
        colour = "OliveDrab1"
    elif colour_random == 8:
        colour = "wheat2"
    elif colour_random == 9:
        colour = "sienna2"
    elif colour_random == 10:
        colour = "lawn green"
    rect_random = random.randint(1, 2)
    if rect_random == 1:
        rect = "x"
    else:
        rect = "y"
    print(rect)

    counter.set(counter.get() + 1)
    feld.delete("all")
    if rect == "x":
        rectangle1 = feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill=colour,tags="rectangle1")
    elif rect == "y":
        rectangle2 = feld.create_rectangle(random_rectangle2x1, random_rectangle2y1, random_rectangle2x2, random_rectangle2y2, fill=colour,tags="rectangle1")
    random_rectanglex1 = random.randint(100, 1000)
    random_rectangley1 = random.randint(500, 800)
    random_rectanglex2 = random.randint(100, 1000)
    random_rectangley2 = random.randint(500, 800)
    random_rectangle2x1 = random.randint(1000, 1500)
    random_rectangle2y1 = random.randint(10, 800)
    random_rectangle2x2 = random.randint(1000, 1500)
    random_rectangle2y2 = random.randint(10, 800)

def countdown(count):
    global counter
    # change text in label
    label['text'] = count

    if count > 0:
        # call countdown again after 1000ms (1s)
        fenster.after(1000, countdown, count-1)

    else:
        counter.set(0)
        countdown(10)
        #message = feld.create_text(text='AUS')
        fenster.update()

def setcounter():
    global counter



fenster = tk.Tk()
fenster.config(bg = 'gray100')
fenster.title('Speed Clicker AIM TRAINER')
feld = tk.Canvas(fenster, width=1920, height=1080, bd=0, bg='pale turquoise')
feld.pack()
random_rectanglex1 = random.randint(100, 1000)
random_rectangley1 = random.randint(400, 1000)
random_rectanglex2 = random.randint(100, 1000)
random_rectangley2 = random.randint(400, 1000)
random_rectangle2x1 = random.randint(1000, 1500)
random_rectangle2y1 = random.randint(10, 800)
random_rectangle2x2 = random.randint(1000, 1500)
random_rectangle2y2 = random.randint(10, 800)
counter = tk.IntVar()

rectangle1 = feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill="red",tags="rectangle1")
Zaehler=tk.Label(fenster, font=('Gothic', 24, 'bold'), textvariable=counter, width=10, height=5, fg="gray100", bg="gray1")
Zaehler.place(x=0, y=0)
feld.tag_bind("rectangle1","<Button-1>",clicked)

label = tk.Label(fenster)
label.place(x=500, y=15)

# call countdown first time

nochmal = tk.Button(text='nochmal', command=setcounter)

countdown(10)
# root.after(0, countdown, 5)
'''if countdown == 0:
    counter.set(0)
    fenster.update()'''

fenster.mainloop()





