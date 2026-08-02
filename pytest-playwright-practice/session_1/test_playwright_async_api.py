#Pre-requisite for asyncronus execution, install pytest-asyncio
#Command to install pytest-asyncio: pip install pytest-asyncio
#To run this code user 'pytest pytest-playwright-practice\test_playwright_async_api.py -s' command in cmd because Because this code bypasses those fixtures and manually calls await p.chromium.launch() inside your test, you are overriding the plugin's configuration. Playwright ignores the CLI flag and defaults your custom launcher back to headless mode.

from playwright.async_api import Page, expect, async_playwright
import pytest
from conftest import BASE_URL

@pytest.mark.asyncio
async def test_verifyPageUrl():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto(BASE_URL)
        pageUrl = page.url
        print("URL of this web application",pageUrl)
        await expect(page).to_have_url(BASE_URL) #Expected URL
        await browser.close()

@pytest.mark.asyncio
async def test_verifyTitle():
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False, slow_mo=1000)
        page = await browser.new_page()
        await page.goto(BASE_URL)
        pageTitle = await page.title()
        print("Page title of this web application",pageTitle)
        await expect(page).to_have_title('Installation | Playwright Python') #Expected Page Title
        await browser.close()