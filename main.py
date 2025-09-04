import random

print("Welcome to the Number Guessing Game: ")
name = input("Enter your name: ")


def guess_game():
    print("Guess a random no. between 1-100 Good luck😄")
    number = random.randint(1, 100)
    for i in range(1, 8):  # 7 tries
        try:
            guessed_number = int(input(f"Attempt {i}: Enter your Guess: "))
        except ValueError:
            print("❌ Please enter a valid number!")
            continue

        if guessed_number not in range(1, 101):
            print("⚠️ Enter a number within 1–100")
            continue

        if guessed_number == number:
            print(f"🎉 Congrats {name}! You guessed it in {i} tries!")
            return
        elif guessed_number < number:
            print("Too low! Try again.")
        else:
            print("Too high! Try again.")

    print(f"😢 Sorry {name}, you're out of tries. The number was {number}.")


while True:
    game_state = input(name + ", do you want to play the game? (y/n): ")
    if game_state.lower() != "y":
        print("Thank You For Playing")
        break
    guess_game()
