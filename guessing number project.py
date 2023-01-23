'''actual_number = 45
attempts = 0

while True:
    attempts +=1
    guess = int(input("Guess the number:\n"))
    if guess < actual_number:
        print("Your guess was too low")

    elif guess > actual_number:
        print("Your guess was too high")

    else:
        print(f"you guessed the number in {attempts} attempts")
        break
print("Thanks for playing!")
    '''


import random as r


def guessingTheNumber():
    attempts = 0
    number = r.randint(25, 100)
    while True:
        g = int(input('Guess the number\n'))
        attempts += 1
        if g > number+10:
            print('your guess is way larger than the number')
        elif g > number:
            print('your guess is larger than the number ')
        elif g < number-10:
            print('your guess is way smaller than the number')
        elif g < number:
            print('your guess is smaller than the number ')
        if g == number:
            print('your guess was correct !!')
            print(f'you guessed the number in {attempts} attempts')


guessingTheNumber()


'''
actualNumber = 45
attempts = 1
guessNumber = int(input("I am thinking of a number between 1 and 50. What is the number i AM THINKING OF?\n"))

while guessNumber != actualNumber:
    attempts +=1
    
    if guessNumber<actualNumber:
        print(f"Your number, {guessNumber} is too low")
        guessNumber = int(input("Try again!\n"))
    elif guessNumber>actualNumber:
        print(f"Your number, {guessNumber} is too high")
        guessNumber = int(input("Try again!\n"))
else:
    print(f"Congratulations!, {guessNumber} is the number and you guess it from {attempts} attempts")
'''


'''
actual_number = int(input("Enter the actual number "))
attempts = 0

while True:
    attempts +=1
    guess = int(input("Guess the number "))
    if guess>actual_number:
        print("Your guess is too high!, Guess again")
    elif guess<actual_number:
        print("Your guess is too low!,Guess again")
    else:
        print("Congratulations you have guessed the correct nummber in ",attempts, "attempts")
        break
'''
