class Letter():
    def __init__(self):
        self.guests_list = []

    def guest_list(self):
        with open("Input/Names/invited_names.txt") as file:
            self.guests_list = file.readlines()
        return self.guests_list

    def prepare_letter(self,name):
        self.name = name.strip()
        with open("Input/Letters/starting_letter.txt") as file:
            return file.read().replace("[name]",self.name)

    def create(self,name,letter):
        with open(f"Output/ReadyToSend/{name.strip()}.txt", mode="w") as file:
            file.write(letter)