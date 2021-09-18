from random import choice

colors = ['red', 'green', 'yellow']
chosenColor = choice(colors)

playerGuess = input("Which color do you choose: green, red or yellow? ")

if playerGuess == chosenColor:
    print("Congratulations! Your guess is correct.")
else:
    print("Sorry, your missed your guess.")