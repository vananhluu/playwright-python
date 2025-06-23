import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/webtables")
    expected_headers = ['First Name','Last Name', 'Age', 'Email', 'Salary', 'Department','Action']
    header_element = page.locator("//div[@class='rt-resizable-header-content']")
    count = await header_element.count()

    actual_headers = []
    for header in range(count):
        header_text = await header_element.nth(header).text_content()
        print(header_text)
        actual_headers.append(header_text)
    print(actual_headers)

    assert actual_headers == expected_headers, f"Header mismatch!\nGot: {actual_headers}"

async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





