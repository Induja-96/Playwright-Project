
import pytest
from playwright.async_api import expect

@pytest.mark.asyncio
async def test_product_availability(async_page):
    await async_page.goto("https://www.amazon.in/")

    await async_page.locator("#twotabsearchtextbox").fill("iPhone 16")
    await async_page.locator("#twotabsearchtextbox").press("Enter")

    product = async_page.locator("div[data-component-type='s-search-result']").first
    await expect(product).to_be_visible()

    await product.locator("h2 a").click()
    await async_page.wait_for_load_state("domcontentloaded")

    add_to_cart = async_page.locator("#add-to-cart-button")

    if await add_to_cart.is_visible():
        if await add_to_cart.is_enabled():
            print("Product is available. Add to Cart is enabled.")

            await add_to_cart.click()
            print("Product added to cart.")

            await async_page.goto("https://www.amazon.in/gp/cart/view.html")

            cart_item = async_page.locator(".sc-list-item").first
            await expect(cart_item).to_be_visible()
            print("Cart validation passed.")

        else:
            print("Product unavailable: Add to Cart is disabled.")
            print("Cart validation skipped because the product cannot be added.")

    else:
        print("Product unavailable: Add to Cart control is missing or not visible.")
        print("Cart validation skipped because the control is unavailable.")
