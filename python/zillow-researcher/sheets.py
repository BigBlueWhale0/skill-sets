import os
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

import time

load_dotenv()

GOOGLE_DOC_URL = os.environ.get("ENV_GOOGLE_DOC_URL")

class Sheets:
    def __init__(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def send_to_sheets(self, properties):
        self.driver.get(GOOGLE_DOC_URL)
        self.wait = WebDriverWait(self.driver, 10)
        for property in properties:
            self.driver.get(GOOGLE_DOC_URL)
            time.sleep(5)
            address = property["address"]
            price = property["price"]
            link = property["link"]
            inputs = self.driver.find_elements(By.CSS_SELECTOR, 'input[type="text"]')
            address_input = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']")))[0]
            address_input.send_keys(address)
            price_input = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']")))[1]
            price_input.send_keys(price)
            link_input = self.wait.until(ec.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text']")))[2]
            link_input.send_keys(link)
            submit_btn = self.driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
            submit_btn.click()

