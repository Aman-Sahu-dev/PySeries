from number_guessing_game.logic.statistics import get_statistics


def display_dashboard() -> None:
    print("\n" + "=" * 40)
    print("          NUMBER GUESSING GAME")
    print("=" * 40)
    print("  1. Start New Game")
    print("  2. View High Score")
    print("  3. View Game Statistics")
    print("  4. Rules & Instructions")
    print("  5. Exit")
    print("=" * 40)


def get_choice() -> int | None:
    try:
        return int(input("Select an option: "))
    except ValueError:
        print("Invalid input! Enter a number.")
        return None


def show_high_score() -> None:
    stats = get_statistics()

    print("\n========== HIGH SCORE ==========")

    if stats["high_score"] is None:
        print("No successful games recorded yet.")
    else:
        print(f"Best attempts: {stats['high_score']}")

    print("=" * 32)


def show_statistics() -> None:
    stats = get_statistics()

    print("\n========== GAME STATISTICS ==========")
    print(f"Total games:       {stats['total_games']}")
    print(f"Successful games:  {stats['wins']}")
    print(f"Failed games:      {stats['losses']}")
    print(f"Average attempts:  {stats['average_attempts']}")
    print(f"Highest attempts:  {stats['highest_attempts']}")
    print("=" * 37)


def show_rules() -> None:
    print("\n========== GAME RULES ==========")
    print("1. The computer generates a random number.")
    print("2. Guess the number within the given range.")
    print("3. You receive higher/lower hints.")
    print("4. Try to guess in as few attempts as possible.")
    print("5. Choose your difficulty before playing.")
    print("=" * 32)


def start_game() -> None:
    from number_guessing_game.interface.game import play_game
    play_game()


def dashboard() -> None:
    while True:
        display_dashboard()
        choice = get_choice()

        if choice is None:
            continue

        match choice:
            case 1:
                start_game()

            case 2:
                show_high_score()

            case 3:
                show_statistics()

            case 4:
                show_rules()

            case 5:
                print("Thanks for playing!")
                break

            case _:
                print("Invalid option. Choose between 1 and 5.")


if __name__ == "__main__":
    dashboard()
