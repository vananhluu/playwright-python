from playwright.sync_api import sync_playwright

def handle_accept_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.accept()
    print("Accept successfully")



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # page.on("dialog",handle_accept_alert)
    page.on("dialog",handle_accept_alert)

    page.goto("https://demoqa.com/alerts")
    page.locator("//button[@id='alertButton']").click()

    # page.close()
