
import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_visibility(async_page):
    await async_page.goto( "https://testautomationpractice.blogspot.com/" )

    # 1. Verify that the heading is visible
    heading = async_page.locator("h1")
    await expect(heading).to_be_visible()
    print("Heading is visible")

    # 2. Verify that the dropdown menu is hidden
    hidden_menu = async_page.locator(".dropdown-content").first
    await expect(hidden_menu).to_be_hidden()
    print("Dropdown menu is hidden")

    # 3. Hover over the dropdown to make the menu visible
    dropdown = async_page.locator(".dropdown").first
    await dropdown.hover()

    # 4. Verify that the dropdown menu is visible after hovering
    await expect(hidden_menu).to_be_visible()
    print("Dropdown menu is visible after hovering")

    # 5. Verify that the name input field is enabled
    name_input = async_page.locator("#name")
    await expect(name_input).to_be_enabled()
    print("Name input is enabled")

    # 6. Verify that the alert button is enabled
    alert_button = async_page.locator("#alertBtn")
    await expect(alert_button).to_be_enabled()
    print("Alert button is enabled")

