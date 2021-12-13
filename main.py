import pandas

file = pandas.read_csv('nato-phonetic-alphabet.csv')
alphabet_frame = pandas.DataFrame(file)
alphabet_dict = {row.letter: row.code for (index, row) in alphabet_frame.iterrows()}
print(alphabet_dict)

word = input("Enter a word: ")
letters_in_word = [alphabet_dict[letter] for letter in word.upper()]
print(letters_in_word)
