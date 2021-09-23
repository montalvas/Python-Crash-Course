'''
prompt = "\nTell me something, and i will repeat it back to you."
prompt += "\n'quit' to end the program."
prompt += "\n"

message = ""

active = True

while active:
    message = input(prompt)
    if message == 'quit':
        active = false
    else:
        print(message)
'''

current_number = 0

while current_number < 10:
    current_number += 1
    if current_number % 2 == 0:
        continue
    else:
        print(current_number)