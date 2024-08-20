import tkinter as tk
import time

def update_spielzuege(spielzug, button_gedr):
    global symbol, winner_text, kreuz, kreis, running
    
    if running:
        spielzuege[int(spielzug)-1] = symbol
        button_gedr.config(image=kreuz if symbol == 'X' else kreis)

        # Check for a win condition
        if (spielzuege[0] == spielzuege[1] == spielzuege[2] or
            spielzuege[3] == spielzuege[4] == spielzuege[5] or
            spielzuege[6] == spielzuege[7] == spielzuege[8] or
            spielzuege[0] == spielzuege[3] == spielzuege[6] or
            spielzuege[1] == spielzuege[4] == spielzuege[7] or
            spielzuege[2] == spielzuege[5] == spielzuege[8] or
            spielzuege[0] == spielzuege[4] == spielzuege[8] or
            spielzuege[2] == spielzuege[4] == spielzuege[6]):
            winner_text.set(f"Spieler {symbol}, du hast gewonnen!")
            running = False
            return
        
        # Check for a draw condition
        if all(x in ['X', 'O'] for x in spielzuege):
            winner_text.set("Unentschieden!")
            running = False
            return

        # Switch player
        symbol = 'O' if symbol == 'X' else 'X'
        app.update_idletasks()

def reset_game():
    global spielzuege, symbol, running
    spielzuege = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbol = 'X'
    running = True
    winner_text.set("Tic Tac Toe")
    
    # Reset all buttons to the empty state
    for button in buttons:
        button.config(image=leer)

app = tk.Tk()

# Load images and keep references
kreuz = tk.PhotoImage(file='kreuz_klein.png')
kreis = tk.PhotoImage(file='kreis_klein.png')
leer = tk.PhotoImage(file='leer.png')

running = True
spielzuege = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
symbol = 'X'
winner_text = tk.StringVar(value='Tic Tac Toe')

app.config(bg="white")
app.title("Tic Tac Toe")

# Game header
ueberschrift = tk.Label(app, textvariable=winner_text, font=('Helvetica', 24, 'bold'), bg='white', fg='black')
ueberschrift.grid(row=0, column=0, columnspan=3, rowspan=1)

# Create buttons and store in a list for easy reset
buttons = []

for i in range(9):
    button = tk.Button(app, image=leer, font=("Helvetica", 40, "bold"), bg="white", fg="black", width=200, height=200,
                       command=lambda i=i: update_spielzuege(str(i+1), buttons[i]))
    button.grid(row=1 + i // 3, column=i % 3)
    buttons.append(button)

# Run the app
app.mainloop()
