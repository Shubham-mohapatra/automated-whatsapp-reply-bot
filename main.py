import time
import random
import json
import logging
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

logging.basicConfig(filename="whatsapp_bot.log", level=logging.INFO)

with open("config.json", "r") as file:
    config = json.load(file)

service = Service(config["chromedriver_path"])
driver = webdriver.Chrome(service=service)

def send_message(name):
    try:
        search_box = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='side']/div[1]/div/label/div/div[2]"))
        )
        search_box.click()
        time.sleep(1)
        search_box.send_keys(name)
        time.sleep(2)

        user = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f'//span[@title="{name}"]'))
        )
        user.click()

        unread_msgs = driver.find_elements(By.XPATH, "//span[@class='_31gEB']")
        if not unread_msgs:
            logging.info(f"No unread messages for {name}. Skipping...")
            return

        textbox = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'))
        )
        message_template = random.choice(config["message_templates"])
        personalized_message = message_template.format(name=name)
        textbox.send_keys(personalized_message)
        time.sleep(1)

        send_button = driver.find_element(By.XPATH, '//*[@id="main"]/footer/div[1]/div[3]/button')
        send_button.click()
        logging.info(f"Message sent to {name}")
    except Exception as e:
        logging.error(f"Error with contact {name}: {e}")

driver.get("https://web.whatsapp.com/")
print("Scan the QR code within 60 seconds...")
WebDriverWait(driver, 60).until(
    EC.presence_of_element_located((By.ID, "side"))
)
print("QR code scanned successfully!")

try:
    while True:
        for name in config["contacts"]:
            send_message(name)
            time.sleep(random.uniform(5, 10))

        logging.info("Waiting for 5 minutes before the next round...")
        time.sleep(300)
except KeyboardInterrupt:
    logging.info("Bot stopped by user.")
finally:
    driver.quit()
