#To run this code user 'pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v --headed' command in cmd
#Commands: 
#pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v --headed (For launch a browser/UI)
#pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v (For headless mode, it's do not launch a browser just display pass ot fail output in CMD)
#pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v --headed --browser firefox (choose from 'chromium', 'firefox', 'webkit')
#pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v --headed --browser firefox --browser chromium (choose from 'chromium', 'firefox', 'webkit')
#pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v --headed --numprocesses 2/--numprocesses=2 (For parallel testcased execution - from playwright)
#pytest pytest-playwright-practice\test_playwright_sync_api.py -s -v --headed -n 2/-n=2 (For parallel testcased execution - from pytest)

from playwright.sync_api import Page,expect
from conftest import BASE_URL

def test_verifyPageUrl(page:Page):
    page.goto(BASE_URL) #passing URL
    pageUrl = page.url
    print("URL of this web application",pageUrl)
    expect(page).to_have_url(BASE_URL) #Expected URL

def test_verifyTitle(page:Page):
    page.goto(BASE_URL)
    pageTitle = page.title()
    print("Page title of this web application",pageTitle)
    expect(page).to_have_title('Installation | Playwright Python') #Expected Page Title