from selenium import webdriver
import os
import time
from random import seed
from random import randint


class InstagramBotRegister:

    def __init__(self, number, fullName, username, password):  # GO DOWN TO SET DATA

        self.number = number
        self.fullName = fullName
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.register()
        time.sleep(2)

    def register(self):
        self.driver.get('https://www.instagram.com/accounts/emailsignup/')
        time.sleep(1)
        self.driver.find_element_by_name('emailOrPhone').send_keys(self.number)
        self.driver.find_element_by_name('fullName').send_keys(self.fullName)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        button = self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(8) > div > button')
        button.click()
        time.sleep(1)


if __name__ == '__main__':
    f = open("user.txt", "a+")
    f.write("USERNAME --> bot" + str(value) + "\n")
    value = randint(0, 100000)
    ig_bot = InstagramBotRegister(
        'PHONE-NUMBER', 'bot' + str(value), 'bot' + str(value), 'PASSWORD')
