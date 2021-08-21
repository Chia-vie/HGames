class Coder():
    def __init__(self, input):
        self.verdict = {'a': 'o', 'b': 'd', 'c': 'm', 'd': 'g', 'e': 'r', 'f': 'w', 'g': 'k',
                         'h':'a','i':'t','j':'z','k':'x','l':'b','m':'f','n':'j',
                         'o':'p','p':'?','q':'q','r':'i','s':'h','t':'n','u':'c',
                         'v':'u','w':'l','x':'y','y':'e','z':'s',' ':'1','L':'3','N':'4'}

        self.entdict = {'o': 'a', 'd': 'b', 'm': 'c', 'g': 'd', 'r': 'e', 'w': 'f', 'k': 'g',
                 'a':'h','t':'i','z':'j','x':'k','b':'l','f':'m','j':'n',
                 'p':'o','y?':'p','q':'q','i':'r','h':'s','n':'t','c':'u',
                 'u':'v','l':'w','y':'x','e':'y','s':'z','1':'  ','3':'L','4':'N'}

        self.input = input

    def verschluesseln(self):
        ver_text = []
        for buchstabe in self.input:
            neuerbuchstabe = self.verdict[buchstabe]
            ver_text.append(neuerbuchstabe)
            vert_text = ''.join(x for x in ver_text)
        return vert_text

    def entschluesseln(self):
        ent_text = []
        for buchstabe in self.input:
            neuerbuchstabe = self.entdict[buchstabe]
            ent_text.append(neuerbuchstabe)
            ente_text = ''.join(x for x in ent_text)
        return ente_text

modus = input('Entschlüsseln(a) oder Verschlüsseln(b)\n')

if modus == 'b':
    print('Ok, ich verschlüssele')
    text = input('Gib einen Text ein\n')
    meinobjekt = Coder(text)
    print(meinobjekt.verschluesseln())
else:
    print('Ok, ich entschlüssele')
    text = input('Gib einen Text ein\n')
    meineobjekt = Coder(text)
    print(meineobjekt.entschluesseln())


