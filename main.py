from enigma import EnigmaMachine

def parse_settings(settings_str):
    parts = settings_str.split()
    if len(parts) < 6:
        raise ValueError("Invalid settings format. Expected format: '3 2 5 24 12 11 ABCDEFGHIJKLMNOPQRST'")

    # Extract rotor numbers
    rotor_numbers = [int(parts[0]), int(parts[1]), int(parts[2])]

    # Extract rotor positions
    rotor_positions = [int(parts[3]), int(parts[4]), int(parts[5])]

    # Extract plugboard settings
    plugboard_settings = parts[6] if len(parts) > 6 else ""

    return rotor_numbers, rotor_positions, plugboard_settings


def main():
    print("Welcome to the Enigma Machine Simulator")
    print("---------------------------------------")

    settings = input("Choose 3 out of 5 total rotors 1-5.\n"
                     "Select a position for each rotor, there are 26 rotor positions 1-26.\n"
                     "Type in a 20 character string with no duplicate letters for the plugboard.\n\n"
                     "Enter Engima settings (format: '3 2 5 24 12 11 ABCDEFGHIJKLMNOPQRST'): ")
    try:
        rotor_numbers, rotor_positions, plugboard_settings = parse_settings(settings)
    except ValueError as e:
        print(f"Error: {e}")
        return

    # Create Enigma machine with the specified settings
    enigma = EnigmaMachine(rotor_numbers, rotor_positions, plugboard_settings)

    while True:
        print("\nWhat would you like to do?")
        print("1. Encrypt a message")
        print("2. Decrypt a message")
        print("3. Change Enigma settings")
        print("4. Exit")

        choice = input("Enter your choice (1-4): ")

        if choice == '1' or choice == '2':
            message = input("Enter the message: ")
            result = enigma.process_text(message)
            print(f"\nResult: {result}")

            # Reset enigma to initial settings for next operation
            enigma = EnigmaMachine(rotor_numbers, rotor_positions, plugboard_settings)

        elif choice == '3':
            settings = input("Enter new Enigma settings: ")
            try:
                rotor_numbers, rotor_positions, plugboard_settings = parse_settings(settings)
                enigma = EnigmaMachine(rotor_numbers, rotor_positions, plugboard_settings)
                print("Settings updated successfully.")
            except ValueError as e:
                print(f"Error: {e}")

        elif choice == '4':
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()