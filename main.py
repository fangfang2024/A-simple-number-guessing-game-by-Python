import random
from art import logo

easy_attempts = 10
difficult_attempts = 5

def secret_number_generate():
    secret_number = random.randint(1, 101)
    return secret_number

def set_difficulties():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    if level == "easy":
        return easy_attempts
    else:
        return difficult_attempts

def check_the_answer(user_input, actual_number):
    if user_input != actual_number:
        if user_input < actual_number:
            print("Too low")
        elif user_input > actual_number:
            print("Too high")
        return 0
    else:
        return 1

def play_game():
    print(logo)
    print(
    '''Welcome to the secret number guessing game.
    I'm thinking about a number between 1 to 100.
    ''')
    answer = secret_number_generate()
    print(f"Pssst, the correct answer is {answer}")
    attempts = set_difficulties()
    while attempts != 0:
        print (f"You have {attempts} left.")
        guess = int(input("Make a guess: "))
        result = check_the_answer(guess,answer)
        if result == 0:
            attempts -= 1
            if attempts == 0:
                print("You are running out of attempts. Game over")
                break
            else:
                print("Try again.")

        elif result == 1:
            print(f"You won. The secret number is {answer}.")
            break

play_game()



