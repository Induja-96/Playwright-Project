import pytest
from playwright.async_api import async_playwright

BASE_URL = "http://localhost:3001/"
# @pytest.mark.asyncio
# async def test_api():
#     async with async_playwright() as playwright:
#         api = await playwright.request.new_context(
#             base_url=BASE_URL,
#             extra_http_headers={"Accept": "application/json"},
#             timeout=5000
#         )
#         #http://localhost:3000/posts
#         resp =  await api.get("posts")
#         assert resp.status == 200 
#         print(await resp.text())
#         print("*" * 30)
#         print(await resp.json())




@pytest.mark.asyncio
async def test_api_post():
        async with async_playwright() as playwright:
            api = await playwright.request.new_context(
                base_url=BASE_URL,
                extra_http_headers={"Accept": "application/json"},
                timeout=5000
            )
            resp = await api.post("posts",
                           data={
                                "title": "Java",
                                "views": 200
                                })

            assert resp.status == 201
            print(await resp.json())
            print(await resp.text())
