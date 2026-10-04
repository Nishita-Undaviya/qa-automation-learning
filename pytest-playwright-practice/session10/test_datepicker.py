from playwright.sync_api import Page, expect
import pytest

def select_date(page: Page, target_year: str, target_month: str, target_day: str, is_future: bool = True):
    while True:
        displayed_month = page.locator('.ui-datepicker-month').inner_text()
        displayed_year = page.locator('.ui-datepicker-year').inner_text()
        if displayed_month == target_month and displayed_year == target_year:
            break
            
        if is_future:
            next_btn = page.locator('.ui-datepicker-next')
            expect(next_btn).to_be_visible()
            next_btn.click()
        else:
            prev_btn = page.locator('.ui-datepicker-prev')
            expect(prev_btn).to_be_visible()
            prev_btn.click()
            
        page.wait_for_timeout(200)

    day_locator = page.locator(f"//td[@data-handler='selectDay']/a[text()='{target_day}']")
    expect(day_locator).to_be_visible()
    day_locator.click()


def test_jquery_datepicker(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    datepicker = page.locator('#datepicker')
    datepicker.fill('12/11/1999')
    expect(datepicker).to_have_value('12/11/1999')
    page.wait_for_timeout(5000)

    is_next = False #True - for future dates, False - for past dates
    y = '2025'
    m = 'December'
    d = '11'
    datepicker.click()
    select_date(page,y,m,d,is_next)
    print(datepicker.inner_text())
    expect(datepicker).to_have_value('12/11/2025')
    page.wait_for_timeout(5000)
