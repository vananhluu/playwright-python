import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/buttons")

    # Click me button

    #     Press the button and keep it
    click_button = page.get_by_role("button", name = "Click Me")
    await click_button.highlight()
    await click_button.click(delay=500)

    # Double Click
    double_click_button = page.get_by_role("button", name = "Double Click Me")
    await double_click_button.highlight()
    await double_click_button.dblclick()

#   Right Click
    right_click_button = page.get_by_role("button", name = "Right Click Me")
    await right_click_button.highlight()
    await right_click_button.click(button="right")











async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





