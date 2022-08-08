class Morse:
    morse_dict = {}

    def __init__(self):
        self.build_morse_dict()

    def build_morse_dict(self):
        self.morse_dict = {
            'A': '._', 'B': '_...', 'C': '_._.', 'D': '_..',
            'E': '.', 'F': '.._.', 'G': '__.', 'H': '....',
            'I': '..', 'J': '.___', 'K': '_._', 'L': '._..',
            'M': '__', 'N': '_.', 'O': '___', 'P': '.__.',
            'Q': '__._', 'R': '._.', 'S': '...', 'T': '_',
            'U': '.._', 'V': '..._', 'W': '.__', 'X': '_.._',
            'Y': '_.__', 'Z': '__..', '1': '.____', '2': '..___',
            '3': '...__', '4': '...._', '5': '.....', '6': '_....',
            '7': '__...', '8': '___..', '9': '___.', '0': '_____'
        }

    def get_morse_code(self, letter: str) -> str:
        return self.morse_dict[letter]

    def get_morse_letter(self, code: str) -> str:
        keys = list(self.morse_dict.keys())
        values = list(self.morse_dict.values())

        return keys[values.index(code)]

    def parse_sentence(self, sentence: str) -> str:
        sentence = sentence.upper()
        morse_sentence = ""

        for letter in sentence:
            if letter != ' ':
                morse_sentence += self.get_morse_code(letter)
            else:
                morse_sentence += ' '
            morse_sentence += ' '

        return morse_sentence
