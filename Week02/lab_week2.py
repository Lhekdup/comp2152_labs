import random

def number_guessing_game():
    targetNumber = random.randint(1, 100)
    while True:
        play = input("Do you want to play number guessing game? yes or no.")
        if play == "yes":
            attempts = 0
            max_attempts = 10

            while attempts < max_attempts:
                try:
                    guess = int(input("Guess the target number: "))
                    attempts += 1
                    if attempts >= max_attempts:
                        print("Game over! The target number was ", targetNumber, ".")
                    elif guess < targetNumber:
                        print("You guessed too low.")
                        continue
                    elif guess > targetNumber:
                        print("You guessed too high.")
                        continue
                    else:
                        print(f"You guessed it after {attempts} tries.")
                    break
                except ValueError:
                    print("Invalid input! Please enter a number between 1 and 100.")
            print(f"Game over! The target number was {targetNumber}.")
            break
        elif play == "no":
            print("Maybe next time!")
            break
        else:
            print("Invalid input! Enter yes or no.")

number_guessing_game()


