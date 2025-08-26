import os
from dotenv import load_dotenv
import smtplib

load_dotenv()

SMTP_FROM_EMAIL = os.environ.get("ENV_SMTP_FROM_EMAIL")
SMTP_PASSWORD = os.environ.get("ENV_SMTP_PASSWORD")

class NotificationManager:
    def send_message(self,email,message):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=SMTP_FROM_EMAIL, password=SMTP_PASSWORD)
            connection.sendmail(from_addr=SMTP_FROM_EMAIL,
                                to_addrs=email,
                                msg=f"Subject:Flight Price Alert!\n\nLow price alert! {message}"
                                )