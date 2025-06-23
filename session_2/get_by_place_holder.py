from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # launch a browser: headless: chay trinh duyet ma khong can hien thi giao dien (ko hien cua so)=> false thi se mo ra trang web
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new tab
    page = browser.new_page()
    # go to url
    page.goto("https://www.saucedemo.com")
    user_name = page.get_by_placeholder("Username")
    user_name.highlight()
    user_name.fill("testing4everyone")
    password = page.get_by_placeholder("Password")
    password.highlight()
    password.fill("password of testing4everyone")


