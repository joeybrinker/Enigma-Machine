from unittest import TestCase

import enigma
from enigma import EnigmaMachine


class TestEnigmaMachine(TestCase):
    def test__rotate_rotors(self):
        # Arrange - setup our variables for testing
        machine = EnigmaMachine([1, 2, 3], [1, 1, 1], [""])
        text = "J"
        expected_positions = [1, 1, 2]

        # Act - call the code we're testing
        machine._rotate_rotors()
        actual_positions = [rotor.position for rotor in machine.rotors]

        # Assert - did we get what we expected
        self.assertEqual(expected_positions, actual_positions)

    def test_process_letter(self):
        # Arrange - setup our variables for testing
        machine = EnigmaMachine([1, 2, 3], [0, 0, 0], "")

        # Act - call the code we're testing
        actual_result = machine.process_letter("A")

        # Assert - did we get what we expected
        # Test for string, length of 1, and is alpha
        self.assertTrue(isinstance(actual_result, str))
        self.assertTrue(len(actual_result) == 1)
        self.assertTrue(actual_result.isalpha())

    def test_process_text(self):
        # Arrange - setup our variables for testing
        machine = EnigmaMachine([1, 2, 3], [0, 0, 0], "")
        text = "HELLO"

        #Encryption
        # Act - call the code we're testing
        encrypted = machine.process_text(text)

        # Assert - did we get what we expected
        self.assertEqual(len(encrypted), len(text))
        self.assertTrue(encrypted.isalpha())

        # Decryption
        # Act - call the code we're testing
        machine = EnigmaMachine([1, 2, 3], [0, 0, 0], "")
        decrypted = machine.process_text(encrypted)

        # Assert - did we get what we expected
        self.assertEqual(decrypted, text)
