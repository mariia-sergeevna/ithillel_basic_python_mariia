from random import randint

number = randint(1, 10)

while True:
    number_input = int(input("Guess the number from 1 to 10 and enter it: "))
    if number_input == number:
        print(f"You guessed it! :) it's {number} ")
        break
    else:
        print("It's not it. Try again")
