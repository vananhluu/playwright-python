import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/checkbox")
    folder_checkbox = page.locator("//span[@class='rct-checkbox']")
    if await folder_checkbox.is_checked() == True and folder_checkbox.is_enabled() == True:
        await folder_checkbox.uncheck()
    else:
        await folder_checkbox.check()

    # await folder_checkbox.highlight()
    # await folder_checkbox.check()
    # await folder_checkbox.click()
    # await folder_checkbox.check()
    # await folder_checkbox.uncheck()
    await page.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





