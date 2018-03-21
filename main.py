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
  options = webdriver.ChromeOptions()
  options.add_argument('headless')
  driver = webdriver.Chrome(chrome_options=options)
  wait = WebDriverWait(driver, 10,0.1)
  driver.get(login_link)
  driver.execute_script("window.stop();")
  wait.until(EC.presence_of_element_located((By.ID, 'login-submit')))
  login_email = driver.find_element_by_id("login-email")
  login_password = driver.find_element_by_id("login-password")
  login_email.send_keys(username)
  login_password.send_keys(password)
  login_attempt = driver.find_element_by_id("login-submit")
  login_attempt.submit()
  wait.until(EC.presence_of_element_located((By.TAG_NAME, 'body')))
  driver.execute_script("window.stop();")
  search_link = 'https://www.linkedin.com/sales/search?facet.N=S'+'&facet.G='+geography+'&facet.CC='+company+\
  '&facet.SE='+senority+'&facet.TE='+tenure+'&count=200&start=0'
  driver.get(search_link)
  wait.until(EC.presence_of_element_located((By.ID, 'pagination')))
  total_results = driver.find_element_by_class_name('spotlight-result-count').text
  if total_results.isdigit() == False:
    total_results = 1000;
  else:
    total_results = int(total_results)
  print(total_results)
  id_list = []
  leadinfo_list = []
  lead_id_list = []
  lead_name_list = []
  lead_shconns_list = []
  for li in driver.find_elements_by_xpath("//div[@class='sublinks-container']"):
    li.find_element_by_tag_name('a').click()
    id_list.append(li.find_element_by_tag_name('a').get_attribute("href").split('#')[-1])
    print(id_list[-1])
    lead_id_list.append(id_list[-1])
  for lead in driver.find_elements_by_xpath("//div[@class='entity-info']"):
    leadinfo_list.append(lead.find_element_by_tag_name('a').get_attribute('title'))
  for idx in range(0,len(id_list)):
    id_no = id_list[idx]
    lead_name = leadinfo_list[idx]
    lead_name_list.append(lead_name)
    lead_shconns_list.append([connection.find_element_by_class_name('header-link').get_attribute("title")\
    for connection in driver.find_element_by_id(id_no).find_elements_by_class_name('entity-lockup-header')])
    print(lead_shconns_list[-1])
  count = 200
  return lead_shconns_list

if __name__ == '__main__':
  app.run()
