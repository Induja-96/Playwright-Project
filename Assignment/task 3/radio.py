
import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_radio_button(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")

    # 1. Identify all radio buttons
    radio_buttons = async_page.locator("input[type='radio']")
    count = await radio_buttons.count()
    print("Total radio buttons:", count)

    # 2. Print radio button labels/names
    for i in range(count):
        radio = radio_buttons.nth(i)
        label = await radio.get_attribute("value")
        name = await radio.get_attribute("name")
        print(f"Radio button {i + 1}: Name={name}, Value={label}")

    # 3. Select one radio button and verify it is checked
    male_radio = async_page.locator("#male")
    await male_radio.check()
    await expect(male_radio).to_be_checked()
    print("Male radio button is selected")

    # 4. Verify another radio button is not selected
    female_radio = async_page.locator("#female")
    await expect(female_radio).not_to_be_checked()
    print("Female radio button is not selected")
