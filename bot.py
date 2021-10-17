from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import os
import time
import geckodriver_autoinstaller


class InstagramBot:

    def __init__(self, username, password, user):
        """
        date:
            username ---> nome instagram dell'utente
            password ---> password dell'utente              GO DOWN TO SET THE DATA 
            user     ---> utente da seguire
        attribute:
            driver:selenium.webdriver.chrome ---> permette di eseguire chrome

        """

        self.username = username
        self.password = password
        self.user = user
        geckodriver_autoinstaller.install()
        options = Options()
        self.driver = webdriver.Firefox(options=options)
        # self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()
        time.sleep(2)
        self.base_url = "https://www.instagram.com"
        self.nav_user(user)
        time.sleep(1)
        # self.follow_user()
    
    def seleniumDefinition():
        options = Options()
        #options.add_argument('--headless')
        return webdriver.Firefox(options=options)

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[4]/div/div/button[1]').click()
        time.sleep(3)
        self.driver.find_element_by_class_name('L3NKy').click()
        time.sleep(8)

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))

    def follow_user(self):
        self.driver.find_element_by_class_name('jIbKX').click()


if __name__ == '__main__':
    ig_bot = InstagramBot('USERNAME','PASSWORD', '')
