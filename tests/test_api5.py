import pytest
from _testcapi import awaitType
from playwright.async_api import async_playwright
BASE_URL = "http://localhost:3001/"
# @pytest.mark.asyncio
# async def test_api_patch():
#         async with async_playwright() as playwright:
#             api = await playwright.request.new_context(
#                 base_url=BASE_URL,
#                 extra_http_headers={"Accept": "application/json"},
#                 timeout=5000
#             )
#             await api.delete("posts/1")

#             res =  await api.get("posts/1")
#             assert  res.status >= 400
#             print(await res.json())
            
@pytest.mark.asyncio
async def test_api_patch(api):

            await api.delete("comments/1")

            res =  await api.get("comments/1")
            assert  res.status >= 400
            print(await res.json())           