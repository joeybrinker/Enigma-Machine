class Rotor:
    def __init__(self, rotor_num, starting_position):

        self.position = starting_position
        self.wiring = self._get_rotor_wiring(rotor_num)
        self.notch = self._get_notch_position(rotor_num)

    def _get_rotor_wiring(self, rotor_num):
        # Historical Enigma rotor wirings given by ChatGPT
        # Prompt: I am creating an Enigma Machine in Python. Can you give me accurate historical Rotor values
        # Link: https://chatgpt.com/share/67d0bba7-26b0-800f-a39b-80711d5f19ea
        wirings = {
            1: "EKMFLGDQVZNTOWYHXUSPAIBRCJ",
            2: "AJDKSIRUXBLHWTMCQGZNPYFVOE",
            3: "BDFHJLCPRTXVZNYEIWGAKMUSQO",
            4: "ESOVPZJAYQUIRHXLNFTGKDCMWB",
            5: "VZBRGITYUPSDNHLXAWMJQOFECK"
        }
        return wirings.get(rotor_num, wirings[1])

    def _get_notch_position(self, rotor_num):
        # The position where the rotor triggers the next rotor to rotate given by ChatGPT
        # Prompt: I am creating an Enigma Machine in Python. Can you give me accurate historical Rotor values
        # Link: https://chatgpt.com/share/67d0bba7-26b0-800f-a39b-80711d5f19ea
        notches = {
            1: "Q",  # Notch at position 16 (Q)
            2: "E",  # Notch at position 4 (E)
            3: "V",  # Notch at position 21 (V)
            4: "J",  # Notch at position 9 (J)
            5: "Z"  # Notch at position 25 (Z)
        }
        return notches.get(rotor_num, notches[1])

    def forward_pass(self, char_index):
        # Find the output letter after going through the rotor
        shift_index = (char_index + self.position) % 26
        shifted_letter = self.wiring[shift_index]
        return (ord(shifted_letter) - ord('A') - self.position) % 26

    def backward_pass(self, char_index):
        # Find the output letter after going through the rotor in reverse
        shift_index = (char_index + self.position) % 26
        letter = chr(shift_index + ord('A'))
        wiring_index = self.wiring.index(letter)
        return (wiring_index - self.position) % 26

    def rotate(self):
        self.position = (self.position + 1) % 26
        return self.position_at_notch()

    def position_at_notch(self):
        current_letter = chr((self.position % 26) + ord('A'))
        return current_letter == self.notch