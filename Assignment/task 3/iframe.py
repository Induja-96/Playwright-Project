import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_iframe_locator(async_page):
    await async_page.goto("https://demo.guru99.com/test/guru99home/", wait_until="load")

    # 1. Locate the iframe using frame_locator()
    frame = async_page.frame_locator( "//iframe[@name='a077aa5e']")

    # 2. Locate the image inside the iframe
    image = frame.locator("//img[contains(@src, 'Jmeter720.png')]" )

    # 3. Verify that the image is visible
    await expect(image).to_be_visible()
    print("JMeter image is visible")

    # 4. Interact with the image
    await image.hover()
    print("Hovered over the JMeter image")


@pytest.mark.asyncio
async def test_iframe_reference(async_page):
    await async_page.goto(
        "https://demo.guru99.com/test/guru99home/",
        wait_until="load"
    )

    # 5. Print the name and URL of each frame
    for frame in async_page.frames:
        print("Frame name:", frame.name)
        print("Frame URL:", frame.url)

    # 6. Find the iframe using its name
    frame = next(
        (
            f for f in async_page.frames
            if f.name == "a077aa5e"
        ),
        None
    )

    # 7. Verify that the iframe exists
    assert frame is not None, "Required iframe was not found"

    # 8. Locate the image using the Frame object
    image = frame.locator(
        "//img[contains(@src, 'Jmeter720.png')]"
    )

    # 9. Verify that the image is visible
    await expect(image).to_be_visible()
    print("JMeter image is visible using the Frame object")

    # 10. Interact with the image
    await image.hover()
    print("Hovered over the image using the Frame object")


# Difference:
# frame_locator() locates an iframe using a selector.
# A Frame object represents a specific frame and lets us
# locate and interact with its elements directly.