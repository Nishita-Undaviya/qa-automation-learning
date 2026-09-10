import pytest
from playwright.sync_api import Page, expect

def test_xpath_locators(page:Page):
    page.goto("https://demowebshop.tricentis.com/")

    #Absolute xpath(full path)
    # logo = page.locator("xpath=/html/body/div[4]/div[1]/div[1]/div[1]/a/img") OR
    logo = page.locator("//html/body/div[4]/div[1]/div[1]/div[1]/a/img")
    expect(logo).to_be_visible(timeout = 1000)

    # #Relative Path: //html tagname[@attribute='value']
    expect(page.locator("//img[@alt='Tricentis Demo Web Shop']")).to_be_visible(timeout = 1000)

    #xpath with contains()
    products = page.locator('//h2//a[contains(@href,"computer")]')
    print('Product Count: ', products.count())
    expect(products).to_have_count(products.count())
    print("First Computer Product: ", products.first.text_content())
    print("Last Computer Product: ", products.last.text_content())
    print("N-th Computer Product: ", products.nth(2).text_content())
    print("All Computer Product: ", products.all_text_contents())
    print("All Computer Product by for loop: ")
    for index, i in enumerate(products.all_text_contents()):
        print(i)

    #Xpath with starts-with()
    build_products = page.locator("//h2//a[starts-with(@href,'/build')]")
    print('Total count of starts with build products', build_products.count())
    expect(build_products).to_have_count(build_products.count())

    # xpath with text()
    expect(page.locator("//a[text()='Register']")).to_be_visible(timeout = 1000)

    # xpath with last()
    expect(page.locator("//div[@class='column follow-us']//li[last()]")).to_have_text('Google+')

    # xpath with position()
    expect(page.locator("//div[@class='column follow-us']//li[position()=2]")).to_have_text('Twitter')
