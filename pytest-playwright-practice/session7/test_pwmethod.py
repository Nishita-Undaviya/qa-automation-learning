import pytest
from playwright.sync_api import sync_playwright, expect
from playwright.async_api import Page

def test_pwmethod(page:Page):
    page.goto('https://demowebshop.tricentis.com/')

    product = page.locator('.product-title>a')

    # inner_text() vs text_content()
    print('\nInner Text:',product.nth(1).inner_text())
    print('Text Content:',product.nth(1).text_content(),'\n')
    page.wait_for_timeout(2000)

    count = product.count()
    for i in range(count):
        print('Text Content in Looping:',product.nth(i).text_content().strip())
        print('Inner Text in Looping:',product.nth(i).inner_text())
    page.wait_for_timeout(2000)

    # all_inner_texts() vs all_text_contents()
    print('\nAll Text Contents:',product.all_text_contents())
    print('\nAll Inner Texts:',product.all_inner_texts())
    page.wait_for_timeout(2000)

    # all()
    all_product = product.all()
    print('\nall() method:', all_product[0].inner_text(),'\n')
    for p in all_product:
        print('all() method in loop: ',p.inner_text())

    print('\n')
    for i in range(len(all_product)):
        print('all() method in loop with index: ',all_product[i].inner_text())