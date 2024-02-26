MINIMUM_LENGTH = 0  # Consider setting it to a positive value to enforce minimum password length.


def main():
    """
    The main function that coordinates the flow of the programme.
    """
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """
    Prints an asterisk * corresponding to the length of the password.
    """
    print(len(password) * '*')


def get_password():
    """
  Prompts the user for a password, returning a password string that meets the minimum length requirement.
    """
    password = input("Please enter a password: ")
    while len(password) < MINIMUM_LENGTH:
        print("Error: Password does not meet the minimum length requirement.")
        password = input("Please enter a password: ")
    return password


main()
