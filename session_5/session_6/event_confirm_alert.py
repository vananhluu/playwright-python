from playwright.sync_api import sync_playwright

def handle_accept_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.accept()
    print("Accept successfully")

def handle_dismiss_alert(dialog):
    print("Alert opened: ", dialog)
    dialog.dismiss()
    print("Cancel successfully")


with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # page.on("dialog",handle_accept_alert)
    page.on("dialog",handle_dismiss_alert)

    page.goto("https://demoqa.com/alerts")
    page.locator("//button[@id='confirmButton']").click()
    text_result = page.locator("//span[@id='confirmResult']").text_content()
    print("Result:", text_result)
    assert text_result == "You selected Cancel", "Text does not match expected value"

    page.close()
