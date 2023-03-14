from PIL import Image,ImageOps
import numpy as np

path = "C:/Users/steve/Desktop/GitHub/python/資料處理/圖片處理/ntnu.png"

img = Image.open(path).convert('L')# 讀取圖片，並轉換為灰度圖像

img_data = np.array(img)# 轉換為數值資料

colorized_img = ImageOps.colorize(img, (255,255,255), (255, 0, 0))# 調整灰度
# print(img_data.shape)# 檢查形狀

colorized_img.save("C:/Users/steve/Desktop/GitHub/python/資料處理/圖片處理/ntnu_2.png")
