from unittest import TestCase
from plugboard import Plugboard


class TestPlugboard(TestCase):
    def test__create_mapping(self):
        # Arrange - setup our variables for testing
        plugboard = Plugboard("ABCDEF")

        # Assert - did we get what we expected (Check for correct Mapping)
        self.assertEqual("B", plugboard.mapping["A"])
        self.assertEqual("A", plugboard.mapping["B"])
        self.assertEqual("D", plugboard.mapping["C"])
        self.assertEqual("C", plugboard.mapping["D"])
        self.assertEqual("F", plugboard.mapping["E"])
        self.assertEqual("E", plugboard.mapping["F"])
        self.assertEqual("G", plugboard.mapping["G"])  # Not Connected, Shouldn't Change

    def test_swap(self):
        # Arrange - setup our variables for testing
        plugboard = Plugboard("AB")
        expected_result1 = "B"
        expected_result2 = "A"
        expected_result3 = "C"

        # Act - call the code we're testing
        result1 = plugboard.swap("A")
        result2 = plugboard.swap("B")
        result3 = plugboard.swap("C") # Not Connected, Shouldn't Change

        # Assert - did we get what we expected
        self.assertEqual(expected_result1, result1)
        self.assertEqual(expected_result2, result2)
        self.assertEqual(expected_result3, result3)
