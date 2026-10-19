from playwright.async_api import async_playwright
import pytest_asyncio

# @pytest_asyncio.fixture
# async def async_page():
#     async with async_playwright() as p:
#         browser =  await p.chromium.launch(headless = False)
#         page = await browser.new_page()
#         yield page
#         await browser.close()
        
@pytest_asyncio.fixture
async def api():
    async with async_playwright() as playwright:
        BASE_URL = "http://localhost:3001/"
        api = await playwright.request.new_context(
            base_url=BASE_URL,
            extra_http_headers={"Accept": "application/json"},
            timeout=5000
        )
        yield api
        await api.dispose()       