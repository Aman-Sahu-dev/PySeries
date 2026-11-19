import random

def number_guess() -> None:
    random_number = random.randint(1,50)
    attempt = 0

    print("welcome to number guessing game")
    print("i have selected number between 1 and 50 guess the number")
   
    while True:
        try:
            user_guess = int(input("enter your guess"))
            attempt+=1;

            if user_guess < 1 or user_guess > 50:
                print("invalid input! please select number between 1 adn 50")
            elif user_guess < random_number:
                print("too low! try again")
            elif user_guess > random_number:
                print("too high! try again")
            else:
                print(f"congratulations you guessed the {random_number} in {attempt} attempt")
                break
        except ValueError:
            print("give valid input")
       
number_guess()
