import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwright: Playwright):
    chromium = playwright.chromium
    browser = await chromium.launch(headless=False, slow_mo = 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/text-box")

#     find the locator of textbox
    fullname_textbox = page.locator("//input[@id='userName']")
#       fill data to textbox
    await fullname_textbox.fill("Testing4Everyone")
    await fullname_textbox.clear()

    email_textbox = page.locator("//input[@id='userEmail']")
    await email_textbox.fill("testing4everyone@gmail.com")
    await email_textbox.fill("")

    address_textarea = page.locator("//textarea[@id='currentAddress']")
    await address_textarea.fill("You're correctly targeting a button element using a valid XPath expression.")
    await browser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())






