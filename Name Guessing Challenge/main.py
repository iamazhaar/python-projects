secret_name = "nikola tesla"
user_guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

print("Guess the person's name;you have three chances.")

while user_guess != secret_name and not(out_of_guesses):
    if guess_count < guess_limit:
        if guess_count == 0:
            print("Hint: He was born in July 10th 1856 during a lightning storm")
        elif guess_count == 1:
            print("Hint 1: He was born in July 10th 1856 during a lightning storm")
            print("Hint 2: Known as the wizard of electricity")
        elif guess_count == 2:
            print("Hint 1: He was born in July 10th 1856 during a lightning storm")
            print("Hint 2: Known as the wizard of electricity")
            print("Hint 3: His name starts with the letter 'N'")
        
        user_guess = input("Enter Your Lucky Guess: ").casefold()
        guess_count += 1
        
    else:
        out_of_guesses = True



if out_of_guesses:
    print("Out of guesses, YOU LOOSE!")
else:
    print("Congratulations, YOU WON!")
