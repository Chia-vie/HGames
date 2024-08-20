class Crypto:
    def __init__(self, msg):
        self.msg = msg.lower()
        self.abc = [' ', '.', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i',
                    'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
                    's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        self.key = [-18, -19, 0, -2, -22, -23, -9, -2, -3, -4,
                    -6, -6, -1, -22, -14, -16, -11, -13, -3, -15,
                    -11, -21, -10, 0, -22, -14, -20, -23, -16,
                    -15, -13, -3, -10, -15, -6, -2, -17, -10, -6,
                    -12, -19, -3, -6, -7, -14, -3, -11, -6, -19,
                    -17, -15, -4, -16, -16, -11, -17, -21, -9,
                    -15, -20, -4, -11, -6, -15, -1, -9, -23, -21,
                    -16, -21, -14, -15, -1, -23, -4, -14, -5, -20,
                    -17, -23, -1, -11, -21, -20, -18, -20, -10,
                    -21, -7, 0, -10, -18, -8, -20, -10, -10, -20,
                    -10, -14, -23, -8, -23, -5, -2, -2, -16, -2,
                    -2, -21, -17, -4, -17, -17, -1, -15, -23, 0,
                    -12, -20, -2, -12, -4, -12, 0, -23, -19, -4,
                    -20, -18, -7, -3, -8, -16, -15, -15, -8, -5,
                    -1, 0, -18, 0, -17, -3, -5, -13, -10, -4, -4,
                    -1, -1, -17, -10, -4, -20, -3, -16, -8, -22,
                    -11, -17, -23, -23, -9, -3, -1, -12, -23, -5,
                    -10, -6, -7, -11, -5, -9, -19, -11, -23, -10,
                    -15, 0, -8, -8, -3, -16, -16, -13, -22, -10,
                    -9, -11, -13, -13, -1, -23, -2, -7, -21, -10,
                    -5, -10]

    def encrypt(self):
        return self._crypt(encrypt=True)

    def decrypt(self):
        return self._crypt(encrypt=False)

    def _crypt(self, encrypt=True):
        msg_res = ''
        abc_len = len(self.abc)
        key_len = len(self.key)

        for n, zeichen in enumerate(self.msg):
            zeichen_index = self.abc.index(zeichen)
            key_shift = self.key[n % key_len]
            shift = key_shift if encrypt else -key_shift
            new_index = (zeichen_index + shift) % abc_len
            msg_res += self.abc[new_index]

        return msg_res


# Example Usage:
if __name__ == '__main__':
    nachricht = Crypto('njsyoxkyrjm qkmzrreczjztf')
    encrypted_message = nachricht.encrypt()
    decrypted_message = nachricht.decrypt()
    
    print(f"Encrypted: {encrypted_message}")
    print(f"Decrypted: {decrypted_message}")
