import tkinter as tk


def dr(text):
    global out
    zahl = get_wert(text)
    out.set(f'Umwandeln in: {text}')
    ergebnis.set(str(int(zahl) - 273))
    fenster.update_idletasks()

def du(text):
    global out, ergebnis
    zahl = get_wert(text)
    out.set(f'Umwandeln in: {text}')
    ergebnis.set(str(int(zahl) + 273))
    fenster.update_idletasks()


def get_wert(text):
    global wert
    wert = zahl.get()
    zahl.delete(0,'end')
    return wert


#def knopfgedrückt(text):
   # global out
    # die verschiedenen outputs einer Variable zuordnen
    #out.set(f'Umwandeln in: {text}')
    #fenster.update_idletasks()
    #zahl = input('wie lautet die Zahl')

def changeColor(self):
    self.b1.configure(bg="yellow")

wert = 0

#optionen = [ "Schlumpf", "Zwerg", "Zentaur"]

# ein tkinter fenster erstellen
fenster = tk.Tk()
# Hintergrundfarbe
# Die verschiedenen Farbmöglichkeiten findet man z.B. hier:
# http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter
fenster.config(bg='gray65')

#fenster größe
#fenster.geometry('100x200')
# Name des Fensters
fenster.title('MyCoolApp')

# die Variablen für die Outputs erzeugen und auf '' = nichts setzen
out = tk.StringVar()
out.set('Wähle aus!')
ergebnis = tk.StringVar()
ergebnis.set('')
#var_opt = tk.StringVar()
#var_opt.set(optionen[0])


# Dropdown Menü
#opt = tk.OptionMenu(fenster, var_opt, *optionen)
#opt.config(width=10, font=('Helvetica', 12))
#opt.pack(side='top')

# Überschrift im Fenster
header = tk.Label(fenster,text='   Umwandler    ',
                        font=('Helvetica',24, 'bold'), bg='gray65', fg='black', width = 40, height=2)

#header.grid(row=0, column=0, columnspan=3, rowspan=2)
# Positionen
# row,column
#  __ __ __
# |00 01 02|
# |10 11 12|
# |20 21 22|
header.pack()

# Text im Fenster
beschreibung = tk.Label(fenster, text='made by AKL©', font=('Helvetica', 16, 'bold'),
                        bg='gray65', fg='black', width = 20, height=1)

#beschreibung.grid(row=2,column=0, columnspan=3, rowspan=1)
beschreibung.pack()

# out1 im Fenster ausgeben
ausgabe = tk.Label(fenster, textvariable=out, font=('Helvetica',14, 'bold'),
                   bg='gray65', fg='black', width = 40, height=2)


# ausgabe.grid(row=3,column=0)
ausgabe.pack()

# out1 im Fenster ausgeben
#ergebniss 2
ergebnisfeld = tk.Label(fenster, textvariable=ergebnis, font=('Helvetica',14, 'bold'),
                   bg='gray65', fg='black', width = 40, height=2)


# ausgabe.grid(row=3,column=0)
ergebnisfeld.pack()


zahl = tk.Entry(fenster, font=('Helvetica',14, 'bold'),
                   bg='dim gray', fg='black')

zahl.pack()
rahmen = tk.Frame(fenster, bg='gray65')
rahmen.pack(side='top', padx='5', pady='10')

# Buttons
'''b1 = tk.Button(rahmen,text='℉', bg='red', highlightbackground='red', fg='black',
               command=lambda: knopfgedrückt(''))'''





b2 = tk.Button(rahmen, text='Kelvin→℃', bg='black', highlightbackground='green', fg='white',
               command=lambda: dr('Celsius'))

b3 = tk.Button(rahmen, text='Celsius→Kelvin', bg='black', highlightbackground='blue', fg='white',
               command=lambda: du('Kelvin'))



#optionen: after, anchor, before, expand, fill, in, ipadx, ipady, padx, pady, side
#b1.pack(side = 'left', padx = 10, pady=40, fill='y')
b2.pack(side = 'left', padx = 10, pady=40, fill='y')
b3.pack(side = 'left', padx = 10, pady=40, fill='y')




# Fenster erzeugen, immer zum Schluss
#if a == 1:
 #   eingabe1 = input('was soll es sein?')
  #  print(eingabe1 - 273)
#else:
 #   print('nothing')
fenster.mainloop()
