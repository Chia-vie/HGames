import tkinter as tk

def dr(text):
    """Convert Kelvin to Celsius."""
    zahl = get_wert()
    out.set(f'Umwandeln in: {text}')
    ergebnis.set(str(int(zahl) - 273))
    fenster.update_idletasks()

def du(text):
    """Convert Celsius to Kelvin."""
    zahl = get_wert()
    out.set(f'Umwandeln in: {text}')
    ergebnis.set(str(int(zahl) + 273))
    fenster.update_idletasks()

def get_wert():
    """Retrieve and clear the value from the Entry widget."""
    wert = zahl.get()
    zahl.delete(0, 'end')
    return wert

# Initialize tkinter window
fenster = tk.Tk()
fenster.config(bg='gray65')
fenster.title('MyCoolApp')

# Initialize variables
out = tk.StringVar()
out.set('Wähle aus!')
ergebnis = tk.StringVar()
ergebnis.set('')

# Header Label
header = tk.Label(fenster, text='Umwandler', font=('Helvetica', 24, 'bold'), 
                  bg='gray65', fg='black', width=40, height=2)
header.pack()

# Description Label
beschreibung = tk.Label(fenster, text='made by AKL©', font=('Helvetica', 16, 'bold'),
                        bg='gray65', fg='black', width=20, height=1)
beschreibung.pack()

# Output Labels
ausgabe = tk.Label(fenster, textvariable=out, font=('Helvetica', 14, 'bold'),
                   bg='gray65', fg='black', width=40, height=2)
ausgabe.pack()

ergebnisfeld = tk.Label(fenster, textvariable=ergebnis, font=('Helvetica', 14, 'bold'),
                        bg='gray65', fg='black', width=40, height=2)
ergebnisfeld.pack()

# Entry Field for Input
zahl = tk.Entry(fenster, font=('Helvetica', 14, 'bold'), bg='dim gray', fg='black')
zahl.pack()

# Frame for Buttons
rahmen = tk.Frame(fenster, bg='gray65')
rahmen.pack(side='top', padx=5, pady=10)

# Buttons for Conversion
b2 = tk.Button(rahmen, text='Kelvin→℃', bg='black', highlightbackground='green', fg='white',
               command=lambda: dr('Celsius'))
b3 = tk.Button(rahmen, text='Celsius→Kelvin', bg='black', highlightbackground='blue', fg='white',
               command=lambda: du('Kelvin'))

# Arrange buttons in the frame
b2.pack(side='left', padx=10, pady=40, fill='y')
b3.pack(side='left', padx=10, pady=40, fill='y')

# Start the tkinter main loop
fenster.mainloop()
