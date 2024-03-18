
def madlib():
    name  = input("Enter a name: ").title()
    noun1 = input("Enter a noun: ")
    adj   = input("Enter an adjective: ").lower()
    noun2 = input("Enter a noun: ")
    noun3 = input("Enter a noun: ")
    noun4 = input("Enter a noun: ")

    madlib = f'''The Misadventures of {name}'s Grocery Shopping Trip:

{name} went to the store to buy {noun1} but ended up finding a {adj} {noun2} instead. They tried to pay with {noun3} but the cashier demanded {noun4} in exchange!'''
    
    print(madlib)

