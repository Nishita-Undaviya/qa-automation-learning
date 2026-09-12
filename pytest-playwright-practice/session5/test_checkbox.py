import pytest, re
from playwright.sync_api import Page, expect

def test_checkbox(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    checkbox = page.get_by_label('Monday')
    checkbox.check()
    expect(checkbox).to_be_checked()
    page.wait_for_timeout(2000)

    days = ['Sunday', 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday']
    checkboxes= []
    # for d in days:
    #     chkbox = page.get_by_label(d)
    #     checkboxes.append(chkbox)
    checkboxes = [page.get_by_label(d) for d in days]
    print('Total number of checkboxes: ', len(checkboxes))
    for chkbox in checkboxes:
        chkbox.check()
        expect(chkbox).to_be_checked()
    page.wait_for_timeout(2000)

    for chkbox in checkboxes[-3:]:
        chkbox.uncheck()
        expect(chkbox).not_to_be_checked()
    page.wait_for_timeout(2000)

    for chkbox in checkboxes:
        if chkbox.is_checked():
            chkbox.uncheck()
            expect(chkbox).not_to_be_checked()
        else:
            chkbox.check()
            expect(chkbox).to_be_checked()
    page.wait_for_timeout(2000)

    index = [1,3,6]
    for i in index:
        checkboxes[i].check()
        expect(checkboxes[i]).to_be_checked()
    page.wait_for_timeout(2000)

    weekday = 'Friday'
    for lbl in days:
        if lbl == weekday:
            c = page.get_by_label(lbl)
            c.check()
            expect(c).to_be_checked()
    page.wait_for_timeout(2000)