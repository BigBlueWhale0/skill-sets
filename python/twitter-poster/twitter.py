import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, TimeoutException
import time
load_dotenv()

TWITTER_EMAIL = os.environ.get("ENV_TWITTER_EMAIL")
TWITTER_USERNAME = os.environ.get("ENV_TWITTER_USERNAME")
TWITTER_PASSWORD = os.environ.get("ENV_TWITTER_PASSWORD")
URL = "https://x.com/i/flow/login"

class Twitter:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(URL)
        self.wait = WebDriverWait(driver, 10)
        driver.fullscreen_window()
        self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(TWITTER_EMAIL)
        driver.find_element(By.XPATH, value = "//span[text()='Next']").click()
        try:
            self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@name='text']"))).send_keys(TWITTER_USERNAME)
            driver.find_element(By.XPATH, "//span[text()='Next']").click()
        finally:
            self.wait.until(ec.presence_of_element_located((By.XPATH, "//input[@name='password']"))).send_keys(TWITTER_PASSWORD)
            driver.find_element(By.XPATH, "//span[text()='Log in']").click()

    def post_a_message(self,message):
        self.wait.until(ec.presence_of_element_located((By.CSS_SELECTOR, 'div[aria-label="Post text"]'))).send_keys(f"{message}.")
        self.wait.until(ec.element_to_be_clickable((By.CSS_SELECTOR, 'div[data-testid="toolBar"] button[data-testid="tweetButtonInline"]'))).click()
