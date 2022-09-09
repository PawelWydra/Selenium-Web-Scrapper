from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import csv

chrome_driver_path = "C:/Users/Pawel/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://soundcloud.com/")
accept_cookie = driver.find_element(By.ID, "onetrust-accept-btn-handler")
accept_cookie.click()
time.sleep(3)

texts = [el.text for el in driver.find_elements(By.CLASS_NAME, "playableTile__descriptionContainer")]
driver.quit()


with open('test.csv', mode='w', encoding='UTF8', newline='') as file:
    file.write("Artist - Song")
    file.write('\n\n')
    for line in texts:
        file.write(line)
        file.write('\n')
print("done")