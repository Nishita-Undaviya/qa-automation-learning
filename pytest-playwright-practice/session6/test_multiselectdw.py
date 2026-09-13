import pytest
from playwright.sync_api import Page, expect

def test_multiselectdw(page:Page):
    page.goto("https://testautomationpractice.blogspot.com/")
    page.locator("#colors").select_option(['Red','Green','Blue']) #by label
    page.wait_for_timeout(2000)
    page.locator("#colors").select_option(label= ['Yellow','White']) #by label
    page.wait_for_timeout(2000)
    page.locator('#animals').select_option(value=['dog','elephant','fox']) #by value
    page.wait_for_timeout(2000)
    page.locator('#animals').select_option(index=[4,2])
    page.wait_for_timeout(2000)
    multiselect = page.locator('#colors>option')
    expect(multiselect).to_have_count(7)
    page.wait_for_timeout(2000)

    sorteddw = page.locator('#animals>option')
    unsorteddw = page.locator('#colors>option')

    #Unsored dropdown
    unsorted_options = [unsorted.strip() for unsorted in unsorteddw.all_text_contents()]
    unsorted_list = unsorted_options.copy()
    colorsdw = sorted(unsorted_options,reverse=True)
    print('Original Options: ',unsorted_list)
    print('Sorted options: ', colorsdw)

    #Sored dropdown
    sorted_options = [sort.strip() for sort in sorteddw.all_text_contents()]
    sorted_list = sorted_options.copy()
    animalesdw = sorted(sorted_options)
    print('Original Options: ',sorted_list)
    print('Sorted options: ', animalesdw)