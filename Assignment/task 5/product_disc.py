
import pytest
from playwright.async_api import expect

# Scenario: Amazon India - Search Product and Validate Details

@pytest.mark.asyncio
async def test_amazon_product(async_page):

    await async_page.goto("https://www.amazon.in/")
    keyword = "iphone 16"
    expected_title = "iPhone 16"  # Product title to match

    # Search for product
    await async_page.locator("//input[@id='twotabsearchtextbox']").fill(keyword)
    await async_page.locator("//input[@id='twotabsearchtextbox']").press("Enter")

    # Wait for search results
    await async_page.wait_for_selector(
        "//div[@data-component-type='s-search-result']"
    )

    # Get all product results
    products = async_page.locator(
        "//div[@data-component-type='s-search-result']"
    )

    selected_product = None
    product_title = None

    # Select product by matching the visible title
    for i in range(await products.count()):
        product = products.nth(i)

        title_locator = product.locator(
            "xpath=.//h2//span"
        )

        if await title_locator.count() > 0:
            title = (await title_locator.first.inner_text()).strip()

            if expected_title.lower() in title.lower():
                selected_product = product
                product_title = title
                break

    # Verify matching product is found
    assert selected_product is not None, (
        f"Product '{expected_title}' not found"
    )

    print("Selected Product:", product_title)

    # Get product URL
    product_link = selected_product.locator("xpath=.//h2/a").first
    product_url = await product_link.get_attribute("href")

    if product_url.startswith("/"):
        product_url = "https://www.amazon.in" + product_url

    print("Product URL:", product_url)

    # Open product detail page
    await async_page.goto(product_url)

    # Get product title from detail page
    detail_title = async_page.locator("//span[@id='productTitle']")
    await expect(detail_title).to_be_visible()

    detail_product_title = (await detail_title.inner_text()).strip()

    print("Product Detail Title:", detail_product_title)

    # Validate title between search result and detail page
    assert (
        product_title.lower() in detail_product_title.lower()
        or detail_product_title.lower() in product_title.lower()
    ), "Product title does not match"

    # Get product price when visible
    price_locator = async_page.locator(
        "(//span[contains(@class,'a-price')]/span[@class='a-offscreen'])[1]"
    )

    price = "Price not visible"

    if await price_locator.count() > 0:
        if await price_locator.first.is_visible():
            price = (await price_locator.first.inner_text()).strip()

    print("Product Price:", price)
    
    print("Final Product URL:", async_page.url)
