import tkinter as tk

class Formen():
    def __init__(self, app):
        self.feld = tk.Canvas(app, width=1000, height=1000, bd=0, bg='SeaGreen1')
        self.feld.pack()

        # Initial position and size of the square
        self.x1, self.y1 = 90, 100
        self.x2, self.y2 = 150, 160

        self.quadrat = self.feld.create_rectangle(self.x1, self.y1, self.x2, self.y2, fill='cyan', width=2, outline='aquamarine2')
        self.labyrinth = self.feld.create_rectangle(0, 10, 30, 40, fill="black", width=2, outline="black")

        # Bind the keys to movement functions
        app.bind('<KeyPress-Left>', self.left)
        app.bind('<KeyPress-Right>', self.right)
        app.bind('<KeyPress-Up>', self.up)
        app.bind('<KeyPress-Down>', self.down)

    def move_quadrat(self, dx, dy):
        # Update position
        self.x1 += dx
        self.y1 += dy
        self.x2 += dx
        self.y2 += dy
        
        # Check boundaries
        if self.x1 < 0: self.x1 = 0; self.x2 = self.x2 - dx
        if self.y1 < 0: self.y1 = 0; self.y2 = self.y2 - dy
        if self.x2 > 1000: self.x2 = 1000; self.x1 = self.x1 - dx
        if self.y2 > 1000: self.y2 = 1000; self.y1 = self.y1 - dy
        
        # Move the square
        self.feld.coords(self.quadrat, self.x1, self.y1, self.x2, self.y2)

    def right(self, event):
        self.move_quadrat(5, 0)

    def left(self, event):
        self.move_quadrat(-5, 0)

    def up(self, event):
        self.move_quadrat(0, -5)

    def down(self, event):
        self.move_quadrat(0, 5)


# Create window
app = tk.Tk()

# Define window properties
app.config(bg='SeaGreen1')
app.geometry("1000x1000")
app.title("Looney Labyrinth")

# Add header label
ueberschrift = tk.Label(app, text="****** Looney Labyrinth ******",
                        font=("Helvetica", 24, "bold"), bg="cyan", fg="magenta3", width=20, height=2)
ueberschrift.pack(side='top')

# Create the labyrinth object
abenteurer = Formen(app)

# Start the Tkinter event loop
app.mainloop()
