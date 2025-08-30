from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

URL = "https://www.speedtest.net/"

class SpeedTest:
    def get_internet_speed(self):
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        driver = webdriver.Chrome(options=chrome_options)
        driver.get(URL)
        wait = WebDriverWait(driver, 10)
        reject_btn = wait.until(ec.element_to_be_clickable((By.ID, "onetrust-reject-all-handler")))
        reject_btn.click()
        go_btn = wait.until(ec.element_to_be_clickable((By.CLASS_NAME, "start-text")))
        go_btn.click()
        sleep(45)
        download_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]/span').text
        upload_speed = driver.find_element(By.XPATH,'//*[@id="container"]/div[1]/div[3]/div/div/div/div[2]/div[2]/div/div[4]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span').text
        driver.close()
        return (download_speed, upload_speed)
