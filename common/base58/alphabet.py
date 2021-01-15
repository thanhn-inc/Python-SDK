class Alphabet:
    def __init__(self, alphabet=None):
        self.alphabet = "123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz"
        if alphabet:
            if len(alphabet) != 58:
                raise Exception("alphabet must be of length 58: have {}.".format(len(alphabet)))
            self.alphabet = alphabet 

        self.encode = [ord(self.alphabet[i]) for i in range(len(self.alphabet))]
        self.decode = [-1 for i in range(128)]
        for i in range(len(self.encode)):
            b = self.encode[i]
            self.decode[b] = i

BTC_ALPHABET = Alphabet("123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz")
FLICKR_ALPHABET = Alphabet("123456789abcdefghijkmnopqrstuvwxyzABCDEFGHJKLMNPQRSTUVWXYZ")

def main():
    alphabet = Alphabet()
    print(alphabet.encode, alphabet.decode)

if __name__ == "__main__":
    main()