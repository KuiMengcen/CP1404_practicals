def get_valid_score():
    """
    Repeatedly prompts the user to enter a score between 0 and 100.
    Once the input is valid, the score is returned.
    """
    score = -1  # Initialize score to an invalid value
    while score < 0 or score > 100:
        try:
            score = float(input("Enter a score (0-100): "))
            if score < 0 or score > 100:
                print("Invalid score. Please try again.")
        except ValueError:
            print("Please enter a valid number.")
    return score


def determine_status(score):
    """
        Determines the status of a score based on predefined criteria.
    """
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


def print_result(score):
    """
        Prints the status of the given score.
    """
    status = determine_status(score)
    print(f"Status: {status}")


def show_stars(score):
    """
        Print a visual representation of the score using an asterisk.
    """
    print("*" * int(score))


def main():
    """
        The main function of the programme.
    """
    print("Welcome to the Score Program!")

    score = get_valid_score()

    choice = ""

    while choice != "Q":
        print("\nMain Menu:")
        print("(G)et a valid score")
        print("(P)rint result")
        print("(S)how stars")
        print("(Q)uit")

        choice = input("Enter your choice: ").upper()

        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print_result(score)
        elif choice == "S":
            show_stars(score)
        elif choice == "Q":
            print("Thank you for using the Score Program. Goodbye!")
        else:
            print("Invalid option. Please try again.")


main()
