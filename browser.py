from playwright.sync_api import sync_playwright
import sys
import os

def main(event_type, click_x="500", click_y="300"):
    print(f"🎯 دستور: {event_type}")
    
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False, slow_mo=500)
        page = browser.new_page()
        page.set_viewport_size({"width": 1366, "height": 768})
        page.goto('https://www.google.com', wait_until='networkidle')
        
        if event_type == "open_google":
            print("✅ گوگل باز شد - 10 ثانیه صبر...")
            page.wait_for_timeout(10000)
            
        elif event_type == "take_screenshot":
            page.screenshot(path='google.png', full_page=True)
            print("📸 اسکرین‌شات ذخیره شد: google.png")
            
        elif event_type == "copy_page":
            page.keyboard.press('Control+a')
            page.keyboard.press('Control+c')
            print("📋 کل صفحه کپی شد")
            
        elif event_type == "click_page":
            page.mouse.click(int(click_x), int(click_y))
            print(f"🖱️ کلیک شد در: {click_x}, {click_y}")
        
        browser.close()
        print("🏁 تمام!")

if __name__ == '__main__':
    event_type = sys.argv[1] if len(sys.argv) > 1 else "open_google"
    click_x = sys.argv[2] if len(sys.argv) > 2 else "500"
    click_y = sys.argv[3] if len(sys.argv) > 3 else "300"
    main(event_type, click_x, click_y)
