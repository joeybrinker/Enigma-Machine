from unittest import TestCase, expectedFailure
from rotor import Rotor


class TestRotor(TestCase):
    def test__get_rotor_wiring(self):
        # Arrange - setup our variables for testing
        rotor = Rotor(1, 0)
        expected_result = "EKMFLGDQVZNTOWYHXUSPAIBRCJ"

        # Act - call the code we're testing
        actual_result = rotor._get_rotor_wiring(1)

        # Assert - did we get what we expected
        self.assertEqual(expected_result, actual_result)

    def test__get_notch_position(self):
        # Arrange - setup our variables for testing
        rotor = Rotor(1, 0)

        # Act - call the code we're testing
        result = rotor._get_notch_position(1)

        # Assert - did we get what we expected
        self.assertEqual('Q', result)

    def test_forward_pass(self):
        # Arrange - setup our variables for testing
        rotor = Rotor(1,0)

        # Act - call the code we're testing
        result = rotor.forward_pass(0) # Should map A to E, which is index 0 to index 4

        # Assert - did we get what we expected
        self.assertEqual(4, result)

    def test_backward_pass(self):
        # Arrange - setup our variables for testing
        rotor = Rotor(1, 0)

        # Act - call the code we're testing
        result = rotor.backward_pass(4)  # Should map E to A, which is index 4 to index 0

        # Assert - did we get what we expected
        self.assertEqual(0, result)

    def test_rotate(self):
        # Arrange - setup our variables for testing
        rotor = Rotor(1, 0)

        # Act - call the code we're testing
        rotor.rotate()
        actual_result = rotor.position

        # Assert - did we get what we expected
        self.assertEqual(1, actual_result)

    def test_position_at_notch(self):
        # Arrange - setup our variables for testing
        rotor1 = Rotor(1, 16)
        rotor2 = Rotor(2, 4)
        rotor3 = Rotor(3, 21)

        # Act - call the code we're testing
        # Assert - did we get what we expected
        self.assertTrue(rotor1.position_at_notch())
        self.assertTrue(rotor2.position_at_notch())
        self.assertTrue(rotor3.position_at_notch())
