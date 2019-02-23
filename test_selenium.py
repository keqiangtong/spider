
from selenium import webdriver
import time

driver = webdriver.PhantomJS()

driver.get('http://www.baidu.com')

driver.save_screenshot('./baidu.pn')

time.sleep(3)

driver.quit()