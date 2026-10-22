import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_alerts(async_page):
    await async_page.goto(
        "https://testautomationpractice.blogspot.com/"
    )

    button = async_page.locator("#alertBtn")

    print("Button count =", await button.count())
    print("Page title =", await async_page.title())

    async def handle_alert(dialog):
        print("alert type =", dialog.type)
        print("alert msg =", dialog.message)
        await dialog.accept()

    async_page.once("dialog", handle_alert)

    await button.click()
    
    
 #Confirm dialog — OK 
@pytest.mark.asyncio
async def test_confirm_alert_ok(async_page):
    await async_page.goto(
        "https://testautomationpractice.blogspot.com/"
    )

    async def handle_confirm(dialog):
        print("alert type =", dialog.type)
        print("alert msg =", dialog.message)
        await dialog.accept()

    async_page.once("dialog", handle_confirm)

    await async_page.locator("#confirmBtn").click()

    msg = async_page.locator("#demo")
    await expect(msg).to_contain_text("You pressed OK!")   
    
    
    
 #Confirm dialog — Cancel   
@pytest.mark.asyncio
async def test_confirm_alert_cancel(async_page):
    await async_page.goto(
        "https://testautomationpractice.blogspot.com/"
    )

    async def handle_confirm(dialog):
        print("alert type =", dialog.type)
        print("alert msg =", dialog.message)
        await dialog.dismiss()

    async_page.once("dialog", handle_confirm)

    await async_page.locator("#confirmBtn").click()

    msg = async_page.locator("#demo")
    await expect(msg).to_contain_text("You pressed Cancel!")    
    
    
 #Prompt dialog   
@pytest.mark.asyncio
async def test_prompt_alert(async_page):
    await async_page.goto(
        "https://testautomationpractice.blogspot.com/"
    )

    async def handle_prompt(dialog):
        print("alert type =", dialog.type)
        print("alert msg =", dialog.message)
        await dialog.accept("Induja")

    async_page.once("dialog", handle_prompt)

    await async_page.locator("#promptBtn").click()

    msg = async_page.locator("#demo")
    
    await async_page.wait_for_timeout(5000)
    await expect(msg).to_contain_text("Induja")    