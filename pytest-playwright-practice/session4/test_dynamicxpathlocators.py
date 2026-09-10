import pytest, re
from playwright.sync_api import Page, expect

def test_dynamic_xpath_locators(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    ''' 
    Dynamic Xpath locators usting html elements:
    //button[text()='START' or text()='STOP']
    //button[@name='start' or @name='stop']
    //button[contains(@name,'st')]
    //button[starts-with(@name,'st')] '''

    for i in range(5):
        page.locator("//button[text()='START' or text()='STOP']").click()
        page.wait_for_timeout(2000)

    
    '''
    Dynamic Xpath locators usting css:
    button[name='start'],button[name='stop']
    button[name^='st'] ---- equals to starts-with()
    button[name*='st'] ---- equals to contains() '''

    for i in range(5):
        page.locator("button[name^='st']").click()
        page.wait_for_timeout(2000)

    # by using playwright locator

    for i in range(5):
        page.get_by_role('button',name=re.compile(r'ST.*')).click()
        page.wait_for_timeout(2000)