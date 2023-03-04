from turtle import title
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
path = "C:/Users/steve/Downloads/chromedriver_win32/chromedriver.exe" #chromedriver位置
driver = webdriver.Chrome(path)

driver.get("https://dcard.tw/f") #目標頁面
print(driver.title) #網頁title
#search = driver.find_element_by_name("query") ==>這東西python已棄用
search = driver.find_element(By.NAME,"query") #要用這個,搜尋某個標籤
search.clear()#清空搜尋欄位
search.send_keys("比特幣") #輸入內容

search.send_keys(Keys.RETURN)#=enter鍵,按完enter後需要時間才會產生標籤

element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, "sc-e1542747-0"))) #系統搜尋到某些東西時才繼續進行

titles = driver.find_elements(By.CLASS_NAME,"sc-d305c7ef-3")
for title in titles:
    print(title.text)

link = driver.find_element(By.LINK_TEXT,"比特幣是騙局") #尋找連結中文字
link.click()#點擊滑鼠
time.sleep(1)
driver.back()#回上一頁
time.sleep(1)
driver.forward()#到下一頁
time.sleep(1)#暫停程式時間 
driver.quit() #關閉網頁 
