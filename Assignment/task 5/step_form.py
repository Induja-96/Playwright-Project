
import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_form_persistence(async_page):

    await async_page.goto("https://demoqa.com/automation-practice-form")

    # Enter test data in the form
    await async_page.locator("#firstName").fill("Test")
    await async_page.locator("#lastName").fill("User")
    await async_page.locator("#userEmail").fill("testuser@example.com")
    await async_page.locator("#currentAddress").fill("100 Test Street")

    # Verify entered data
    assert await async_page.locator("#firstName").input_value() == "Test"
    assert await async_page.locator("#lastName").input_value() == "User"
    assert await async_page.locator("#userEmail").input_value() == "testuser@example.com"

    print("Form data entered successfully")

    # Navigate to another section of the page
    await async_page.locator("#currentAddress").scroll_into_view_if_needed()

    # Check whether the data is still populated
    assert await async_page.locator("#firstName").input_value() == "Test"
    assert await async_page.locator("#lastName").input_value() == "User"
    assert await async_page.locator("#userEmail").input_value() == "testuser@example.com"
    assert await async_page.locator("#currentAddress").input_value() == "100 Test Street"

    print("Form data retained after navigation")

