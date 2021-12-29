import pandas

file = pandas.read_csv('nato-phonetic-alphabet.csv')

alphabet_dict = {row.letter: row.code for (index, row) in file.iterrows()}
print(alphabet_dict)


def generate_phonetic():
    word = input("Enter a word: ").upper()
    try:
        letters_in_word = [alphabet_dict[letter] for letter in word.upper()]
    except KeyError:
        print("Sorry, only letters please.")
        generate_phonetic()
    else:
        print(letters_in_word)


generate_phonetic()
