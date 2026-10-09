import pytest
from playwright.async_api import expect
from pathlib import Path
# File_downloads
# @pytest.mark.asyncio
# async def test_frm(async_page):
#     await async_page.goto("https://the-internet.herokuapp.com/download")
#     await async_page.wait_for_timeout(5000)
#     download_folder = Path("downloads")
#     download_folder.mkdir(exist_ok=True)

#     ele =   async_page.get_by_text("app.js")

#     # event
#     async with async_page.expect_download() as download_info:
#         await ele.click() # project :-->
#     download = await download_info.value
#     fn = download.suggested_filename
#     fp = download_folder/fn
#     await download.save_as(str(fp))
#     assert fp.exists()
    
    
# mouse hover    
# @pytest.mark.asyncio
# async def test_download(async_page):
#     await async_page.goto("https://demowebshop.tricentis.com/")
#     ele =  async_page.locator("(//a[contains(text(),'Computers')])[1]")
#     await ele.hover()
#     ele1 = async_page.locator("(//a[contains(text(),'Desktops')])[1]")
#     await expect(ele1).to_be_visible()
#     await ele1.click()
#     print(await async_page.title())
#     await async_page.wait_for_timeout(5000)   
    
    
#double click
# @pytest.mark.asyncio
# async def test_double_click(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")
#     button =  async_page.get_by_text("Copy Text")
#     await button.dblclick()
#     ele = async_page.locator("#field2")
#     print(await ele.input_value())    
    
#drag and drop
@pytest.mark.asyncio
async def test_double_click(async_page):
    await async_page.goto("https://demo.guru99.com/test/drag_drop.html")
    se =  async_page.locator("(//a[@class='button button-orange'])[5]")
    te = async_page.locator("(//li[@class='placeholder'])[1]")
    await async_page.wait_for_timeout(5000) 
    await se.drag_to(te)    