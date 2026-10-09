#from playwright.async_api import expect
#import pytest


#@pytest.mark.asyncio
#async def test_Assertions(async_page):
    #await async_page.goto("https://demowebshop.tricentis.com/")
    #ele = async_page.locator(".topic-html-content-header")
    #expect(ele).to_be_visible()
    #print(ele.inner_text())
import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_Assertions1(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    await expect(async_page).to_have_title("Demo Web Shop")
    options = async_page.locator("//li[@class='answer']")
    await expect(options).to_have_count(4)