import pytest
from playwright.async_api import expect


# 1. Open a new tab and switch between pages
@pytest.mark.asyncio
async def test_new_tab(async_page):
    await async_page.goto("https://demoqa.com/browser-windows")

    # Original page details
    original_url = async_page.url
    original_title = await async_page.title()

    print("Original URL =", original_url)
    print("Original Title =", original_title)

    # Open a new tab
    async with async_page.expect_popup() as popup_info:
        button = async_page.locator("#tabButton")
        await expect(button).to_be_visible()
        await button.click()

    child_page = await popup_info.value
    await child_page.wait_for_load_state()

    # Verify that two pages are available
    pages = async_page.context.pages
    assert len(pages) == 2

    print("Number of pages =", len(pages))
    print("Child URL =", child_page.url)
    print("Child Title =", await child_page.title())

    # Perform an action on the child page
    heading = child_page.locator("#sampleHeading")
    await expect(heading).to_have_text("This is a sample page")

    # Return to the original page
    await async_page.bring_to_front()

    assert async_page.url == original_url
    assert await async_page.title() == original_title

    print("Returned URL =", async_page.url)
    print("Returned Title =", await async_page.title())


# 2. Open a new browser window
@pytest.mark.asyncio
async def test_new_window(async_page):
    await async_page.goto("https://demoqa.com/browser-windows")

    # Open a new window and wait for the popup event
    async with async_page.expect_popup() as popup_info:
        button = async_page.locator("#windowButton")
        await expect(button).to_be_visible()
        await button.click()

    window_page = await popup_info.value
    await window_page.wait_for_load_state()

    # Verify two pages are available
    pages = async_page.context.pages
    assert len(pages) == 2

    print("Number of pages =", len(pages))
    print("Window URL =", window_page.url)
    print("Window Title =", await window_page.title())

    # Perform an action on the new window
    heading = window_page.locator("#sampleHeading")
    await expect(heading).to_have_text("This is a sample page")

    # Return to the original page
    await async_page.bring_to_front()

    assert async_page.url == "https://demoqa.com/browser-windows"
    print("Original page URL =", async_page.url)
    print("Original page Title =", await async_page.title())
