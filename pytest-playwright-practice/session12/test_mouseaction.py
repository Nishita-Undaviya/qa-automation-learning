from playwright.sync_api import Page, expect, sync_playwright
import pytest

@pytest.mark.skip
def test_mouse_hover(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.locator('.dropbtn').hover()
    # page.locator('.dropdown-content>a').nth(1).hover()
    page.locator('.dropdown-content>a:nth-child(2)').hover()
    page.wait_for_timeout(3000)

@pytest.mark.skip
def test_mouse_right_click(page:Page):
    page.goto('https://swisnl.github.io/jQuery-contextMenu/demo.html')
    page.locator('.context-menu-one').click(button = 'right')
    page.wait_for_timeout(3000)

@pytest.mark.skip
def test_mouse_double_click(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    page.locator('button').get_by_text('Copy Text').dblclick()
    expect(page.locator('#field2')).to_have_value('Hello World!')
    page.wait_for_timeout(3000)

def test_mouse_drag_drop(page:Page):
    page.goto('https://testautomationpractice.blogspot.com/')
    source = page.locator('#draggable')
    target = page.locator('#droppable')

    # Method 1
    # source.hover()
    # page.mouse.down()
    # target.hover()
    # page.mouse.up()

    # Method 2
    source.drag_to(target)
    page.wait_for_timeout(3000)