from flask import Flask
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoAlertPresentException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support import expected_conditions as EC
app = Flask(__name__)

@app.route('/')
def hello_world():
  username = 'jdurham@outlook.com'
  password = 'Summer201-'
  geography = 'us%3A0'
  company = '1441'
  senority = '6'
  tenure = '5'
  login_link = 'https://www.linkedin.com/'
  driver = webdriver.Chrome()
  driver.get(login_link)
  login_email = driver.find_element_by_id("login-email").get_attribute('class')
  return login_email

if __name__ == '__main__':
  app.run()
