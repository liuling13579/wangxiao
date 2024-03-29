#coding:utf-8
from common.base import Base
import time

class Login(Base):

    loc_user = ("xpath",".//*[@class='account']/input")
    loc_psw = ("xpath",".//*[@class='password']/input")
    loc_button = ("css selector",".submit")
    loc_userinfo = ("class name","index_name-2eduw")
    loc_tishi = ("class name","tip")
    #首页地址
    url_1 = "https://test.1x.cn"

    def input_user(self,user):
        self.sendKeys(self.loc_user,user,True)

    def input_pas(self,pas):
        self.sendKeys(self.loc_psw,pas,True)

    def click_but(self):
        self.click(self.loc_button)

    def get_login_username(self):
        try:
            # time.sleep(5)
            t = self.findElementNew(self.loc_userinfo).text
            print(t)
            return t
        except:
            return "获取用户名失败"

    def get_alert_text(self):
        try:
            a = self.findElementNew(self.loc_tishi).text
            # a = self.driver.find_element_by_class_name("tip").text
            return a
        except:
            return ""

    def login(self,user="yingxiong",pas="123456"):
        self.driver.get(self.url_1)
        self.driver.maximize_window()
        self.input_user(user)
        self.input_pas(pas)
        self.click_but()

if __name__ == "__main__":
    from selenium import webdriver
    driver = webdriver.Chrome()
    L = Login(driver)
    L.login()
    t = L.get_login_username()
    driver.quit()
