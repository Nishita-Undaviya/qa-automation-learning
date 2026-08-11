import time, re
from playwright.sync_api import Page, expect

def test_verify_pwlocators(page:Page):
    page.goto("https://playwright.dev/python/docs/intro")
    # time.sleep(2) #second - pythn method
    page.wait_for_timeout(2000) #200 ms = 2 sec - Playwright method

    #get_by_alt_text()
    logoAltText = page.get_by_alt_text("Playwright logo") #get_by_alt_text()
    expect(logoAltText).to_be_visible()

    #get_by_text()
    text_loc = page.get_by_text("Playwright recommends using the official")
    expect(text_loc).to_be_visible() 
    expect(page.get_by_text("Playwright recommends using the")).to_be_visible() #Partial Text
    expect(page.get_by_text(re.compile(".*Playwright.*")).first).to_be_visible() #Regular Expression

    #get_by_role
    page.goto("https://playwright.dev/python/docs/locators")
    page.wait_for_timeout(2000)
    # Target specifically the H1 heading element to resolve the strict mode conflict
    expect(page.get_by_role("heading", name="Locators", exact=True)).to_be_visible()
    expect(page.get_by_role("heading", name="Locating")).to_be_visible()

    #get_by_label
    page.get_by_label("Password").fill("PlayW@123")
    page.wait_for_timeout(2000)

    #get_by_placeholder
    page.get_by_placeholder("name@example.com").fill("PlayW@pw.com")
    page.wait_for_timeout(2000)

    #get_by_title
    expect(page.get_by_title("Issues count")).to_have_text("25 issues")
    page.wait_for_timeout(2000)

    #get_by_test_id
    expect(page.get_by_test_id("directions")).to_have_text("Itinéraire")
    page.wait_for_timeout(2000)