##################################################
##   Project_Name: SHU Daily Report Script      ##
##   Latest_Version: 0.2                        ##
##   Date: 2020/11/24                           ##
##   Based on Python, Selenium                  ##
##   Originated by LuminolT (2020 SHU.CES-CSE)  ##
##   Contact me!    QQ: 1477357096              ##
##################################################

import pytest
import time
import json
import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestDailyReport():
  def setup_method(self):
    chrome_driver = 'C:\Program Files\Google\Chrome\Application\chromedriver.exe'
    self.driver = webdriver.Chrome(executable_path=chrome_driver)
    vars = {}
  
  def teardown_method(self):
    quit()
  
  def login(self):
    TodayDate = time.strftime('%Y-%m-%d', time.localtime(time.time()))
    TodayHour = int(time.strftime('%H', time.localtime(time.time())))
    if TodayHour < 20:
      self.driver.get("https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?day={}&t=1".format(TodayDate))
    else:
      self.driver.get("https://selfreport.shu.edu.cn/XueSFX/HalfdayReport.aspx?day={}&t=2".format(TodayDate))
    self.driver.find_element(By.ID, "username").click()
    ## ID and Password
    self.driver.find_element(By.ID, "username").send_keys("")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("")
    self.driver.find_element(By.ID, "submit").click()
  
  def test_dailyReport(self):
    # self.driver.find_element(By.PARTIAL_LINK_TEXT, "未填报").click()
    # time.sleep(n)
    # self.driver.find_element(By.CSS_SELECTOR, "#p1_ChengNuo .f-field-body-checkboxlabel").click()
    # time.sleep(n)
    # self.driver.find_element(By.ID, "p1_TiWen-inputEl").click()
    # time.sleep(n)
    # temperature = random.randint(1, 6)/10
    # t = str(36+temperature)
    # self.driver.find_element(By.ID, "p1_TiWen-inputEl").send_keys(t)
    # time.sleep(n)
    # self.driver.find_element(By.CSS_SELECTOR, "#fineui_7 .f-field-body-checkboxlabel").click()
    # time.sleep(n) 
    # self.driver.find_element(By.ID, "p1_ctl00_btnSubmit").click()
    # time.sleep(n)
    # self.driver.find_element(By.ID, "fineui_14").click()
    # time.sleep(1)    
    # self.driver.find_element(By.ID, "fineui_19").click()
    # time.sleep(n)
    # self.driver.find_element(By.ID, "lbReportHistory").click()
    self.driver.find_element(By.ID, "p1_ChengNuo-inputEl-icon").click()
    self.driver.find_element(By.ID, "fineui_6-inputEl-icon").click()
    self.driver.find_element(By.ID, "fineui_11-inputEl-icon").click()
    self.driver.find_element(By.ID, "fineui_13-inputEl-icon").click()
    self.driver.find_element(By.ID, "p1_TiWen-inputEl").click()
    time.sleep(0.1)
    temperature = random.randint(1, 6)/10
    t = str(36+temperature)
    self.driver.find_element(By.ID, "p1_TiWen-inputEl").send_keys(t)
    time.sleep(0.1)
    self.driver.find_element(By.ID, "fineui_21-inputEl-icon").click()
    self.driver.find_element(By.ID, "fineui_23-inputEl-icon").click()
    # self.driver.find_element(By.ID, "p1_ctl00_btnSubmit").click()
    # time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#fineui_32 .f-btn-text").click()
    time.sleep(1)
    self.driver.find_element(By.CSS_SELECTOR, "#fineui_37 .f-btn-text").click()
    time.sleep(1)

def main():

  
  TD=TestDailyReport()
  TD.setup_method()
  TD.login()
  TD.test_dailyReport()

if __name__ == "__main__":
  main()