
import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_auth_form(async_page):

    await async_page.goto("https://demowebshop.tricentis.com/")

    await async_page.get_by_text("Log in").click()

    await async_page.locator("#Email").fill("zxcvbn12@gmail.com")
    await async_page.locator("#Password").fill("123456")

    await async_page.locator("//input[@value='Log in']").click()

    await expect(async_page.get_by_text("Log out")).to_be_visible()

    print("User logged in successfully")

    await async_page.context.storage_state(path="demosession.json")

    print("Session saved successfully")
