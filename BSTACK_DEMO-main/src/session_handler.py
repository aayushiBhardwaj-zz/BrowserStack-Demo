from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from threading import Thread
import json

def execute_locally():
    driver = webdriver.Chrome("/Users/abhardwa/Desktop/BSTACK_DEMO-main/chromedriver")
    return driver

def execute_remotely(username, access_key, desired_cap):
    hub_url = 'https://'+username+':'+access_key+'@hub-cloud.browserstack.com/wd/hub'
    driver = webdriver.Remote(
	    command_executor=hub_url,
	    desired_capabilities=desired_cap)
    return driver

