from playwright.sync_api import Page, expect, sync_playwright

def test_frame(page:Page):
    page.goto('https://ui.vision/demo/webtest/frames/')
    frames = page.frames
    print('Number of frames: ', len(frames))
    # frame1 = page.frame_locator('frame[src="frame_1.html"]') #method 1 for get the frame
    frame1 = page.frame(url = 'https://ui.vision/demo/webtest/frames/frame_1') #mathod 2 get the frame
    # frame1 = page.frame('name ofthe frame') #mathod 3 get the frame
    frame1.locator('input[name="mytext1"]').fill('Frame 1 Text')
    expect(frame1.locator('input[name="mytext1"]')).to_have_value('Frame 1 Text')
    page.wait_for_timeout(5000)