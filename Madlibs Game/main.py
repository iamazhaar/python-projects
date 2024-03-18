from SampleMadlibs import misadventure, poem, office, romance
import random


if __name__ == "__main__":
    file = random.choice([misadventure, poem, office, romance])
    
    file.madlib()

