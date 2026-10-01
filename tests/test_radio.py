import pytest
from playwright.async_api import expect
@pytest.mark.asyncio
async def test_radio_button(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.wait_for_timeout(500)
    radio_buttons = await async_page.locator("//label[text()='Gender:']/..//input[@type='radio']").all()
    for rad in radio_buttons:
        await rad.click()
        expect(rad).to_be_checked()
        
        