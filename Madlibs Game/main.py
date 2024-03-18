from sample_madlibs import misadventure, poem, office, romance
import random


if __name__ == "__main__":
    madlib = random.choice([misadventure(), poem(), office(), romance()])
    print(madlib)

