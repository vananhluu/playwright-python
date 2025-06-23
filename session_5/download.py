import asyncio

from playwright.async_api import Playwright, async_playwright


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://demoqa.com/upload-download")
    async with page.expect_download() as download_info:
        # Wait for the download to start and get the download object: click the download button
        await page.locator("//a[@id='downloadButton']").click()
    download = await download_info.value
    # Save the download file
    download_path = await download.path()
    await download.save_as("./download_folder/" + download.suggested_filename)
    print(f"File downloaded to: {download_path}")

    await browser.close()



async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





