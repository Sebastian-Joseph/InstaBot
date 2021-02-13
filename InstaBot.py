from selenium import webdriver
from time import sleep
driver = webdriver.Chrome()
pw = open("password.txt", "r").read()

class InstaBot:
    def __init__(self, username, pw):
        self.driver = webdriver.Chrome()
        self.username = username
        self.driver.get("https://instagram.com")
        sleep(4)
        self.driver.find_element_by_xpath("//input[@name=\"username\"]") \
            .send_keys(username)
        self.driver.find_element_by_xpath("//input[@name=\"password\"]") \
            .send_keys(pw)
        self.driver.find_element_by_xpath('//button[@type="submit"]') \
            .click()
        sleep(4)
        self.driver.find_element_by_xpath("//button[contains(text(), 'Not Now')]") \
            .click()
        sleep(2)

def get_unfollowers(self):
    self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[3]/div/div[5]/div[1]")\
        .click


my_bot = InstaBot('_sebastianjoseph', pw)