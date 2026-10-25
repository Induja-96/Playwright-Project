import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_add_to_cart(async_page):

    # Open Amazon
    await async_page.goto("https://www.amazon.in/")

    # Search product
    search_box = async_page.locator("#twotabsearchtextbox")
    await search_box.fill("iphone 16")
    await search_box.press("Enter")

    # Select matching product
    products = async_page.locator(
        "//div[@data-component-type='s-search-result']"
    )

    await products.first.wait_for(state="visible")

    product_name = "iphone 16"

    for i in range(await products.count()):
        product = products.nth(i)
        title = await product.locator("h2").inner_text()

        if product_name.lower() in title.lower():
            product_link = product.locator("h2 a")
            break

    # Open product details
    await product_link.click()

    # Validate product title
    title = async_page.locator("#productTitle")
    await expect(title).to_be_visible()

    print("Product title:", await title.inner_text())

    # Validate Add to Cart button
    add_to_cart = async_page.locator("#add-to-cart-button")
    await expect(add_to_cart).to_be_visible()

    # Add product to cart
    await add_to_cart.click()

    # Open cart
    await async_page.locator("#nav-cart").click()

    # Validate cart item
    cart_item = async_page.locator(
        "div[data-item-index]"
    ).first

    await expect(cart_item).to_be_visible()

    print("Cart item:", await cart_item.inner_text())

    # Validate quantity
    quantity = cart_item.locator("select[name='quantity']")
    await expect(quantity).to_be_visible()
    await expect(quantity).to_have_value("1")

    # Proceed to checkout
    checkout_button = async_page.locator(
        "input[name='proceedToRetailCheckout']"
    )
    await expect(checkout_button).to_be_visible()
    await checkout_button.click()

    # Stop before placing the order or submitting payment
    print("Checkout opened. Stopping before final order submission.")