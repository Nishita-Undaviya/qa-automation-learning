from playwright.sync_api import sync_playwright, Page, expect

def select_checkin_date(page, year, month, day):
    while True:
        checkin_my = page.locator('[id^="bui-calendar-month-"]').nth(0).inner_text()
        m,y = checkin_my.split(" ")
        if m == month and y == year:
            break;
        else:
            page.locator("button[aria-label='Next month']").click()
        
    all_dt= page.locator('table[aria-labelledby^="bui-calendar-month-"] tbody').nth(0).locator('td').all()
    for date in all_dt:
        if date.inner_text() == day:
            date.click()
            break

def select_checkout_date(page, year, month, day):
    while True:
        checkout_my = page.locator('[id^="bui-calendar-month-"]').nth(1).inner_text()
        m,y = checkout_my.split(" ")
        if m == month and y == year:
            break;
        else:
            page.locator("button[aria-label='Next month']").click()
        
    all_dt= page.locator('table[aria-labelledby^="bui-calendar-month-"] tbody').nth(1).locator('td').all()
    for date in all_dt:
        if date.inner_text() == day:
            date.click()
            break

def test_bootstrap_datepicker(page:Page):
    page.goto('https://www.booking.com/', wait_until='domcontentloaded')

    try:
        page.locator('#onetrust-accept-btn-handler').click(timeout=5000)
    except Exception:
        pass

    try:
        page.locator('button[aria-label="Dismiss sign-in info."]').click(timeout=5000)
    except Exception:
        pass

    page.locator('[data-testid="searchbox-dates-container"]').click()

    select_checkin_date(page, '2026', 'December', '10')
    select_checkout_date(page, '2027', 'December', '20')

    checkin_dt = page.locator('span[data-testid="date-display-field-start"]').inner_text()
    checkout_dt = page.locator('span[data-testid="date-display-field-end"]').inner_text()

    print('Check-In Date: ',checkin_dt)
    print('Check-Out Date: ',checkout_dt)

    expect(page.locator('span[data-testid="date-display-field-start"]')).to_contain_text(checkin_dt)
    expect(page.locator('span[data-testid="date-display-field-end"]')).to_contain_text(checkout_dt)

    page.wait_for_timeout(5000)