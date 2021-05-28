import pytest
from selenium import webdriver
from time import sleep , ctime
import os
options = webdriver.ChromeOptions()
options.add_argument('–log-level=3')
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(executable_path='C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe',
options=options,service_log_path=os.devnull)
# driver.get('http://www.baidu.com')
# sleep(3)
def test_demo1():
    # options = webdriver.ChromeOptions()
    # options.add_argument('–log-level=3')
    # options.add_experimental_option('excludeSwitches', ['enable-logging'])
    # driver = webdriver.Chrome(executable_path='C:\\Users\\dell\\AppData\\Local\\Google\\Chrome\\Application\\chromedriver.exe',
    # options=options,service_log_path=os.devnull)
    driver.get('http://www.baidu.com')
    sleep(3)
    driver.find_element_by_id("kw").send_keys("selenium")
    driver.find_element_by_id("su").click()
    sleep(3)
    driver.quit()



