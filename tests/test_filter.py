import pytest
from playwright.async_api import expect

# @pytest.mark.asyncio
# async def test_filter(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     products =  async_page.locator(".product-title")
#     simple_comp = products.filter(has_text="Simple Computer")
#     count = await simple_comp.count()
#     print("num simple computer" ,count )
#     await simple_comp.first.click()
    
# @pytest.mark.asyncio
# async def test_filter(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     products =  async_page.locator(".product-title").filter(has= async_page.get_by_role("link",name="Simple Computer"))
    
#     await products.click(button = 'right')
#     await async_page.wait_for_timeout(5000) 
    
# 

    
# @pytest.mark.asyncio
# async def test_filter(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     await async_page.pause()
#     login = async_page.get_by_role("link",name="Log in")
#     await login.click()
#     msg = async_page.get_by_text("Welcome, Please Sign In!")
#     await expect(msg).to_be_visible()    

import asyncio
import re
from playwright.async_api import Playwright, async_playwright, expect


async def run(playwright: Playwright) -> None:
    browser = await playwright.chromium.launch(headless=False)
    context = await browser.new_context()
    page = await context.new_page()
    await page.goto("https://demowebshop.tricentis.com/")
    await page.get_by_role("link", name="Log in").click()
    await page.get_by_role("link", name="Log in").click()
    await page.goto("https://demowebshop.tricentis.com/login")
    await page.get_by_role("heading", name="Welcome, Please Sign In!").click()
    await expect(page.locator("#small-searchterms")).to_be_visible()
    await page.locator("#small-searchterms").click()
    await page.locator("#small-searchterms").fill("book")
    await page.get_by_role("button", name="Search").click()
    await page.get_by_role("link", name="Books").first.click()
    await page.get_by_role("link", name="Books").nth(1).click()
    await expect(page.get_by_role("listitem").filter(has_text="Books").nth(2)).to_be_visible()
    await expect(page.get_by_role("link", name="Computing and Internet", exact=True)).to_be_visible()
    await page.locator(".rating > div").first.click()
    await expect(page.get_by_role("button", name="Add to cart").first).to_be_visible()

    # ---------------------
    await context.close()
    await browser.close()


async def main() -> None:
    async with async_playwright() as playwright:
        await run(playwright)


asyncio.run(main())