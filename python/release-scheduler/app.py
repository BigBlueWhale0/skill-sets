import datetime
from holidays import Holidays

RELEASE_PERIOD = 7
countries = ["ES", "FR", "IT"]

is_not_correct = True

while is_not_correct:
    release_date = input("Write the release date in format year-mm-dd: ")
    try:
        release_end_date = (datetime.datetime.strptime(release_date, "%Y-%m-%d") + datetime.timedelta(days=RELEASE_PERIOD)).strftime("%Y-%m-%d")
        is_not_correct = False
    except ValueError:
        print("You have typed the wrong date, please try it again")
        is_not_correct = True

for country in countries:
    county_holidays = Holidays(country)
    county_holidays.release_date = release_dates
    county_holidays.release_end_date = release_end_date
    county_holidays.find_all_holidays()
    county_holidays.get_holidays_list()
    county_holidays.check_the_date(release_date)

