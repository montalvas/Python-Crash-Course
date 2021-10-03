file_name = 'sherlock.txt'

try:
    with open(file_name, encoding='utf-8') as file_object:
        content = file_object.read()
except FileNotFoundError:
    print("Sorry, this file doesn't exist.")
else:
    words = content.split()
    number_words = len(words)
    print(f"The file {file_name} has about {number_words} words.")