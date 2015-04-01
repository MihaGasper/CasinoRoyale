print("Welcome to CASINO ROYALE")

from random import randint

secret = randint(1, 20)

guess="0"

while guess:

    g=raw_input("Guess the number from 1 to 20 and win 1.000.000 $ prize:  ")

    guess=int(g)

    if guess==secret:
        print("Congratulations you just won a million $")
        break
    else:
        print("Better luck next time, try again for just 1$")
        continue