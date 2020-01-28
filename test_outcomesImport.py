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

class TestOutcomesImport():
  def setup_method(self, method):
    self.driver = webdriver.Firefox()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_outcomesImport(self):
    self.driver.get("https://canvas.instructure.com/login/canvas")
    self.driver.set_window_size(1847, 1028)
    self.driver.find_element(By.ID, "pseudonym_session_unique_id").click()
    self.driver.find_element(By.ID, "pseudonym_session_unique_id").send_keys("muzaibanjum95@ucp.edu.pk")
    self.driver.find_element(By.ID, "pseudonym_session_password").click()
    self.driver.find_element(By.ID, "pseudonym_session_password").send_keys("pakistan1234")
    self.driver.find_element(By.CSS_SELECTOR, ".Button--login:nth-child(1)").click()
    self.driver.find_element(By.CSS_SELECTOR, ".ic-DashboardCard__header-title > span").click()
    self.driver.find_element(By.LINK_TEXT, "Outcomes").click()
    self.driver.find_element(By.CSS_SELECTOR, ".import_outcomes > .ui-button-text").click()
  
