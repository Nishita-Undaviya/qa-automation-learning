from playwright.sync_api import Page, expect, sync_playwright
import pytest

def test_keyboard_events(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    page.locator('#input1').focus()
    page.keyboard.insert_text('Keayboard Events')
    page.keyboard.press('Control+A')
    page.keyboard.press('Control+C')
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Control+V')
    page.keyboard.press('Tab')
    page.keyboard.press('Tab')
    page.keyboard.press('Control+V')

    expect(page.locator('#input2')).to_have_value('Keayboard Events')
    expect(page.locator('#input3')).to_have_value('Keayboard Events')

    page.wait_for_timeout(5000)