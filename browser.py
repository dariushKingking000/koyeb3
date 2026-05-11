# browser.py - Docker version
import os
import sys
import json
from playwright.sync_api import sync_playwright

def run_browser(event_type, x=500, y=300):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=1000)
        page = browser.new_page()
        page.goto('https://www.google.com')
        
        if event_type == "take_screenshot":
            page.screenshot(path='/tmp/google.png')
            print("📸 /tmp/google.png")
        elif event_type == "copy_page":
            page.keyboard.press('Control+a')
            page.keyboard.press('Control+c')
            print("📋 کپی شد")
        elif event_type == "click_page":
            page.mouse.click(int(x), int(y))
            print(f"🖱️ کلیک {x},{y}")
            
        browser.close()

if __name__ == '__main__':
    event = sys.argv[1]
    x, y = sys.argv[2] if len(sys.argv)>2 else "500", sys.argv[3] if len(sys.argv)>3 else "300"
    run_browser(event, x, y)
