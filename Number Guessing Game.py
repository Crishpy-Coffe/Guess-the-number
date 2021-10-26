import random


def guessing():
    num = 0
    guess = 0
    while num != hid_num:
        num = int(input("Guess number : "))
        guess += 1
        if num == hid_num:
            print(f"Congrats you win in {guess} guesses")
            return guess
        elif num > hid_num:
            print(f"Guess any lower number")
            continue
        elif num < hid_num:
            print(f"Guess any higher number")
            continue
        else:
            print("Invalid Input")
            continue


if __name__ == '__main__':

    print("**** Number Guessing Game ****")
    a = int(input("Enter the first number : "))
    b = int(input("Enter the second number : "))

    hid_num = random.randrange(a, b)
    actual1 = hid_num
    print(f"Player 1\nGuess the number between {a} and {b}")
    p1 = guessing()
    hid_num = random.randrange(a, b)
    actual2 = hid_num
    print(f"Player 2\nGuess the number between {a} and {b}")
    p2 = guessing()

    if p1 == p2:
        print("Match Draw")
    elif p1 > p2:
        print(f"Player 2 won the mathch with {p1 - p2} less guess")
    elif p1 < p2:
        print(f"Player 1 won the mathch with {p2 - p1} less guess")

    print(f"The real number of Player 1 is {actual1} and Player 2 is {actual2}")