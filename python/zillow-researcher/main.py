from zillow import Zillow
from sheets import Sheets

zillow = Zillow()
sheets = Sheets()
properties_data = zillow.collect_details()
print(f"There were found {len(properties_data)} properties")
sheets.send_to_sheets(properties_data)