from pytest_bdd import scenario, when, then
from Drivers.chromedriver import driver
from Pages.Top_Navigation_Panel import top_panel
from Pages.Gist_Details import details
from Pages.File_Details_Page import elements
from Source.conftest import git_logout
import datetime
from Synchronization.Custom_wait import wait_till_element_enabled,\
    wait_till_element_disappears, wait_for_element


@scenario('../Features/common_steps.feature', 'Opening and logging into the git dashboard')
@scenario('../Features/test_100_Creating a Gist.feature','To test the ability of the user to login and create a gist')
def test_create_a_gist():
    pass
 
@scenario('../Features/common_steps.feature', 'Opening and logging into the git dashboard')
@scenario('../Features/test_100_Creating a Gist.feature','To test the ability of the user to login and create a private gist')
def test_create_a_private_gist():
    pass


@when("User clicks on + in the top panel and selects New Gist")
def new_gist():
    wait_till_element_enabled("xpath", top_panel.create_new, 0.1)
    driver.find_element_by_xpath(top_panel.create_new).click()
    wait_till_element_enabled("xpath", top_panel.new_gist, 0.1)
    driver.find_element_by_xpath(top_panel.new_gist).click()


@when("User is entering the description and filename")
def gist_details():
    wait_till_element_enabled("name", details.description, 0.1)
    driver.find_element_by_name(details.description).send_keys("Test Description", str(datetime.datetime.now()))
    driver.find_element_by_name(details.filename).send_keys("Test Name", str(datetime.datetime.now()))
    driver.find_element_by_class_name(details.code).click()
    driver.find_element_by_class_name(details.code).send_keys("classname")
    
    
@when("User is clicking on Create Public gist button")
def gist_creation():
    driver.find_element_by_xpath(details.create).click()
    wait_till_element_disappears("xpath", details.create, 0.1)
    
    
@when("User is clicking on Create private gist button")
def gist_private_creation():
    driver.find_element_by_xpath(details.private_create).click()
    wait_till_element_disappears("xpath", details.private_create, 0.5)
    

@then("User has created a private gist")
@then("User has created a public gist")
def gist_created():
    assert driver.find_element_by_xpath(elements.delete_button)
    wait_till_element_enabled("xpath", elements.delete_button, 0.1) 
    

@then("User is logging out")
def sign_out():
    git_logout()