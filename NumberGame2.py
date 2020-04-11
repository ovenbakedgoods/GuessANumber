import random

number_of_guesses = 0

name = input('Are you feeling lucky? Step right up and guess a number! First what is your name?')

print(name + ', help me set some limits on this number')
x = int(input('Whats the smallest number to be included?'))
y = int(input('Whats the largest number to be included? '))

number = random.randint(x, y)
while number_of_guesses < 6:
    guess = input("Take a guess ")
    guess = int(guess)

    number_of_guesses = number_of_guesses + 1
    guesses_left = 6 - number_of_guesses

    if guess < number:
        guesses_left = str(guesses_left)
        print("Your guess is too low! You have ", guesses_left, ' guesses left')

    if guess > number:
        guesses_left = str(guesses_left)
        print("Your guess is too high! you have",guesses_left,'guesses left')

    if guess == number:
        print("That's the number I was thinking!")
        number_of_guesses = str(number_of_guesses)
        print("Good job! You guessed the number in {} tries",format(number_of_guesses))
        break

if guess != number:
    number = str(number)
    print('\n Sorry. The number I was thinking of was',number)