import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
load_dotenv()

ACCOUNT_EMAIL = os.environ.get("ENV_ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ENV_ACCOUNT_PASSWORD")
GYM_URL = "https://appbrewery.github.io/gym/"

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
user_data_dir = os.path.join(os.getcwd(), "chrome_profile")
chrome_options.add_argument(f"--user-data-dir={user_data_dir}")

driver = webdriver.Chrome(options=chrome_options)
driver.get(GYM_URL)

wait = WebDriverWait(driver, 2)

def retry(func, retries=7, description=None):
    for i in range(retries):
        print(f"Trying {description}. Attempt: {i + 1}")
        try:
            return func()
        except TimeoutException:
            if i == retries - 1:
                raise
            time.sleep(1)

def login():
    login_btn = wait.until(ec.element_to_be_clickable((By.ID, "login-button")))
    login_btn.click()

    email_input = wait.until(ec.presence_of_element_located((By.ID, "email-input")))
    email_input.clear()
    email_input.send_keys(ACCOUNT_EMAIL)

    password_input = driver.find_element(By.ID, "password-input")
    password_input.clear()
    password_input.send_keys(ACCOUNT_PASSWORD)

    submit_btn = driver.find_element(By.ID, "submit-button")
    submit_btn.click()

    wait.until(ec.presence_of_element_located((By.ID, "schedule-page")))

def book_class(booking_button):
    booking_button.click()
    wait.until(lambda d: booking_button.text == "Booked")

retry(login, description="login")

booked_count = 0
waitlist_count = 0
already_booked_count = 0
booking_list = []
waiting_list = []

class_cards = driver.find_elements(By.CSS_SELECTOR, "div[id^='class-card-']")
for card in class_cards:
    day_group = card.find_element(By.XPATH, "./ancestor::div[contains(@id, 'day-group-')]")
    day_title = day_group.find_element(By.TAG_NAME, "h2").text

    if "Tue" in day_title or "Thu" in day_title:
        time_text = card.find_element(By.CSS_SELECTOR, "p[id^='class-time-']").text
        if "6:00 PM" in time_text:
            class_name = card.find_element(By.CSS_SELECTOR, "h3[id^='class-name-']").text
            button = card.find_element(By.CSS_SELECTOR, "button[id^='book-button-']")
            button_status = button.text
            if button_status == "Booked":
                print(f"✓ Already booked: {class_name} on {day_title}")
                already_booked_count += 1
            elif button_status == "Waitlisted":
                print(f"✓ Already on waitlist: {class_name} on {day_title}")
                already_booked_count += 1
            elif button_status == "Book Class":
                retry(lambda: book_class(button), description="Booking")
                print(f"✓ Booked: {class_name} on {day_title}")
                booked_count += 1
                booking_list.append(f"• [New Booking] {class_name} on {day_title}")
            elif button_status == "Join Waitlist":
                retry(lambda: book_class(button), description="Waitlisting")
                waitlist_count += 1
                print(f"✓ Joined waitlist for: {class_name} on {day_title}")
                waiting_list.append(f"• [New Waitlist] {class_name} on {day_title}")
            break

total_booked = already_booked_count + booked_count + waitlist_count
print(f"\n--- Total Tuesday/Thursday 6pm classes: {total_booked} ---")
print("\n--- VERIFYING ON MY BOOKINGS PAGE ---")

my_booking_button = driver.find_element(by=By.ID, value="my-bookings-link").get_attribute("href")
driver.get(my_booking_button)
wait.until(ec.presence_of_element_located((By.ID, "my-bookings-page")))
verified_count = 0
all_cards = driver.find_elements(By.CSS_SELECTOR, "div[id*='card-']")
for card in all_cards:
    try:
        when_paragraph = card.find_element(By.XPATH, ".//p[strong[text()='When:']]")
        when_text = when_paragraph.text
        if ("Tue" in when_text or "Thu" in when_text) and "6:00 PM" in when_text:
            class_name = card.find_element(By.TAG_NAME, "h3").text
            print(f"  ✓ Verified: {class_name}")
            verified_count += 1
    except NoSuchElementException:
        pass

print(f"\n--- VERIFICATION RESULT ---")
print(f"Expected: {total_booked} bookings")
print(f"Found: {verified_count} bookings")

if total_booked == verified_count:
    print("✅ SUCCESS: All bookings verified!")
else:
    print(f"❌ MISMATCH: Missing {total_booked - verified_count} bookings")

print(f"""
--- BOOKING SUMMARY ---
Classes booked: {booked_count}
Waitlists joined: {waitlist_count}
Already booked/waitlisted: {already_booked_count}
Total Tuesday/Thursday 6pm classes processed: {booked_count + waitlist_count + already_booked_count}
""")

print(f"""
--- DETAILED CLASS LIST ---
{"\n".join(booking_list)}
{"\n".join(waiting_list)}
""")
