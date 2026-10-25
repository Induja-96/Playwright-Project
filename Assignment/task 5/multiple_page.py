
import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_product_state_retention(async_page):

    await async_page.goto("https://www.amazon.in")

    # Search for a product
    await async_page.locator("#twotabsearchtextbox").fill("iPhone 16")
    await async_page.locator("#twotabsearchtextbox").press("Enter")

    # Capture product title from search results
    product = async_page.locator(
        "div[data-component-type='s-search-result']"
    ).first

    await expect(product).to_be_visible()

    search_title = await product.locator("h2 a span").inner_text()
    print("Search result product:", search_title)

    # Open product detail page
    await product.locator("h2 a").click()

    await expect(async_page.locator("#productTitle")).to_be_visible()

    detail_title = await async_page.locator("#productTitle").inner_text()
    print("Product detail title:", detail_title)

    # Verify product title
    assert search_title in detail_title, "Product title mismatch"

    # Capture product URL before navigation
    product_url = async_page.url
    print("Product URL:", product_url)

    # Add product to cart
    await async_page.locator("#add-to-cart-button").click()

    # Open cart
    await async_page.goto("https://www.amazon.in/gp/cart/view.html")

    cart_items = async_page.locator(".sc-list-item")

    await expect(cart_items.first).to_be_visible()

    cart_text = await cart_items.first.inner_text()
    print("Cart item:", cart_text)

    # Verify same product is present in cart
    assert detail_title in cart_text or search_title in cart_text, (
        "Selected product is not present in the cart"
    )

    # Navigate back to product detail page
    await async_page.goto(product_url)

    await expect(async_page.locator("#productTitle")).to_be_visible()

    restored_title = await async_page.locator("#productTitle").inner_text()

    # Verify product information is retained
    assert restored_title == detail_title, "Product information changed after navigation"

    print("Product information retained successfully")
