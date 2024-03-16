import random


secret_number = random.randint(1, 10)
user_guess = 0
guess_count = 0
guess_limit = 3
out_of_guesses = False
feedback_list = []

while user_guess != secret_number and not(out_of_guesses):
    if guess_count < guess_limit:
        if guess_count == 0:
            print("Hint 1: Enter a number between [1, 10]")
        elif guess_count == 1:
            print("Hint 1: Enter a number between [1, 10]")
            print(feedback_list[0])
        elif guess_count == 2:
            print("Hint 1: Enter a number between [1, 10]")
            print(feedback_list[0])
            print(feedback_list[1])

        user_guess = int(input("Enter Your Lucky Guess: "))
        guess_count += 1

        if user_guess > secret_number:
            f = f"Hint 2: The number is smaller than {user_guess}"
            feedback_list.append(f)
        elif user_guess < secret_number:
            f = f"Hint 3: The number is bigger than {user_guess}"
            feedback_list.append(f)

    else:
        out_of_guesses = True
    
if out_of_guesses:
    print("Out of guesses, YOU LOOSE!")
else:
    print("Congratulations, YOU WON!")
