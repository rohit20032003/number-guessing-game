import random

def number_guessing_game():
    number_to_guess = random.randint(1, 100)
    attempts_allowed = 7
    print("🎯 Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 100.")

    for attempt in range(1, attempts_allowed + 1):
        guess = int(input(f"Attempt {attempt}/{attempts_allowed}: Enter your guess: "))

        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print(f"🎉 Congratulations! You guessed it in {attempt} tries.")
            break
    else:
        print(f"❌ Sorry! The number was {number_to_guess}. Better luck next time!")

number_guessing_game()
