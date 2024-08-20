import tkinter as tk
import random

def clicked(*args):
    """Handles the click event and updates the rectangle."""
    # Randomize colors
    colours = ["red", "green", "SteelBlue1", "honeydew2", "tomato2", 
               "cyan2", "OliveDrab1", "wheat2", "sienna2", "lawn green"]
    colour = random.choice(colours)

    # Randomize shape to create
    rect_type = random.choice(["x", "y"])

    # Increment the counter
    counter.set(counter.get() + 1)
    
    # Clear the canvas
    feld.delete("all")

    # Create new rectangle
    if rect_type == "x":
        feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill=colour, tags="rectangle1")
    else:
        feld.create_rectangle(random_rectangle2x1, random_rectangle2y1, random_rectangle2x2, random_rectangle2y2, fill=colour, tags="rectangle1")
    
    # Randomize new positions for rectangles
    randomize_positions()

def randomize_positions():
    """Randomizes positions for the rectangles."""
    global random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2
    global random_rectangle2x1, random_rectangle2y1, random_rectangle2x2, random_rectangle2y2

    random_rectanglex1 = random.randint(100, 1000)
    random_rectangley1 = random.randint(500, 800)
    random_rectanglex2 = random.randint(100, 1000)
    random_rectangley2 = random.randint(500, 800)

    random_rectangle2x1 = random.randint(1000, 1500)
    random_rectangle2y1 = random.randint(10, 800)
    random_rectangle2x2 = random.randint(1000, 1500)
    random_rectangle2y2 = random.randint(10, 800)

def countdown(count):
    """Manages the countdown timer and resets the game after it reaches zero."""
    label['text'] = f"Time left: {count} s"
    
    if count > 0:
        # Call countdown again after 1000ms (1s)
        fenster.after(1000, countdown, count-1)
    else:
        # Reset counter and start countdown again
        counter.set(0)
        countdown(10)

def setcounter():
    """Resets the counter and starts a new game."""
    counter.set(0)
    countdown(10)
    feld.delete("all")
    randomize_positions()
    feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill="red", tags="rectangle1")
    
# Initialize tkinter window
fenster = tk.Tk()
fenster.config(bg='gray100')
fenster.title('Speed Clicker AIM TRAINER')

# Create canvas for rectangles
feld = tk.Canvas(fenster, width=1920, height=1080, bd=0, bg='pale turquoise')
feld.pack()

# Initialize positions for rectangles
randomize_positions()

# Initialize counter variable
counter = tk.IntVar()

# Initial rectangle
feld.create_rectangle(random_rectanglex1, random_rectangley1, random_rectanglex2, random_rectangley2, fill="red", tags="rectangle1")

# Counter display
Zaehler = tk.Label(fenster, font=('Gothic', 24, 'bold'), textvariable=counter, width=10, height=5, fg="gray100", bg="gray1")
Zaehler.place(x=0, y=0)

# Bind the click event
feld.tag_bind("rectangle1", "<Button-1>", clicked)

# Timer label
label = tk.Label(fenster, text="Time left: 10 s")
label.place(x=500, y=15)

# Restart button
nochmal = tk.Button(fenster, text='Restart', command=setcounter)
nochmal.place(x=600, y=15)

# Start countdown
countdown(10)

# Start the tkinter main loop
fenster.mainloop()
