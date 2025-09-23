import datetime
import requests

class Holidays:
    def __init__(self, countryCode):
        self.countryCode = countryCode
        self.dataHolidays = []
        self.nationalHolidays = []
        self.release_date = ""
        self.release_end_date = ""

    def find_all_holidays(self):
        params = {
            "countryIsoCode": self.countryCode,
            "validFrom": self.release_date,
            "validTo": self.release_end_date,
            "languageIsoCode": "EN",
        }
        response = requests.get(f"https://openholidaysapi.org/PublicHolidays", params=params, verify=False)
        self.dataHolidays = response.json()


    def get_holidays_list(self):
        holidays = []
        for holiday in self.dataHolidays:
            holiday_name = holiday["name"][0]["text"]
            holiday_date = holiday["startDate"]
            holiday_national = holiday["regionalScope"]
            if holiday_national == "National":
                holidays.append({"holiday_name": holiday_name, "holiday_date": holiday_date})
        self.nationalHolidays = holidays

    def check_the_date(self,release_date):
        if len(self.nationalHolidays) == 0:
            print(f"You can release your updates in {release_date} in {self.countryCode} region")
        for holiday in self.nationalHolidays:
            if release_date == self.release_end_date:
                break
            if holiday["holiday_date"] == release_date:
                new_date = datetime.datetime.strptime(release_date, "%Y-%m-%d") + datetime.timedelta(days=1)
                self.check_the_date(new_date.strftime("%Y-%m-%d"))
            else:
                print(f"You can release your updates in {release_date} in {self.countryCode} region")
            break






