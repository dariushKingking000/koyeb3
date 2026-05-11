# browser_control.py - توی GitHub repo
from playwright.sync_api import sync_playwright
import sys
import json

def main(event):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto('https://www.google.com')
        
        if event == 'open_google':
            print("✅ گوگل باز شد")
        elif event == 'take_screenshot':
            page.screenshot(path='google.png')
            print("📸 اسکرین‌شات گرفته شد")
        elif event == 'copy_page':
            page.keyboard.press('Control+a')
            page.keyboard.press('Control+c')
            print("📋 کپی شد")
        elif event == 'click_page':
            payload = json.loads(sys.argv[2] if len(sys.argv)>2 else '{}')
            x, y = payload.get('x', 500), payload.get('y', 300)
            page.mouse.click(x, y)
            print(f"🖱️ کلیک: {x},{y}")
        
        browser.close()

if __name__ == '__main__':
    event_type = sys.argv[1]
    main(event_type)
