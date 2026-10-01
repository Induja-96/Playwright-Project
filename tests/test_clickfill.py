import pytest
from playwright.async_api import expect

#@pytest.mark.asyncio
#sync def test_click_fill_type_clear_waits(async_page):
  #  await async_page.goto("https://www.google.com/")
   # await expect(async_page).to_have_title("Google")
    #ele= await async_page.locator("textarea[name='q']")
    #await ele.type("Mobile")
    #await ele.clear()
    #await ele.fill("Books")
    #await ele.press("Enter")
    #await expect(async_page).to_have_title("Books - Google Search")
    
#import pytest

#@pytest.mark.asyncio
#async def test_get_text_attribute(async_page):
    #await async_page.goto("https://demowebshop.tricentis.com/")
   # print(await async_page.locator("label[for='pollanswers-1']").inner_text())
    #print(await async_page.get_by_text("$25 Virtual Gift Card").first.get_attribute("href"))
    
import pytest

@pytest.mark.asyncio
async def test_get_text_attribute(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    ele = async_page.locator("#pollanswers-1")
    print(await ele.inner_text())
    ele1 = async_page.get_by_text("$25 Virtual Gift Card")
    print(await ele1.get_attribute("href"))