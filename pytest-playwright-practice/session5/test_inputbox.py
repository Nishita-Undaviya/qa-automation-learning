import pytest, re
from playwright.sync_api import Page, expect

def test_input(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    textbox = page.locator('#name')

    #Visibility, enable, unenable elements
    expect(textbox).to_be_visible()
    expect(textbox).to_be_enabled()

    #check attribute of elements
    expect(textbox).to_have_attribute('maxlength','15')

    #get an attribute of an element
    maxlength = textbox.get_attribute('maxlength')
    print('Max lenght of input: ', maxlength)

    #Fill inputbox
    textbox.fill('Nishita Soni')

    #Get  input value from input box
    value = textbox.input_value()
    print("entered value is: ", value)

    page.wait_for_timeout(5000) 