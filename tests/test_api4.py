import pytest
from _testcapi import awaitType
from playwright.async_api import async_playwright
BASE_URL = "http://localhost:3001/"
@pytest.mark.asyncio
async def test_api_patch():
        async with async_playwright() as playwright:
            api = await playwright.request.new_context(
                base_url=BASE_URL,
                extra_http_headers={"Accept": "application/json"},
                timeout=5000
            )
            await api.patch("posts/1",data={
                "views": 700
            })

@pytest.mark.asyncio
async def test_api_put():
        async with async_playwright() as playwright:
            api = await playwright.request.new_context(
                base_url=BASE_URL,
                extra_http_headers={"Accept": "application/json"},
                timeout=5000
            )
            await api.put("posts/1",data={
                "views": 500,
                "title" : "THE Boss"
            })          