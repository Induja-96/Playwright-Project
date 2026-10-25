
import pytest
from playwright.async_api import async_playwright, expect

BASE_URL = "http://localhost:3000/"


@pytest.mark.asyncio
async def test_product_data_validation(async_page):

    async with async_playwright() as playwright:
        api = await playwright.request.new_context(
            base_url=BASE_URL,
            extra_http_headers={"Accept": "application/json"},
            timeout=5000
        )

        # Get product data from mock API
        endpoint = "products/1"
        resp = await api.get(endpoint)

        assert resp.status == 200

        resp_json = await resp.json()
        api_title = resp_json["title"]

        print("API endpoint:", BASE_URL + endpoint)
        print("API field: title")
        print("API title:", api_title)

        # Open Amazon
        await async_page.goto("https://www.amazon.in")

        await async_page.locator(
            "#twotabsearchtextbox"
        ).fill(api_title)

        await async_page.locator(
            "#twotabsearchtextbox"
        ).press("Enter")

        product = async_page.locator(
            "div[data-component-type='s-search-result']"
        ).first

        await expect(product).to_be_visible()

        ui_title = await product.locator("h2 a span").inner_text()

        # Normalize whitespace and case
        api_title = " ".join(api_title.split()).lower()
        ui_title = " ".join(ui_title.split()).lower()

        print("UI field: product search result title")
        print("UI title:", ui_title)

        # Compare API and UI values
        assert api_title in ui_title or ui_title in api_title, (
            f"Product title mismatch | "
            f"Endpoint: {BASE_URL + endpoint} | "
            f"API field: title | "
            f"UI field: product search result title | "
            f"API value: '{api_title}' | "
            f"UI value: '{ui_title}'"
        )

        print("Product title matched successfully")

        await api.dispose()
