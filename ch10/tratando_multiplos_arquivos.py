def count_words(filename):
    """Conta a quantidade de palavras de um arquivo

    Args:
        filename (str): 'nome_do_arquivo.txt'
    """
    try:
        with open(filename, encoding='utf-8') as file_object:
            content = file_object.read()
    except FileNotFoundError:
        print(f"Sorry, this file {filename} doesn't exist.")
    else:
        words = content.split()
        number_words = len(words)
        print(f"The file {filename} has about {number_words} words.")


books = ['fabula.txt', 'poema.txt', 'sherlock.txt']

for book in books:
    count_words(book)
