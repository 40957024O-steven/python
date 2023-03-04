import os
from pickle import TRUE
import re


class phone: #class只是模板
    def __init__(self,sys,number,waterproof):
        self.sys = sys
        self.number = number 
        self.waterproof = waterproof
    def is_ios(self):
        if self.sys == "ios":
            return True
        elif self.sys == "安卓":
            return False
    def add (self,a,b):
        return a+b

iphone = phone("ios",13,True)
sony = phone("安卓","M13",False)
print (iphone.sys)#取得資料
print (sony.number)
print (sony.is_ios())
print (sony.add(7,10))