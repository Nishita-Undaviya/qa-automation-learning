import pytest, re
from playwright.sync_api import Page, expect

def test_radiobutton(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    radio_button = page.locator('#female')

    #Visibility, enable, unenable elements
    expect(radio_button).to_be_visible()
    expect(radio_button).to_be_enabled()
    expect(radio_button).not_to_be_checked()
    radio_button.check()
    expect(radio_button).to_be_checked()
    page.wait_for_timeout(5000)