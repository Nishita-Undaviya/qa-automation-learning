import pytest
from playwright.sync_api import Page, expect

@pytest.mark.skip #use ficture to skip execution
def test_paginationtable(page:Page):
    page.goto('https://datatables.net/examples/core/basic_init/zero_configuration.html')
    has_more_pages = True
    while has_more_pages:
        rows = page.locator("#example tbody tr").all()
        for r in rows:
            print(r.inner_text())
        page.wait_for_timeout(3000)
        
        next_btn = page.locator("button[aria-label='Next']")
        disable = next_btn.get_attribute('class')
        if 'disabled' in disable:
            has_more_pages = False
        else:
            next_btn.click()

def test_filtertable(page:Page):
    page.goto('https://datatables.net/examples/core/basic_init/zero_configuration.html')
    filter_dropdown = page.locator('#dt-length-0')
    filter_dropdown.select_option(label='25')
    page.wait_for_timeout(5000)
    rows = page.locator("#example tbody tr")
    print('Number of rows filtered: ', rows.count())
    expect(rows).to_have_count(25)