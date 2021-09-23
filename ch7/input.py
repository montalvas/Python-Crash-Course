'''
prompt = "If you tell us who you are, we can personalize the messages you see"
prompt += "\nWhat is your first name: "

name = input(prompt)
print("\nHello, " + name + "!\n")

age = int(input("how old are you? "))
print(age, end="\n\n")

height = float(input("How tall are you, in meters? "))

if height >= 1.50:
    print("\nYou're tall enough to ride!\n")
else:
    print("\nYou're be able to ride when you're a little older.\n") 

number = int(input("Enter a number, and I'll tell you if it's even or odd: "))

if number % 2 == 0:
    print(f"\nThe number {number} is even.\n")
else:
    print(f"\nthe number {number} is odd.\n")
'''

family = int(input('How many people are in your family group? '))

if family > 8:
    print("\nYou must wait a moment.")
else:
    print("\nYour table is set.")