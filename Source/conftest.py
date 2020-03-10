#Common functions are saved here

import pytest
from Drivers.chromedriver import driver
from pytest_bdd.steps import given, then
from Pages.Login_Page import login_page
from Pages.Top_Navigation_Panel import top_panel
from Pages.Sign_out_page import page_details
from Credentials.git_credentials import git, gist
from Pages.Gist_Search import Sign_in
from Synchronization.Custom_wait import wait_till_element_enabled,\
    wait_till_element_disappears, wait_if_displayed
import time



@pytest.fixture(scope="session", autouse=True)
def pretest():
    yield driver
    driver.quit()
    
    
@pytest.fixture
def supply_url():
    return "https://api.github.com"

#If username and password textboxes are prompted, it is being handled using the script in the UI

@given("User is opening login page")
def git_login_page():
    driver.get(git.url)    
    
@given("User is opening the gist page")
def gist_page():
    driver.get(gist.url)   
    
@given("User is logging in")
def logging_in():
    git_login()
    
@given("User is logging into Gist")
def logging_in_gist():
    gist_login()


def git_login():
    if len(driver.find_elements_by_id(login_page.username)) > 0:  
        driver.find_element_by_id(login_page.username).send_keys(git.username)
        driver.find_element_by_id(login_page.password).send_keys(git.password)
        driver.find_element_by_xpath(login_page.sign_in).click()
        
def gist_login():
    wait_till_element_enabled("xpath", Sign_in.si_button, 0.1)
    driver.find_element_by_xpath(Sign_in.si_button).click()
    wait_till_element_enabled("id", login_page.username, 0.1)  
    driver.find_element_by_id(login_page.username).send_keys(git.username)
    driver.find_element_by_id(login_page.password).send_keys(git.password)
    driver.find_element_by_xpath(login_page.sign_in).click()
    wait_till_element_disappears("xpath", login_page.sign_in, 0.5)
    
def git_logout():
    time.sleep(1)
    wait_till_element_enabled("xpath", top_panel.profile, 0.1)
    driver.find_element_by_xpath(top_panel.profile).click()
    flag = wait_if_displayed("xpath", top_panel.sign_out, 2)
    if flag == 1:
        driver.find_element_by_xpath(top_panel.profile).click()
        wait_till_element_enabled("xpath", top_panel.sign_out, 0.1)
    driver.find_element_by_xpath(top_panel.sign_out).click()
    wait_till_element_enabled("xpath", page_details.sign_out, 0.1)
    driver.find_element_by_xpath(page_details.sign_out).click()
    wait_till_element_disappears("xpath", page_details.sign_out, 0.1)