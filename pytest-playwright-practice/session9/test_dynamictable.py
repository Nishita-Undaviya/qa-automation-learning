import pytest
from playwright.sync_api import Page, expect

def test_dynamictable(page:Page):
    page.goto("https://practice.expandtesting.com/dynamic-table")

    table = page.locator('table.table tbody')
    rows = table.locator('tr').all()
    cpu_load = ''
    for r in rows:
        browser_nm = r.locator('td').nth(0).inner_text()
        if browser_nm == 'Chrome':
            cpu_load = r.locator("td:has-text('%')").inner_text()
            print("CPU load of ",browser_nm ,': ', cpu_load)
            break
    
    expect(page.locator('#chrome-cpu')).to_contain_text(cpu_load)
    page.wait_for_timeout(5000)