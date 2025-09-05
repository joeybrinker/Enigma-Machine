from unittest import TestCase
from reflector import Reflector


class TestReflector(TestCase):
    def test__get_reflector_wiring(self):
        # Arrange - setup our variables for testing
        reflector = Reflector('B')
        expected_result = "YRUHQSLDPXNGOKMIEBFZCWVJAT"

        # Act - call the code we're testing
        result = reflector._get_reflector_wiring('B')

        # Assert - did we get what we expected
        self.assertEqual(expected_result, result)

    def test_reflect(self):
        # Arrange - setup our variables for testing
        reflector = Reflector('B')

        # Act - call the code we're testing
        result = reflector.reflect(0) # Reflect A to Y

        # Assert - did we get what we expected
        self.assertEqual(24, result)
