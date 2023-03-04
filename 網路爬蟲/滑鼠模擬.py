#action chains ==> https://www.geeksforgeeks.org/action-chains-in-selenium-python/
from turtle import up
from numpy import append
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By

path = "C:/Users/steve/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://tsj.tw/")

blow = driver.find_element(By.ID,"click")
count = driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[2]/h4[2]')#在網頁上==>右鍵 > 複製 > 複製XPATH    #若XPATH的內容有""則 前後要用''不然會衝突

items = []
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[5]/button[1]/i'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[5]/button[1]/i'))
items.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[5]/button[1]/i'))

prices = []
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[4]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[3]/td[4]'))
prices.append(driver.find_element(By.XPATH,'//*[@id="app"]/div[2]/div[4]/div[4]/table/tbody/tr[2]/td[4]'))

actions = ActionChains(driver)

for i in range(100):
    actions.click(blow)#=點擊
    actions.perform() #執行actions的動作
    countnb = int(count.text.replace("您目前擁有","").replace("技術點",""))  #將WebElement轉為文字
    for j in range(3):
        price = int(prices[j].text.replace("技術點",""))
        if price <= countnb:
            uplevelact = ActionChains(driver)
            uplevelact.move_to_element(items[j]) #移動滑鼠到某個地方
            uplevelact.click()
            uplevelact.perform()
            break # 停止迴圈
# driver.close()




