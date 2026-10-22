import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_check(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")

    await async_page.wait_for_timeout(500)

    check_boxes = await async_page.locator(
        "//label[text()='Days:']/..//input[@type='checkbox']"
    ).all()

    # 1. Select at least two checkboxes
    await check_boxes[0].check()
    await check_boxes[1].check()

    # 2. Verify that both checkboxes are checked
    await expect(check_boxes[0]).to_be_checked()
    await expect(check_boxes[1]).to_be_checked()

    # 3. Uncheck the first checkbox
    await check_boxes[0].uncheck()

    # Verify that the first checkbox is no longer checked
    await expect(check_boxes[0]).not_to_be_checked()

    # 4. Final assertion: first unchecked, second checked
    await expect(check_boxes[0]).not_to_be_checked()
    await expect(check_boxes[1]).to_be_checked()