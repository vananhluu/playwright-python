from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # launch a browser: headless: chay trinh duyet ma khong can hien thi giao dien (ko hien cua so)=> false thi se mo ra trang web
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new tab
    page = browser.new_page()
    # go to url
    page.goto("https://bootswatch.com/default/")
    password_textbox = page.get_by_label("Password")
    password_textbox.highlight()
    password_textbox.fill("password_data")

    browser.close()


