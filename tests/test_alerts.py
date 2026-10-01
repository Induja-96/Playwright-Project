
import pytest
from playwright.async_api import expect


async def handle_alerts(dialog):
    print("alert type =", dialog.type)
    print("alert msg =", dialog.message)
    await dialog.accept()


@pytest.mark.asyncio
async def test_alerts(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    async_page.on("dialog", handle_alerts)

    await async_page.locator("//input[@type='submit']").click()
    await async_page.locator("#small-searchterms").fill("abc")


async def handle_confirm_alerts(dialog):
    print("alert type =", dialog.type)
    print("alert msg =", dialog.message)
    await dialog.accept()


@pytest.mark.asyncio
async def test_confirm_alert(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")

    async_page.on("dialog", handle_confirm_alerts)

    await async_page.locator("#confirmBtn").click()

    msg = async_page.locator("#demo")

    await expect(msg).to_contain_text("You pressed OK!")




@pytest.mark.asyncio
async def test_check_box(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")

    check_box = async_page.locator("#sunday")

    await check_box.check()

    await expect(check_box).to_be_checked()

