import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://demowebshop.tricentis.com/")
    await page.get_by_role("link", name="Books").nth(1).click()
    await expect(page.get_by_role("link", name="Fiction", exact=True)).to_be_visible()
    await page.get_by_role("link", name="Books").nth(1).click()
    await page.get_by_role("listitem").filter(has_text="Books").nth(2).click()
    await page.locator("#products-viewmode").select_option("https://demowebshop.tricentis.com/books?viewmode=list")
    await page.goto("https://demowebshop.tricentis.com/books?viewmode=list")
    await page.locator("#products-pagesize").select_option("https://demowebshop.tricentis.com/books?viewmode=list&pagesize=4")
    await page.goto("https://demowebshop.tricentis.com/books?viewmode=list&pagesize=4")
    await page.get_by_role("link", name="Computers").nth(1).click()
    await page.get_by_role("link", name="Desktops").first.click()
    await expect(page.get_by_role("link", name="Build your own cheap computer", exact=True)).to_be_visible()
    await page.get_by_role("button", name="Add to cart").first.click()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())
