import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()

    # View port
    await page.set_viewport_size({"width": 393, "height": 852})

    await page.goto("https://demoqa.com/links")

    full_name = page.locator("//input[@id='userName']")
    await full_name.fill("testing4everyone")
    await full_name.clear()

    email = page.locator("//input[@id='userEmail']")
    await email.fill("testing4everyone")
    await email.fill("")

    permanent_address = page.locator("//textarea[@id='permanentAddress']")
    await permanent_address.fill("I have attached my resume for your review. I would welcome the chance to discuss how my skills, my knowledge, my responsibilities make a suitable candidate for this position.")
    await permanent_address.fill("")


    await page.close()

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





