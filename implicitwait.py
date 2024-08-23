import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
driver = webdriver.Chrome(service=Service("Driver//chromedriver.exe"))
driver.maximize_window()
driver.get("https://www.demoblaze.com/")

nav_login=driver.find_element(By.ID,"login2")
nav_login.click()



uname = WebDriverWait(driver,10).until(ec.element_to_be_clickable((By.ID,"loginusername" )))
uname.send_keys("testmorning")
pwd = driver.find_element(By.ID,"loginpassword")
pwd.send_keys("test123")

button = driver.find_element(By.XPATH,'//*[@id="logInModal"]/div/div/div[3]/button[2]')
button.click()
time.sleep(10)



