import random
import smtplib
import datetime as dt
import pandas
import os

my_email = ""
my_password=""
now = dt.datetime.now()
today_tuple = (now.month,now.day)
path = "letter_templates"
dir_list = os.listdir(path)

def prepare_a_card():
    cards_list = []
    for letter in dir_list:
        with open(f"{path}/{letter}") as file:
            cards_list.append(file.read())
    return random.choice(cards_list)

def congratulate_people():
    data = pandas.read_csv("birthdays.csv")
    for person in data.iterrows():
        if (person[1].month,person[1].day) == today_tuple:
            send_message(person[1])

def send_message(person):
    name = person["name"]
    email = person["email"]
    card = prepare_a_card()
    message = card.replace("[NAME]",name)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email,password=my_password)
        connection.sendmail(from_addr=my_email,
                            to_addrs=email,
                            msg=f"Subject:Happy Birthday!\n\n{message}"
        )

congratulate_people()

