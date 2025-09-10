import os
from string import punctuation
from zipfile import ZipFile

def analyze_file(func):
    global search_word
    def wrapper(*args):
        sum_word_count = 0
        word_lines = []
        file_content, file_name = func(*args)
        for line_number,row in enumerate(file_content):
            words_collection = [word_in_line.strip(punctuation) for word_in_line in row.split()]
            search_word_count = words_collection.count(search_word)
            sum_word_count += search_word_count
            if search_word_count > 0:
                word_lines.append(line_number+1)
        if sum_word_count != 0:
            print(f"The file {file_name} consists of the word {search_word} {sum_word_count} times in lines {','.join(str(number) for number in word_lines)}")
    return wrapper

@analyze_file
def check_file(file_name):
    with open(f"data/{file_name}") as file:
        file_content = file.readlines()
    return file_content, file_name


with ZipFile("data.zip") as file:
    file.extractall()
search_word = input("Write a word to search: ")

files_list = os.listdir("data")
for file in files_list:
    check_file(file)
