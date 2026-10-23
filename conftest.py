# from playwright.async_api import async_playwright
# import pytest_asyncio

# # @pytest_asyncio.fixture
# # async def async_page():
# #     async with async_playwright() as p:
# #         browser =  await p.chromium.launch(headless = False)
# #         page = await browser.new_page()
# #         yield page
# #         await browser.close()
        
# @pytest_asyncio.fixture
# async def api():
#     async with async_playwright() as playwright:
#         BASE_URL = "http://localhost:3001/"
#         api = await playwright.request.new_context(
#             base_url=BASE_URL,
#             extra_http_headers={"Accept": "application/json"},
#             timeout=5000
#         )
#         yield api
#         await api.dispose()    
          
        
# @pytest_asyncio.fixture
# async def api():
#     async with async_playwright() as playwright:
        
#         api = await playwright.request.new_context(
#             base_url=("https://parabank.parasoft.com/" 
#                       "parabank/services/bank/"),
#             extra_http_headers={"Accept": "application/json"},
#             # token="", github
#             timeout=5000
#         )
#         print("api fixture is stated")
#         yield api
#         await api.dispose()
#         print("api fixture is closed")       
        
# @pytest_asyncio.fixture
# async def api_git():
#     async with async_playwright() as playwright:
#         api = await playwright.request.new_context(
#             base_url=("https://api.github.com"),
#             # extra_http_headers={
#             #     "Accept": "application/vnd.github+json"},
#             # # token="", github
#             # timeout=5000
#         )
#         print("api fixture is stated")
#         yield api
#         await api.dispose()
#         print("api fixture is closed")         
         
         
         
         
         

import os
import pytest_asyncio
from dotenv import load_dotenv
from playwright.async_api import async_playwright

load_dotenv()


@pytest_asyncio.fixture
async def api():
    async with async_playwright() as playwright:

        api = await playwright.request.new_context(
            base_url=(
                "https://parabank.parasoft.com/"
                "parabank/services/bank/"
            ),
            extra_http_headers={
                "Accept": "application/json"
            },
            timeout=5000
        )

        print("api fixture is started")
        yield api

        await api.dispose()
        print("api fixture is closed")


@pytest_asyncio.fixture
async def api_git():
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise RuntimeError(
            "GITHUB_TOKEN is missing. Check your .env file."
        )

    async with async_playwright() as playwright:
        api = await playwright.request.new_context(
            base_url="https://api.github.com",
            extra_http_headers={
                "Authorization": f"Bearer {token}",
                "Accept": "application/vnd.github+json"
            },
            timeout=5000
        )

        print("api_git fixture is started")
        yield api

        await api.dispose()
        print("api_git fixture is closed")
         