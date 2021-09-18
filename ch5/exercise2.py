playerGuess = input("What color is the alien(green/red/yellow)? ")
points = 0

if playerGuess == 'green':
    points = 5
else:
    points = 10

print(f"Your shoot a {playerGuess} alien and got {points} points")