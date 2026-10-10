from playwright.sync_api import Page, expect, sync_playwright
import pytest

@pytest.mark.skip
def test_dialog_box_mathod1(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    # Register an event
    def handle_dialog(dialog):
        print(dialog.type, dialog.message)
        dialog.accept()

    page.on('dialog',handle_dialog)
    page.wait_for_timeout(3000)

    page.locator('#alertBtn').click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_dialog_box_mathod2(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    page.on('dialog',lambda dialog: dialog.accept())
    page.wait_for_timeout(3000)

    page.locator('#alertBtn').click()
    page.wait_for_timeout(5000)

@pytest.mark.skip
def test_dialog_box_mathod3(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    messages = []

    def handle_dialog(dialog):
        page.wait_for_timeout(3000)
        print('DIALOG FIRED:', dialog.type, dialog.message)
        messages.append(dialog.message)
        dialog.accept()

    page.once('dialog', handle_dialog)
    page.locator('#alertBtn').click()

    assert messages == ['I am an alert box!']

@pytest.mark.skip
def test_confirmation_dialog_box(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    messages = []

    def handle_dialog(dialog):
        page.wait_for_timeout(3000)
        print('DIALOG FIRED:', dialog.type, dialog.message)
        messages.append(dialog.message)
        # dialog.accept() #for OK button
        dialog.dismiss() #for cancel button

    page.once('dialog', handle_dialog)
    page.locator('#confirmBtn').click()

    print('Demo Text: ',page.locator('#demo').inner_text())

def test_prompt_dialog_box(page: Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    messages = []

    def handle_dialog(dialog):
        page.wait_for_timeout(3000)
        print('DIALOG FIRED:', dialog.type, dialog.message)
        messages.append(dialog.message)
        dialog.accept('John Doe') #for OK button
        # dialog.dismiss() #for cancel button

    page.once('dialog', handle_dialog)
    page.locator('#promptBtn').click()

    print('Demo Text: ',page.locator('#demo').inner_text())