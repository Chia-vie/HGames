import tkinter as tk
class Formen():
    def __init__(self, app):
        self.feld = tk.Canvas(app, width=1000, height=1000, bd=0, bg='SeaGreen1')
        self.feld.pack()
        self.points = [90, 100, 150, 160,]
        self.quadrat = self.feld.create_rectangle(self.points, fill='cyan', width=2, outline='aquamarine2')
        self.labyrinth = self.feld.create_rectangle(0, 10, 30, 40, fill="black", width=2, outline="black")
        self.x = 0
        self.y = 0
        self.feld.move(self.quadrat, self.x, self.y)
        self.feld.move(self.labyrinth, self.x, self.y)

    def right(self):
        self.x = 5
        self.y = 0
        self.feld.move(self.quadrat, self.x, self.y)

    def left(self):
        self.x = -5
        self.y = 0
        self.feld.move(self.quadrat, self.x, self.y)

    def up(self):
        self.x = 0
        self.y = -5
        self.feld.move(self.quadrat, self.x, self.y)

    def down(self):
        self.x = 0
        self.y = 5
        self.feld.move(self.quadrat, self.x, self.y)


#Fenster erstellen
app = tk.Tk()

#Appeigenschaften definieren
app.config(bg='SeaGreen1')

app.geometry("1000x1000")

app.title("Looney Labyrinth")

ueberschrift = tk.Label(app, text="****** Looney Labyrinth ******",
                        font=("Helvetica",24, "bold"), bg="cyan", fg="magenta3", width=20, height=2)

ueberschrift.pack(side='top')

abenteurer = Formen(app)


# Pfeiltasten
app.bind('<KeyPress-Left>', lambda e: abenteurer.left())
app.bind('<KeyPress-Right>', lambda e: abenteurer.right())
app.bind('<KeyPress-Up>', lambda e: abenteurer.up())
app.bind('<KeyPress-Down>', lambda e: abenteurer.down())

app.mainloop()
