from playwright.sync_api import Page, expect, sync_playwright

def test_iframe(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')

    frames = page.frame(url='https://ui.vision/demo/webtest/frames/frame_3')
    frames.locator('input[name="mytext3"]').fill('Frame 3 Text')
    page.wait_for_timeout(2000)

    child_frame = frames.child_frames
    print('Child Frames: ', len(child_frame))
    page.wait_for_timeout(2000)

    iframe = child_frame[0]

    radio_btn = iframe.get_by_label('I am a human')
    radio_btn.click()
    expect(radio_btn).to_be_checked()

    #Another method
    # radio_label = iframe.locator("label", has_text="I am a human")
    # radio_label.click()

    iframe.get_by_label('Web Testing').click()
    expect(iframe.get_by_label('Web Testing')).to_be_checked()

    next_btn = iframe.locator('div[role="button"]').filter(has_text="Next")
    next_btn.click()

    page.wait_for_timeout(2000)
    short_txt = iframe.locator('input[type="text"]').fill('Iframe Short Text')
    expect(iframe.locator('input[type="text"]')).to_have_value('Iframe Short Text')

    page.wait_for_timeout(2000)
    long_txt = iframe.locator('textarea[aria-label="Your answer"]').fill('Iframe Long Answer')
    expect(iframe.locator('textarea[aria-label="Your answer"]')).to_have_value('Iframe Long Answer')

    submit_btn = iframe.locator('div[role="button"]').filter(has_text="Submit")
    submit_btn.click()

    page.wait_for_timeout(2000)

    frames5 = page.frame(url='https://ui.vision/demo/webtest/frames/frame_5')
    frames5.locator('input[name="mytext5"]').fill('Frame 5 Text')
    page.wait_for_timeout(2000)

    frames5.locator('a[href="https://a9t9.com"]').click()
    page.wait_for_timeout(2000)
    target_element = frames5.locator('span[class="highlight"]').get_by_text('1. Get Ui.Vision')
    expect(target_element).to_have_text('1. Get Ui.Vision')
    page.wait_for_timeout(5000)
