
def misadventure():
    name  = input("Enter a name: ")
    noun1 = input("Enter a noun: ")
    adj   = input("Enter an adjective: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    noun4 = input("Enter a noun: ")

    return f'''The Misadventures of {name}'s Grocery Shopping Trip:

{name} went to the store to buy {noun1} but ended up finding a {adj} {noun2} instead. They tried to pay with {noun3} but the cashier demanded {noun4} in exchange!'''
    


def poem():
    flower = input("Enter a flower's name: ")
    color  = input("Enter a color: ")
    person = input("Enter the name of a person you love: ")

    return f'''{flower} are red;
Violets are {color};
I love {person}!'''
    

def office():
    noun1 = input("Enter a noun: ")
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")

    return f'''The Hilarious Office Memo:
          
The boss sent out a memo demanding that all employees must bring {noun1} to the next meeting. However, instead of {noun2}, everyone brought {noun3} and chaos ensued!'''
    

def romance():
    adj     = input("Enter an adjective: ")
    animal  = input("Enter the name of your favourite animal: ")
    adj1    = input("Enter an adjective: ")
    animal1 = input("Enter the name of an animal: ")
    verb    = input("Enter a verb ending with _ing: ")
    noun    = input("Enter a noun: ")
    noun1   = input("Enter a noun: ")

    return f'''The Unlikely Romance of a {adj} {animal}:

Once upon a time, a {adj} {animal} fell in love with a {adj1} {animal1}. Their love story involved {verb} through fields of {noun} and sharing romantic dinners of {noun1}.'''
    
