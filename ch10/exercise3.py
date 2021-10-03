filename = 'dracula.txt'

try:
    with open(filename, encoding='utf-8') as file_object:
        content = file_object.read()
except FileNotFoundError:
    print(f"Sorry, the file {filename} doesn't exist.")
else:
    key_word = "vampire"
    words = content.split()
    print(f"The word {key_word} appears {words.count(key_word)} times in {filename} file.")