from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os
import wget

path = "C:/Users/steve/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.XPATH,'//*[@id="loginForm"]/div/div[3]')))

username = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')
pw = driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')
username.clear()
pw.clear()

username.send_keys('stevenwsp901007@gmail.com')
pw.send_keys('970222')

driver.find_element(By.XPATH,'//*[@id="loginForm"]/div/div[3]/button').click()

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'_aauy')))

serch = driver.find_element(By.CLASS_NAME,'_aauy')

keyword = '#cat'

serch.send_keys(keyword)

time.sleep(5)
serch.send_keys(Keys.RETURN)
time.sleep(3)
serch.send_keys(Keys.RETURN)
# time.sleep(1)
# serch.send_keys(Keys.RETURN)

element = WebDriverWait(driver, 20).until(EC.presence_of_element_located((By.CLASS_NAME,'x5yr21d')))

imgs = driver.find_elements(By.CLASS_NAME,'x5yr21d')

path = os.path.join(keyword) 
os.mkdir(path) 
count = 0

for img in imgs:
    save_as = os.path.join(path,keyword + str(count) + '.jpg')
    # print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"),save_as)
    count += 1