
def madlib():
    adj     = input("Enter an adjective: ").lower()
    animal  = input("Enter the name of your favourite animal: ").capitalize()
    adj1    = input("Enter an adjective: ").lower()
    animal1 = input("Enter the name of an animal: ").capitalize()
    verb    = input("Enter a verb ending with _ing: ").lower()
    noun    = input("Enter a noun: ").lower()
    noun1   = input("Enter a noun: ").lower()

    madlib = f'''The Unlikely Romance of a {adj} {animal}:

Once upon a time, a {adj} {animal} fell in love with a {adj1} {animal1}. Their love story involved {verb} through fields of {noun} and sharing romantic dinners of {noun1}.'''
    
    print(madlib)