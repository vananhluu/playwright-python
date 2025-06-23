import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/upload-download")

    await page.locator("//input[@id='uploadFile']").set_input_files("./download_folder/sampleFile.jpeg")
    # Remove all the selected files
    await page.locator("//input[@id='uploadFile']").set_input_files([])

    # Upload again
    await page.locator("//input[@id='uploadFile']").set_input_files("./download_folder/sampleFile.jpeg")
    await expect(page.locator("//p[@id='uploadedFilePath']")).to_contain_text("sampleFile.jpeg")


    await browser.close()



async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





