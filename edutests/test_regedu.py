# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

class TestRegedu():
  def setup_method(self, method):
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_regedu(self):
    self.driver.get("http://127.0.0.1:5000/")
    self.driver.set_window_size(792, 816)
    self.driver.find_element(By.ID, "signup-link").click()
    self.driver.find_element(By.ID, "new-email").click()
    self.driver.find_element(By.ID, "new-email").send_keys("josh@gmail.com")
    self.driver.find_element(By.ID, "new-username").click()
    self.driver.find_element(By.ID, "new-username").send_keys("josh")
    self.driver.find_element(By.ID, "new-password").click()
    self.driver.find_element(By.ID, "new-password").send_keys("joshpwd")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(7)").click()
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("josh")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("joshpwd")
    self.driver.find_element(By.CSS_SELECTOR, ".btn:nth-child(6)").click()
  
