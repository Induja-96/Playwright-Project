import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
# async def test_check_box(async_page):
#     await async_page.goto("https://testautomationpractice.blogspot.com/")

#     check_box = async_page.locator("#sunday")
#     await expect(check_box).not_to_be_checked()

#     await check_box.check()

#     await expect(check_box).to_be_checked()

async def test_check_box(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")
    await async_page.wait_for_timeout(500)
    check_boxes = await async_page.locator("//label[text()='Days:']/..//input[@type='checkbox']").all()
    await async_page.wait_for_timeout(500)
    for check_box in check_boxes:
        await check_box.click()