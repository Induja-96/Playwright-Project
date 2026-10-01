@pytest.mark.asyncio

async def test_action_click_db_(async_page):
    await async_page.goto("https://demo.guru99.com/test/simple_context_menu.html")
    dbc = async_page.locator("//button[text()='Double-Click Me To See Alert']")
    dbc.dblclick()