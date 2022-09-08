from selenium import webdriver

chrome_driver_path = "C:/Users/Pawel/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://soundcloud.com/")

data = driver.find_element(By.XPATH, "//*[@id=&quote;content&quote;]/div/div/div[2]/div/div[2]/div[2]/ul/li[1]/div/div[2]/div[1]/a")
driver.close()
driver.quit()