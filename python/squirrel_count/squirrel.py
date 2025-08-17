import pandas

DATA_SOURCE = "2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv"

class Squirrel:
    def __init__(self):
        self.data = pandas.read_csv(DATA_SOURCE)
        self.report = {}

    def get_fur_list(self):
        fur_colors = self.data["Primary Fur Color"].unique().tolist()
        color_list = [color for color in fur_colors if isinstance(color,str)]
        self.report["Fur Color"] = color_list
        return color_list

    def count_colors(self, fur_colors):
        color_count = []
        for color in fur_colors:
            color_count.append(len(self.data[self.data["Primary Fur Color"] == color]))
        self.report["Count"] = color_count

    def create_report(self):
        data = pandas.DataFrame(self.report)
        data.to_csv("squirrel_count.csv")
