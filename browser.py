import sys
from playwright.sync_api import sync_playwright

event = sys.argv[1] if len(sys.argv) > 1 else "screenshot"

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto('https://google.com')
    
    if event == "screenshot":
        page.screenshot(path='screenshot.png')
        print("📸 screenshot.png ذخیره شد!")
    
    browser.close()
    print("✅ تمام!")
