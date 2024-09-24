import random

def guess_the_number():
    secret_number = random.randint(15, 20)
    play_again = True

    while play_again:
        try:
            guess = int(input("Guess secret number between 15 and 20: "))
        except ValueError:
            print("Enter a valid integer")
            continue

        match guess:
            case _ if guess ==secret_number:
                print("Congratulations, you guessed it right!")
            case _ if guess > secret_number:
                print("Ooop!, Your number is too high. Try again!")
            case _ if guess < secret_number:
                print ("Your number is too low. Try again!")
        
        play_again_input = input("Do you want to play again? (yes or no)").strip().lower()
        if play_again_input != "yes":
            play_again = False
            print("Thanks for playing with us!")

guess_the_number()




