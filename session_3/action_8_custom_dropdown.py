import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/automation-practice-form")
    await page.locator("//div[@id='state']").click()


    



async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





