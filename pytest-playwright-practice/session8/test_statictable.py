import pytest
from playwright.sync_api import sync_playwright, expect, Page

def test_statictable(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    tbl = page.locator('table[name="BookTable"]>tbody')
    expect(tbl).to_be_visible(timeout=2000)

    rows = tbl.locator('tr')
    expect(rows).to_have_count(7)
    print('No. of rows in table: ',rows.count())

    hdr= rows.locator('th')
    expect(hdr).to_have_count(4)
    print('No. of headers: ', hdr.count())

    second_row_text = rows.nth(2).locator('td').all_inner_texts()
    print("Row Data: ",second_row_text)

    total = 0
    print("Table data:")
    for text in rows.all()[1:]:
        print(text.locator('td').all_inner_texts())
        author = text.locator('td').nth(1).inner_text()
        price = text.locator('td').nth(3).inner_text()
        total+=int(price)
        if author == 'Mukesh':
            print(author, 'have Book: ',text.locator('td').nth(0).inner_text())
        
    print("Total Price: ", total)
        
