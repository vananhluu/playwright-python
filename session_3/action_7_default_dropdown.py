import asyncio

from playwright.async_api import Playwright, async_playwright, expect


async def run(playwirght: Playwright):
    chromium = playwirght.chromium
    browser = await chromium.launch(headless=False, slow_mo= 500)
    page = await browser.new_page()
    await page.goto("https://egov.danang.gov.vn/reg")

    # Count the total number of options
    tinh_thuong_tru_options = page.locator("//select[@name='tinhThuongTru']/option")
    count = await tinh_thuong_tru_options.count()
    print(count)
    print(f"Total options in dropdown: {count}")

#     Print each option text
    for option in range(count):
        text = await tinh_thuong_tru_options.nth(option).text_content()
        print(text)

#   Select 1 option trong dropdown list
    await page.select_option("//select[@name='tinhThuongTru']",value = '20704')
    selected_value = await page.eval_on_selector("//select[@name='tinhThuongTru']","el => el.value" )
    print(f"Selected value: {selected_value}")
    assert selected_value == "20704", "Selected value is incorrect!"

    # Verify selected text
    selected_text = await page.eval_on_selector(
        "//select[@name='tinhThuongTru']", "el => el.options[el.selectedIndex].text"
    )
    print(f"Selected text: {selected_text}")
    assert selected_text.strip() == "phường Thới Hoà", "Selected text is incorrect!"

#     Check the dropdown is multi-select or single select

    is_multiselect = await page.eval_on_selector(
    "//select[@name='tinhThuongTru']", "el => el.multiple"
    )

    if is_multiselect:
        print("Dropdown is multi-select.")
    else:
        print("Dropdown is single-select.")



async def main():
    async with async_playwright() as playwright:
        await run(playwright)

asyncio.run(main())





