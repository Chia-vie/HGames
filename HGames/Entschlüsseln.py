'''
Author: Damian Sykora, Alexander Steinbauer
Date: 17th of August 2021
This is a program to encrypt and decrypt messages.
'''

class VerEntSchluesseln:
    def __init__(self):
        self.ver_schluessel = [3, 5, 6, 2, 4, 5, 7, 9, 20, 6, 3, 5, 6, 3, 4, 8, 1, 14, 12, 21, 19, 12, 21, 12]
        self.ent_schluessel = [3, 5, 6, 2, 4, 5, 7, 9, 34, 6, 3, 5, 6, 3, 4, 8, 1, 87, 45, 67, 98, 12, 34, 56]

    def process_text(self, text, schluessel, mode='encrypt'):
        result_list = []
        key_len = len(schluessel)

        for i, char in enumerate(text):
            key = schluessel[i % key_len]
            if mode == 'encrypt':
                processed_char = chr(ord(char) + key)
            else:
                processed_char = chr(ord(char) - key)
            result_list.append(processed_char)

        result = ''.join(result_list)
        return result

    def verschluesseln(self, text):
        return self.process_text(text, self.ver_schluessel, mode='encrypt')

    def entschluesseln(self, text):
        return self.process_text(text, self.ent_schluessel, mode='decrypt')


# Main program
mein = VerEntSchluesseln()
mode = input('Willst du verschlüsseln oder entschlüsseln? ').strip().lower()

if mode == 'verschlüsseln':
    text = input('Gib den Text zum Verschlüsseln ein: ')
    encrypted_text = mein.verschluesseln(text)
    print(f'Verschlüsselter Text: {encrypted_text}')
elif mode == 'entschlüsseln':
    text = input('Gib den Text zum Entschlüsseln ein: ')
    decrypted_text = mein.entschluesseln(text)
    print(f'Entschlüsselter Text: {decrypted_text}')
else:
    print('Ungültige Eingabe, bitte "verschlüsseln" oder "entschlüsseln" eingeben.')
