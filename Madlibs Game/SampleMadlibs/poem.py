
def madlib():
    flower = input("Enter a flower's name: ").capitalize()
    color  = input("Enter a color: ").lower()
    person = input("Enter the name of a person you love: ").title()

    madlib = f'''{flower} are red;
Violets are {color};
I love {person}!'''
    
    print(madlib)