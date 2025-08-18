import pandas

student_data_frame = pandas.read_csv("nato_phonetic_alphabet.csv")

new_dict_alph = {row.letter:row.code for (index, row) in student_data_frame.iterrows()}

def generate_code():
    try:
        word = input("Enter a word:  ")
        output_list = [new_dict_alph[letter.upper()] for letter in word]
    except KeyError as error_key:
        print(f"You have used the wrong symbol {error_key}. Please try again")
        generate_code()
    else:
        print(output_list)

generate_code()

