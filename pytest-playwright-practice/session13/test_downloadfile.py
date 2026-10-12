from playwright.sync_api import Page, expect, sync_playwright
import os

def test_download_files(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/p/download-files_25.html')
    page.locator('#inputText').fill('Download File')
    page.locator('#generateTxt').click()

    # Method 1
    # def handle_download(download):
    #     download.save_as('../download_files/test_file.txt')
    
    # page.on('download',handle_download)

    page.on('download', lambda download: download.save_as('../download_files/test_file.txt'))
    page.locator('#txtDownloadLink').click()

    page.wait_for_timeout(5000)

    if os.path.exists('../download_files/test_file.txt'):
        print("File Exist")
    else:
        print('File doesn\'t exist')