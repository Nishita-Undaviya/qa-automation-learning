from playwright.sync_api import Page, expect, sync_playwright
import pytest

@pytest.mark.skip
def test_single_file(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    page.locator('#singleFileInput').set_input_files("../files/Test1.txt")
    page.wait_for_timeout(3000)
    page.locator("button:has-text('Upload Single File')").click()
    page.wait_for_timeout(3000)
    single_file_msg = page.locator('#singleFileStatus').inner_text()
    print(single_file_msg)
    expect(page.locator('#singleFileStatus')).to_contain_text('Test1.txt')
    print('File Upload sucessfully')
    page.wait_for_timeout(3000)


def test_multi_files(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')

    files = ['../files/Test1.txt','../files/Test2.txt']
    page.locator('#multipleFilesInput').set_input_files(files)
    page.wait_for_timeout(3000)
    page.locator("button:has-text('Upload Multiple Files')").click()
    page.wait_for_timeout(3000)
    single_file_msg = page.locator('#multipleFilesStatus').inner_text()
    print(single_file_msg)
    expect(page.locator('#multipleFilesStatus')).to_contain_text('Test1.txt')
    expect(page.locator('#multipleFilesStatus')).to_contain_text('Test2.txt')
    print('Multiple Files Upload sucessfully')
    page.wait_for_timeout(3000)