from selenium import webdriver
import os
import time


class InstagramBotLogin:

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

        self.driver = webdriver.Chrome('./chromedriver.exe')

        self.login()
        time.sleep(2)
        self.base_url = "https://www.instagram.com"
        self.nav_user(user)
        time.sleep(1)
        self.follow_user()

    def login(self):
        self.driver.get('https://www.instagram.com/accounts/login/')
        time.sleep(1)
        self.driver.find_element_by_name('username').send_keys(self.username)
        self.driver.find_element_by_name('password').send_keys(self.password)
        time.sleep(1)
        self.driver.find_element_by_class_name('L3NKy').click()
        time.sleep(1)

    def nav_user(self, user):
        self.driver.get('{}/{}'.format(self.base_url, user))

    def follow_user(self):
        self.driver.find_element_by_class_name('jIbKX').click()

if __name__ == '__main__':
    ig_bot = InstagramBotLogin('SET-LOGIN-ACCOUNT', 'SET-PASSWORD', 'SET-USERNAME-TO-FOLLOW')
