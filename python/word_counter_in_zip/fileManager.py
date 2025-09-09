import os
from zipfile import ZipFile
from string import punctuation

class fileManager():
    def __init__(self, file_name):
        self.search_word = ""
        self.file_name = file_name
        self.statistic_report = {}
        self.folder_name = os.path.splitext(file_name)[0]
        is_folder_exist = os.path.exists(self.folder_name)
        is_ready = False
        if is_folder_exist:
            while not is_ready:
                rewrite = input(f"The folder {self.folder_name} exists already. Do you want to recreate it? Type yes or no: ")
                if rewrite == "no":
                    is_ready = True
                    return
                elif rewrite == "yes":
                    is_ready = True
                else:
                    print(f"You've written the incorrect word.")
        self._unzip()

    def _unzip(self):
        with ZipFile(self.file_name) as file:
            file.extractall()

    def get_files_list(self):
        return os.listdir(self.folder_name)

    def check_file(self, file_name):
        word_lines = []
        sum_word_count = 0
        with open(f"{self.folder_name}/{file_name}") as file:
            file_rows = file.readlines()
        for line_number,row in enumerate(file_rows):
            words_collection = [word_in_line.strip(punctuation) for word_in_line in row.split()]
            search_word_count = words_collection.count(self.search_word)
            sum_word_count += search_word_count
            if search_word_count > 0:
                word_lines.append(line_number+1)
        if sum_word_count != 0:
            self.statistic_report[file_name] = {"count": sum_word_count, "lines": word_lines}
