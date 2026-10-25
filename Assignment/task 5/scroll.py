
import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_search_result_pagination(async_page):

    await async_page.goto("https://www.amazon.in")

    # Search for a product
    await async_page.locator("#twotabsearchtextbox").fill("iPhone 16")
    await async_page.locator("#twotabsearchtextbox").press("Enter")

    products = async_page.locator(
        "div[data-component-type='s-search-result']"
    )

    await expect(products.first).to_be_visible()

    first_product = await products.first.inner_text()
    print("First product before navigation:", first_product)

    # Check pagination
    next_page = async_page.locator("a.s-pagination-next")

    # Check Load More control
    load_more = async_page.get_by_text("Load more", exact=True)

    # Check infinite scroll by scrolling down
    await async_page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    await async_page.wait_for_timeout(3000)

    new_count = await products.count()
    print("Product count after scrolling:", new_count)

    if await next_page.is_visible() and await next_page.is_enabled():

        print("Behavior: Pagination")

        await next_page.click()
        await expect(products.first).to_be_visible()

        second_product = await products.first.inner_text()
        print("First product on next page:", second_product)

        assert first_product != second_product, (
            "Product results did not change after pagination"
        )

    elif await load_more.is_visible():

        print("Behavior: Load More control")

        old_count = await products.count()
        await load_more.click()

        await expect(products).not_to_have_count(old_count)

        print("New products loaded successfully")

    elif new_count > 0:

        print("Behavior: Scrolling checked")
        print("Product count before scrolling and after scrolling:",
              new_count)

    else:
        print("No pagination or Load More control detected")
