from rotor import Rotor
from reflector import Reflector
from plugboard import Plugboard


class EnigmaMachine:
    def __init__(self, rotor_numbers, rotor_positions, plugboard_settings):
        # Rotors
        self.rotors = [
            Rotor(rotor_numbers[0], rotor_positions[0]),
            Rotor(rotor_numbers[1], rotor_positions[1]),
            Rotor(rotor_numbers[2], rotor_positions[2])
        ]

        # Reflector
        self.reflector = Reflector()

        # Plugboard
        self.plugboard = Plugboard(plugboard_settings)

    def _rotate_rotors(self):
        # Check if middle rotor is at notch position
        if self.rotors[1].position_at_notch():
            self.rotors[0].rotate()  # Rotate left rotor
            self.rotors[1].rotate()  # Rotate middle rotor
        # Check if right rotor is at notch position
        elif self.rotors[2].position_at_notch():
            self.rotors[1].rotate()  # Rotate middle rotor

        # Right rotor always rotates
        self.rotors[2].rotate()

    def process_letter(self, letter):
        if not letter.isalpha():
            return letter  # Return non-alphabetic characters

        letter = letter.upper()

        # Apply plugboard
        letter = self.plugboard.swap(letter)

        # Rotate Rotors
        self._rotate_rotors()

        # Convert letter to index (0-25)
        char_index = ord(letter) - ord('A')

        # Pass through rotors right to left
        for rotor in reversed(self.rotors):
            char_index = rotor.forward_pass(char_index)

        # Pass through reflector
        char_index = self.reflector.reflect(char_index)

        # Pass through rotors left to right
        for rotor in self.rotors:
            char_index = rotor.backward_pass(char_index)

        # Convert index back to letter
        result = chr(char_index + ord('A'))

        # Apply plugboard again
        result = self.plugboard.swap(result)

        return result

    def process_text(self, text):
        result = ""
        for letter in text:
            result += self.process_letter(letter)
        return result