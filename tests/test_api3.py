import pytest
from _testcapi import awaitType
from playwright.async_api import async_playwright
BASE_URL = "http://localhost:3001/"
@pytest.mark.asyncio
async def test_api_post_on_comment():
        async with async_playwright() as playwright:
            api = await playwright.request.new_context(
                base_url=BASE_URL,
                extra_http_headers={"Accept": "application/json"},
                timeout=5000
            )
            resp = await api.post("posts",data={
            "title": "NoteBOOK",
            "views": 300
            })
            resp_json = await resp.json()
            res_id = resp_json["id"]
            #============================ post commet
            resp_com = await api.post("comments",data={
                "text": "demo",
                "postId": res_id
                })
            print(await resp.json())