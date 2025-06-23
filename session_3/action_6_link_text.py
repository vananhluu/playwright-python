import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/links")

    simple_link_text = page.locator("//a[@id='simpleLink']")
    await simple_link_text.highlight()
    await expect(simple_link_text).to_have_text("Home")
    await simple_link_text.click()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





