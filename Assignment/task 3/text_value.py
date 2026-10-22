import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_text_values(async_page):
    await async_page.goto("https://testautomationpractice.blogspot.com/")

    # 1. Get heading text
    heading = async_page.locator("h1")
    heading_text = await heading.text_content()

    print("Heading text =", heading_text)

    # text_content() retrieves the text content from the DOM element.
    # It can include text that is not currently visible.

    await expect(heading).to_contain_text("Automation")
    


    # 2. Enter a value into an input field
    input_box = async_page.locator("#name")
    await input_box.fill("Induja")

    input_value = await input_box.input_value()

    print("Input value =", input_value)

    # input_value() retrieves the current value entered in an input field.
    # It does not retrieve the text content of an ordinary element.

    await expect(input_box).to_have_value("Induja")


    # 3. Get inner text from a container
    container = async_page.locator("body")
    container_text = await container.inner_text()

    print("Container inner text =")
    print(container_text)

    # inner_text() retrieves the rendered text as a user sees it.
    # It includes text from multiple child elements and respects visibility.

    await expect(container).to_contain_text("Name")


