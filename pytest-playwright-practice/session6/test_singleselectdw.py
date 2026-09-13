import pytest
from playwright.sync_api import Page, expect

def test_singleselectdw(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")

    page.locator('#country').select_option('India') #Select by label
    page.wait_for_timeout(2000)
    page.locator('#country').select_option(label= 'Canada') #Select by label
    page.wait_for_timeout(2000)
    page.locator('#country').select_option('germany') #Select by value
    page.wait_for_timeout(2000)
    page.locator('#country').select_option(value = 'usa') #Select by value
    page.wait_for_timeout(2000)
    page.locator('#country').select_option(index = 4) #Select by index
    page.wait_for_timeout(2000)
    dw = page.locator('#country>option')
    expect(dw).to_have_count(10)
    option_text = [text.strip() for text in dw.all_text_contents()]
    print(option_text)
    for options in option_text:
        print(options)
    page.wait_for_timeout(2000)