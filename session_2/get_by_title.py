from playwright.sync_api import sync_playwright

with sync_playwright() as playwright:
    # launch a browser: headless: chay trinh duyet ma khong can hien thi giao dien (ko hien cua so)=> false thi se mo ra trang web
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    # create a new tab
    page = browser.new_page()
    # go to url
    page.goto("https://parabank.parasoft.com/parabank/index.htm")
    user_name = page.get_by_title("ParaBank")


