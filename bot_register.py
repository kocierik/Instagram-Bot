import prova
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os
import time
from random import seed
from random import randint
from urllib.request import urlopen
import re
import sys
sys.path.insert(0, 'prova.py')


class InstagramBotRegister:

    def __init__(self, number, fullName, username, password):  # GO DOWN TO SET DATA

        self.number = number
        self.fullName = fullName
        self.username = username
        self.password = password

        self.driver = webdriver.Chrome('./chromedriver.exe')
        self.register()
        time.sleep(10)
        code = prova.InstagramBotRegister1.register1(
            self, "https://www.receivesms.co/italian-phone-number/3350/")
        time.sleep(3)
        try:
            self.code_verify(code)
        except Exception as e:
            print("errore numero")
    def register(self):
        self.driver.get('https://www.instagram.com/accounts/emailsignup/')
        time.sleep(2)
        self.driver.find_element_by_name('emailOrPhone').send_keys(self.number)
        self.driver.find_element_by_name('fullName').send_keys(self.fullName)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        button1 = self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > article > div > div:nth-child(1) > div > form > div:nth-child(8) > div > button')
        button1.click()
        time.sleep(2)

    def code_verify(self, code):
        self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > article > div > div:nth-child(1) > div > div > div > form > div.TfHme > div > label > input').send_keys(code)
        final = self.driver.find_element_by_css_selector(
            '#react-root > section > main > div > article > div > div:nth-child(1) > div > div > div > form > div.Igw0E.IwRSH.eGOV_._4EzTm.MGdpg.CovQj.jKUp7 > button')
        final.click()
        time.sleep(2)
        self.driver.find_element_by_id(
            'igCoreRadioButtonageRadioabove_18').click()
        time.sleep(1)
        self.driver.find_element_by_css_selector(
            'body > div.RnEpo.Yx5HN > div > div._0GT5G > div > button').click()


if __name__ == '__main__':

    f = open("user.txt", "a+")
    value = randint(0, 100000)
    f.write("INSERT-USERNAME" + str(value) + "\n")
    ig_bot = InstagramBotRegister(
        'INSERT-NUMBER', 'INSERT-NAME' + str(value), 'INSERT-USERNAME PLUS NUMBER-RANDOM ->' + str(value), 'INSERT-THE-PASSWORD')
