import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_product_selection(async_page):

    # Open Amazon India
    await async_page.goto(
        "https://www.amazon.in/",
        wait_until="domcontentloaded"
    )

    # Search for the product
    search_box = async_page.locator("#twotabsearchtextbox")
    await search_box.fill("iphone 16")
    await search_box.press("Enter")

    # Wait for search results
    products = async_page.locator(
        "div[data-component-type='s-search-result']"
    )

    await products.first.wait_for(state="visible", timeout=20000)

    # Product name to select
    product_name = "iphone 16"

    selected_title = ""
    selected_url = ""

    # Find the matching product dynamically
    product_count = await products.count()
    print("Total products found:", product_count)

    for i in range(product_count):

        # Get each product card
        product = products.nth(i)

        # Get product title
        title_locator = product.locator("h2").first

        if await title_locator.count() == 0:
            continue

        title = (await title_locator.inner_text()).strip()
        print(f"Product {i + 1}: {title}")

        # Match the required product
        if product_name.lower() in title.lower():

            # Get the product link from the matching card
            product_link = product.locator("h2 a").first

            if await product_link.count() > 0:

                href = await product_link.get_attribute("href")

                if href:
                    selected_title = title

                    # Prepare the complete product URL
                    if href.startswith("http"):
                        selected_url = href
                    else:
                        selected_url = "https://www.amazon.in" + href

                    print("Matching product found:", selected_title)
                    break

    # Validate that the product was found
    assert selected_url, (
        f"No product matching '{product_name}' was found "
        "with a valid product link."
    )

    print("Selected product:", selected_title)
    print("Selected product URL:", selected_url)

    # Open the product details page directly
    await async_page.goto(
        selected_url,
        wait_until="domcontentloaded",
        timeout=30000
    )

    # Validate the product title
    details_title = async_page.locator("#productTitle")

    await expect(details_title).to_be_visible(timeout=20000)

    actual_title = (await details_title.inner_text()).strip()

    print("Product details title:", actual_title)

    # Verify the product title
    assert product_name.lower() in actual_title.lower(), (
        f"Product title does not match '{product_name}'. "
        f"Actual title: '{actual_title}'"
    )

    # Get the product price
    price_locator = async_page.locator(
        "span.a-price:not(.a-text-price) span.a-offscreen"
    ).first

    if await price_locator.count() > 0:
        price = (await price_locator.inner_text()).strip()
    else:
        price = "Price not displayed"

    print("Product price:", price)

    # Get the product URL
    product_url = async_page.url

    print("Product URL:", product_url)

    # Validate the product URL
    assert "/dp/" in product_url or "/gp/" in product_url, (
        f"Invalid product details URL: {product_url}"
    )