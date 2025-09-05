class Plugboard:
    def __init__(self, connections):
        self.mapping = self._create_mapping(connections)

    def _create_mapping(self, connections):
        # Initialize with default mapping (each letter to itself)
        mapping = {chr(i + ord('A')): chr(i + ord('A')) for i in range(26)}

        # Apply the connections
        if connections and len(connections) % 2 == 0:
            for i in range(0, len(connections), 2):
                first, second = connections[i], connections[i + 1]
                mapping[first] = second
                mapping[second] = first

        return mapping

    def swap(self, letter):
        return self.mapping.get(letter, letter)