
import pytest
from pathlib import Path
from playwright.async_api import async_playwright, expect


SCREENSHOT_DIR = Path("screenshots")


async def save_screenshot(page, name):
    SCREENSHOT_DIR.mkdir(exist_ok=True)
    await page.screenshot(
        path=str(SCREENSHOT_DIR / name),
        full_page=True
    )


@pytest.mark.asyncio
async def test_product_search_and_cart(async_page):

    try:
        await async_page.goto("https://www.amazon.in/")

        search_box = async_page.locator("#twotabsearchtextbox")
        await search_box.fill("iPhone 16")
        await search_box.press("Enter")

        product = async_page.locator(
            "div[data-component-type='s-search-result']"
        ).first

        await expect(product).to_be_visible()

        product_title = await product.locator("h2 a").inner_text()
        print("Selected product:", product_title)

        await product.locator("h2 a").click()
        await async_page.wait_for_load_state("domcontentloaded")

        add_to_cart = async_page.locator("#add-to-cart-button")

        if not await add_to_cart.is_visible():
            await save_screenshot(async_page, "product_unavailable.png")
            pytest.skip(
                "Add to Cart is missing. Cart validation skipped."
            )

        if not await add_to_cart.is_enabled():
            await save_screenshot(async_page, "product_unavailable.png")
            pytest.skip(
                "Add to Cart is disabled. Cart validation skipped."
            )

        await add_to_cart.click()

        await async_page.goto(
            "https://www.amazon.in/gp/cart/view.html"
        )

        cart_item = async_page.locator(".sc-list-item").first
        await expect(cart_item).to_be_visible()

        print("Product added to cart and cart validation passed.")

    except Exception:
        await save_screenshot(async_page, "product_test_failure.png")
        raise


@pytest.mark.asyncio
async def test_restore_session():

    session_file = Path("demosession.json")

    if not session_file.exists():
        pytest.fail("demosession.json is missing. Run auth.py first." )

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=False)
        context = await browser.new_context(
            storage_state=str(session_file)
        )
        page = await context.new_page()

        try:
            await page.goto("https://demowebshop.tricentis.com/")

            logout_link = page.get_by_text("Log out")

            if await logout_link.is_visible():
                await expect(logout_link).to_be_visible()
                print("Saved session restored successfully.")
            else:
                await save_screenshot(page, "session_expired.png")
                pytest.fail(
                    "Saved session is expired or invalid. "
                    "Run auth.py to sign in again."
                )

        except Exception:
            await save_screenshot(page, "session_test_failure.png")
            raise

        finally:
            await browser.close()
