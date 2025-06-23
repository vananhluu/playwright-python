from playwright.sync_api import sync_playwright

input_message = "Van Anh"
def handle_prompt_alert(dialog):
    print("Prompt opened: ", dialog.message)
    dialog.accept(input_message)
    print(f"Entered the text: {input_message} and clicked OK")



with sync_playwright() as playwright:
    browser = playwright.chromium.launch(headless=False, slow_mo=500)
    page = browser.new_page()

    # page.on("dialog",handle_accept_alert)
    page.on("dialog",handle_prompt_alert)

    page.goto("https://demoqa.com/alerts")
    page.locator("//button[@id='promtButton']").click()

    # Verify the result get from page
    text_result = page.locator("//span[@id='promptResult']").text_content()
    assert text_result == f"You entered {input_message}", f"The text does not match. Found: {text_result}"
    print(text_result)


    page.close()
