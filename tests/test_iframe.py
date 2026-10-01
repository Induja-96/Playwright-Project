import pytest
from playwright.async_api import expect

# @pytest.mark.asyncio

# async def test_frm(async_page):
#     await async_page.goto("https://demo.guru99.com/test/guru99home/", wait_until="load")
#     async_page.wait_for_url
#     await async_page.wait_for_timeout(5000)
#     frame = assync_page.frame_locator('#a077aa5e')
#     await async_page.wait_for_timeout(5000)
#     img = frame.locator("//img[@src='Jmeter720.png]")

#     await expect(img).to_be_visible()
#     await async_page.wait_for_timeout(500)
#     await img.click()
#     email = async_page.get_by_placeholder("Enter Email")
#     await expect(email).to_be_visible()
#     await email.fill("abc@gmail.com")
#     print(email.input_value)
    
    
#multiple windows
# @pytest.mark.asyncio
# async def test_frm(async_page):
#    await async_page.goto("https://demowebshop.tricentis.com/")
#    # --------------------------Facebook
#    async with async_page.expect_popup() as popup_info:
#        facebook = async_page.get_by_text("Facebook")
#        await expect(facebook).to_be_visible()
#        await facebook.click()
#    facebook_page = await popup_info.value
#    await facebook_page.wait_for_load_state()
#    print(facebook_page.url)
#    print(facebook_page.title)
#    email = facebook_page.locator("(//input[@name='email'])[2]")
#    await expect(email).to_be_visible()
#    await email.fill("abc@gmail.com")
#    print(await email.input_value())
#    # come back to demo webshop
#    await async_page.bring_to_front()
#    # ------ event google
#    async with async_page.expect_popup() as popup_info:
#        google = async_page.get_by_text("Google+")
#        await expect(google).to_be_visible()
#        await google.click()
#    google_page = await popup_info.value
#    await google_page.locator("//input[@name='q']").fill("Books")
   
   #fileupload
@pytest.mark.asyncio
async def test_frm(async_page):
   await async_page.goto("https://the-internet.herokuapp.com/upload")
   file_input = async_page.locator("#file-upload")
   await file_input.set_input_files("/home/user/Documents/DOB admin.odt")
   await async_page.locator("#file-submit").click()
   await async_page.wait_for_timeout(5000)
   msg = async_page.get_by_text("File Uploaded!")
   await expect(msg).to_be_visible()