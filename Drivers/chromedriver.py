#File to store the location of Drivers, in case of cross browser tesing
from selenium import webdriver

chromedriver_link = '/usr/local/bin/chromedriver'
driver = webdriver.Chrome(chromedriver_link)
driver.maximize_window()