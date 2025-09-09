from fileManager import fileManager

ZIP_FILE = "data.zip"

data_files = fileManager(ZIP_FILE)
files_list = data_files.get_files_list()

search_word = input("Write a word to search: ")
data_files.search_word = search_word

for file in files_list:
    data_files.check_file(file)

print(data_files.statistic_report)