from pytest_bdd import scenario, when, then
from Drivers.chromedriver import driver
from Synchronization.Custom_wait import wait_for_element
from Pages.Gist_Search import Search_Page, Search_Results
from Source.conftest import git_logout
import re
from selenium.webdriver.common.keys import Keys



@scenario('../Features/common_steps.feature', 'Opening Gists Search')
@scenario('../Features/test_200_Search a Gist.feature','To test the ability of an unauthenticated user to search a gist')
def test_search_gist():
    pass
   
@scenario('../Features/common_steps.feature', 'Opening Gists Search and logging in')
@scenario('../Features/test_200_Search a Gist.feature','To test the ability of an authenticated user to search a gist')
def test_search_gist_authenticated():
    pass


@when("User is searching with the gist name keywords")
def search_gist():
    gist_search()
   
    
@then("Public gists are displayed")
def public_gist():
    if_present(Search_Results.public_gist)
    
    
@then("Private gists are not displayed")
def secret_gist():
    if_not_present(Search_Results.secret_gist)
    

@then("Private gists are displayed")
def secret_gist_authenticated():
    if_present(Search_Results.secret_gist)
    
@then("User is logging out")
def sign_out():
    git_logout()
    
    
def gist_search():
    wait_for_element("xpath", "xpath", Search_Page.search_textbox, Search_Page.search_textbox_logged, 1)
    if len(driver.find_elements_by_xpath(Search_Page.search_textbox)) > 0:
        driver.find_element_by_xpath(Search_Page.search_textbox).send_keys("Test Name2020")
        driver.find_element_by_xpath(Search_Page.search_textbox).send_keys(Keys.ENTER)
    else:
        driver.find_element_by_xpath(Search_Page.search_textbox_logged).send_keys("Test Name2020")
        driver.find_element_by_xpath(Search_Page.search_textbox_logged).send_keys(Keys.ENTER)
    
def if_present(element):
    src = driver.page_source
    if re.search(r'{}'.format(element), src):
        pass
    else:
        raise Exception("Element not found")
        
    
def if_not_present(element):
    src = driver.page_source
    if re.search(r'{}'.format(element), src):
        raise Exception("Element found")
    else:
        pass