'''
Author:Damian Sykora, Alexander Steinbauer
Date: 17th of August 2021
This is a program to encrypt and decrypt messages.
'''


class VerEntSchluesseln:
    def entschluesseln(self):
        # voreingestellte Variablen und Listen
        schluessel = [3, 5, 6, 2, 4, 5, 7, 9, 34, 6, 3, 5, 6, 3, 4, 8, 1, 87, 45, 67, 98, 12, 34, 56]
        text = input('eingabe:')
        zahl = 0
        entliste = []
        # vercodungsprozess str->int+int->str
        for n in text:
            egal = ord(n)
            entliste.append(chr(egal - schluessel[zahl]))
            zahl += 1
            if zahl == 23:
                zahl = 0
        # output
        print(''.join(x for x in entliste))
        return ''.join(x for x in entliste)

    def VerSchluesseln(self):
        # voreingestellte Variablen und Listen
        schluessel = [3, 5, 6, 2, 4, 5, 7, 9, 20, 6, 3, 5, 6, 3, 4, 8, 1, 14, 12, 21, 19, 12, 21, 12]
        text = input('eingabe:')
        zahlen = 0
        verliste = []
        # vercodungsprozess str->int+int->str
        for n in range(len(text)):
            umgewandelte_zahl = (ord(text[n]) + schluessel[zahlen])
            verliste.append(''.join(chr(umgewandelte_zahl)))
            zahlen += 1
            if zahlen == 23:
                zahlen = 0
        # output
        print(''.join(x for x in verliste))
        return ''.join(x for x in verliste)



mein = VerEntSchluesseln()
ver_oder_ent = input('willst du ver- oder entschlüsseln?').upper()
if ver_oder_ent == 'VERSCHLÜSSELN':
    mein.VerSchluesseln()
elif ver_oder_ent == 'ENTSCHLÜSSELN':
    mein.entschluesseln()
else:
    print('was meinst du?')
