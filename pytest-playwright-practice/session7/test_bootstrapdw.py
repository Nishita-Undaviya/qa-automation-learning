import pytest
from playwright.sync_api import sync_playwright, Page, expect

def test_bootstrapdw(page:Page):
    page.goto('https://opensource-demo.orangehrmlive.com/web/index.php/auth/login')

    page.locator('input[name="username"]').fill('Admin')
    page.locator('input[name="password"]').fill('admin123')
    page.locator('button[type="submit"]').click()
    page.wait_for_timeout(3000)
    page.get_by_text("PIM").click()
    page.locator('form i').nth(2).click()
    page.wait_for_timeout(3000)
    options= page.locator('div[role="listbox"] span')
    print("Total number of options of Job Title field", options.count())
    expect(options).to_have_count(options.count())
    page.wait_for_timeout(3000)
    print("All options", options.all_text_contents())
    for i in range(options.count()):
        # print(options.nth(i).text_content())
        text = options.nth(i).text_content()
        print(text)
        if(text=='Automaton Tester'):
            options.nth(i).click()
            break
    page.wait_for_timeout(3000)