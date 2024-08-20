import tkinter as tk
import random

def random_rectangle_coordinates(x_range, y_range):
    """Generate random coordinates for a rectangle within given ranges."""
    x1 = random.randint(*x_range)
    y1 = random.randint(*y_range)
    x2 = random.randint(*x_range)
    y2 = random.randint(*y_range)
    return x1, y1, x2, y2

def clicked(*args):
    global rect_coords_1, rect_coords_2

    colours = ["red", "green", "SteelBlue1", "honeydew2", "tomato2", 
               "cyan2", "OliveDrab1", "wheat2", "sienna2", "lawn green"]
    colour = random.choice(colours)

    # Randomly choose which rectangle to draw
    rect_choice = random.choice([1, 2])

    counter.set(counter.get() + 1)
    feld.delete("all")

    if rect_choice == 1:
        rect_coords_1 = random_rectangle_coordinates((100, 1000), (500, 800))
        rectangle1 = feld.create_rectangle(*rect_coords_1, fill=colour, tags="rectangle1")
    else:
        rect_coords_2 = random_rectangle_coordinates((1000, 1500), (10, 800))
        rectangle2 = feld.create_rectangle(*rect_coords_2, fill=colour, tags="rectangle2")

# Initialize window
fenster = tk.Tk()
fenster.config(bg='gray100')
fenster.title('Dynamische Objekte in tkinter')

# Create canvas
feld = tk.Canvas(fenster, width=1920, height=1080, bd=0, bg='pale turquoise')
feld.pack()

# Initialize rectangles with random coordinates
rect_coords_1 = random_rectangle_coordinates((100, 1000), (400, 1000))
rect_coords_2 = random_rectangle_coordinates((1000, 1500), (100, 800))

# Draw initial rectangles
rectangle1 = feld.create_rectangle(*rect_coords_1, fill="red", tags="rectangle1")

# Counter for click events
counter = tk.IntVar()
Zaehler = tk.Label(fenster, font=('Gothic', 24, 'bold'), textvariable=counter, width=10, height=5, fg="gray100", bg="gray1")
Zaehler.place(x=0, y=0)

# Bind click event to rectangle
feld.tag_bind("rectangle1", "<Button-1>", clicked)

# Run the main loop
fenster.mainloop()
