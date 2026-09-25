import pytest

# @pytest.mark.asyncio
# async def test_actions_click_db_(async_page):
#     await async_page.goto("https://demo.guru99.com/test/simple_context_menu.html")
#     dbc = async_page.locator("//button[text()='Double-Click Me To See Alert']")
#     await dbc.dblclick()
    
   
@pytest.mark.asyncio
async def test_login_(async_page):  
    await async_page.goto("https://agents.akbartravelsonline.com/b2bplus/login")
    await async_page.locator("#mat-input-1").fill("abc")
    await async_page.locator("#mat-input-2").fill("abc@123")
    await async_page.locator("//div[text()=' Sign In ']").click()
        
@pytest.mark.asyncio
async def test_reg_(async_page):
    await async_page.goto("https://agents.akbartravelsonline.com/b2bplus/apisign-up")
    await async_page.locator("#mat-input-0").fill("abc")
    await async_page.locator("#mat-input-1").fill("abc@gmail.com") 
    await async_page.locator("#mat-input-2").fill("1234567899")
    # time 
    async_page.wait_for_timeout(10000)
    await async_page.locator("//span[text()='Submit']").click()
    ele = await async_page.locator("//p[text()='Get Ready For Integration! Our Team Will Contact You Shortly.']")