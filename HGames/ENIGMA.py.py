class Coder():
    def __init__(self, input):
        self.verdict = {'a': 'o', 'b': 'd', 'c': 'm', 'd': 'g', 'e': 'r', 'f': 'w', 'g': 'k',
                        'h':'a','i':'t','j':'z','k':'x','l':'b','m':'f','n':'j',
                        'o':'p','p':'?','q':'q','r':'i','s':'h','t':'n','u':'c',
                        'v':'u','w':'l','x':'y','y':'e','z':'s',' ':'1','L':'3','N':'4'}

        self.entdict = {'o': 'a', 'd': 'b', 'm': 'c', 'g': 'd', 'r': 'e', 'w': 'f', 'k': 'g',
                        'a':'h','t':'i','z':'j','x':'k','b':'l','f':'m','j':'n',
                        'p':'o','?':'p','q':'q','i':'r','h':'s','n':'t','c':'u',
                        'u':'v','l':'w','y':'x','e':'y','s':'z','1':' ','3':'L','4':'N'}

        self.input = input

    def verschluesseln(self):
        return ''.join(self.verdict.get(buchstabe, buchstabe) for buchstabe in self.input)

    def entschluesseln(self):
        return ''.join(self.entdict.get(buchstabe, buchstabe) for buchstabe in self.input)

# Main program
modus = input('Entschlüsseln(a) oder Verschlüsseln(b)\n').strip().lower()

if modus == 'b':
    print('Ok, ich verschlüssele')
    text = input('Gib einen Text ein\n')
    meinobjekt = Coder(text)
    print(meinobjekt.verschluesseln())
elif modus == 'a':
    print('Ok, ich entschlüssele')
    text = input('Gib einen Text ein\n')
    meinobjekt = Coder(text)
    print(meinobjekt.entschluesseln())
else:
    print('Ungültiger Modus. Bitte "a" zum Entschlüsseln oder "b" zum Verschlüsseln wählen.')
