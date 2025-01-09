# 3-masala

class Alphabet:
    def __init__(self):
        self.alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index >= len(self.alphabet):
            raise StopIteration
        alphabet = self.alphabet[self.index]
        self.index += 1
        return alphabet

alphabet = Alphabet()

for i in alphabet:
    print(i)