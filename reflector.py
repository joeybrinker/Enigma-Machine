class Reflector:
    def __init__(self, reflector_type='B'):
        self.wiring = self._get_reflector_wiring(reflector_type)

    def _get_reflector_wiring(self, reflector_type):
        # Historical Enigma reflector wirings given by ChatGPT
        # Prompt: I am creating an Enigma Machine in Python. Can you give me accurate historical Rotor values
        # Link: https://chatgpt.com/share/67d0bba7-26b0-800f-a39b-80711d5f19ea
        wirings = {
            'A': "EJMZALYXVBWFCRQUONTSPIKHGD",
            'B': "YRUHQSLDPXNGOKMIEBFZCWVJAT",
            'C': "FVPJIAOYEDRZXWGCTKUQSBNMHL"
        }
        return wirings.get(reflector_type, wirings['B'])

    def reflect(self, char_index):
        reflected_letter = self.wiring[char_index]
        return ord(reflected_letter) - ord('A')