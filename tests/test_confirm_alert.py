import pytest
from playwright.async_api import expect


async def handle_prompt_alert(dialog):
    print("Alert type:", dialog.type)
    print("Alert message:", dialog.message)

    # Enter ABC into the prompt and click OK
    await dialog.accept("ABC")


@pytest.mark.asyncio
async def test_prompt_alert(async_page):
    # Open the website
    await async_page.goto( "https://testautomationpractice.blogspot.com/")

    # Register the dialog handler BEFORE clicking the button
    async_page.on("dialog", handle_prompt_alert)

    # Click the Prompt button
    await async_page.locator("#promptBtn").click()

    # Verify the result displayed on the page
    msg = async_page.locator("#demo")

    await expect(msg).to_have_text("Hello ABC! How are you today?" )