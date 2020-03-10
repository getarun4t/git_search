from Drivers.chromedriver import driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
   
wait = WebDriverWait(driver, 30)    
 
def wait_till_element_disappears(locator_type, element, polling_interval):
    if locator_type == "id":
        while (len(driver.find_elements_by_id(element))>0):
            time.sleep(polling_interval)
    elif locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element))>0):
            time.sleep(polling_interval)
    elif locator_type == "css":
        while (len(driver.find_elements_by_css_selector(element))>0):
            time.sleep(polling_interval)


def wait_till_element_enabled(locator_type, element, polling_interval):
    if locator_type == "id":
        while (len(driver.find_elements_by_id(element))==0):
            time.sleep(polling_interval)
        while (driver.find_element_by_id(element).is_enabled() == "false"):
            time.sleep(polling_interval)
        wait.until(EC.element_to_be_clickable((By.ID, element)))
    elif locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element))==0):
            time.sleep(polling_interval)
        while (driver.find_element_by_xpath(element).is_enabled() == "false"):
            time.sleep(polling_interval)
        wait.until(EC.element_to_be_clickable((By.XPATH, element)))
    elif locator_type == "css":
        while (len(driver.find_elements_by_css_selector(element))==0):
            time.sleep(polling_interval)
        while (driver.find_element_by_css_selector(element).is_enabled() == "false"):
            time.sleep(polling_interval)
        wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, element)))
    elif locator_type == "class":
        while (len(driver.find_elements_by_class_name(element))==0):
            time.sleep(polling_interval)
        while (driver.find_element_by_class_name(element).is_enabled() == "false"):
            time.sleep(polling_interval)
        wait.until(EC.element_to_be_clickable((By.CLASS_NAME, element)))
    if locator_type == "name":
        while (len(driver.find_elements_by_name(element))==0):
            time.sleep(polling_interval)
        while (driver.find_element_by_name(element).is_enabled() == "false"):
            time.sleep(polling_interval)
        wait.until(EC.element_to_be_clickable((By.NAME, element)))
        
def wait_for_element(locator_type1, locator_type2, element1, element2, wait_time):
    for x in range(1, wait_time*10, 1): 
        time.sleep(0.1)   
        if locator_type1 == "xpath":
            if (len(driver.find_elements_by_xpath(element1))>0):
                break
        elif locator_type2 == "xpath":
            if (len(driver.find_elements_by_xpath(element2))>0):
                break
            
def wait_if_displayed(locator_type, element, wait_time):
    count = 0
    interval = 0.1
    total_time = wait_time/interval
    if locator_type == "xpath":
        while (len(driver.find_elements_by_xpath(element))==0):
            time.sleep(interval)
            count = count+1
            if (len(driver.find_elements_by_xpath(element))==0) & (count == total_time):
                return "1"