import pytest
from playwright.sync_api import Page, expect

'''
    tag id combination css locators - written as tag#id
    tag class combination css locators - written as tag.class
    tag attribute combination css locators - written as tag[attribute=value]
    tag class attribute combination css locators - written as tag.class[attribute=value]
'''

def test_csslocators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #tag id combination css locators
    # written as tag#id
    # page.locator("input#newsletter-email").fill('playwright@pw.com')
    page.locator("#newsletter-email").fill('playwright@pw.com')
    page.wait_for_timeout(1000)

    #class
    page.locator('input.search-box-text').fill('playwright')
    page.locator('.search-box-text').fill('playwright')
    page.wait_for_timeout(1000)

    #attribute
    page.wait_for_timeout(1000)
    expect(page.locator('input[name="NewsletterEmail"]')).to_be_visible()
    expect(page.locator('[name="NewsletterEmail"]')).to_be_visible()

    page.wait_for_timeout(1000)
    expect(page.locator('input.search-box-text[value="Search store"]')).to_be_visible()
    expect(page.locator('.search-box-text[value="Search store"]')).to_be_visible()

    page.wait_for_timeout(1000)
    expect(page.locator('.header-logo>a>img[alt="Tricentis Demo Web Shop"]')).to_be_visible()