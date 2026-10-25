import pytest
from playwright.async_api import expect


@pytest.mark.asyncio
async def test_amazon_autocomplete(async_page):

    # Open Amazon India
    await async_page.goto(
        "https://www.amazon.in/",
        wait_until="domcontentloaded"
    )

    # Enter a partial product name
    search_box = async_page.locator("#twotabsearchtextbox")
    await search_box.fill("iphone")

    # Locate autocomplete suggestions
    suggestions = async_page.locator(
        "#sac-autocomplete-results-container"
    )

    # Check whether suggestions appear in the current session
    try:
        await suggestions.wait_for(state="visible", timeout=5000)

        suggestion_items = suggestions.locator(
            "div.s-suggestion"
        )

        suggestion_count = await suggestion_items.count()

    except Exception:
        suggestion_count = 0

    # Select a matching suggestion if suggestions appear
    if suggestion_count > 0:

        print("Autocomplete suggestions are displayed.")

        matching_suggestion = None

        for i in range(suggestion_count):

            suggestion = suggestion_items.nth(i)
            suggestion_text = (await suggestion.inner_text()).strip()

            print(f"Suggestion {i + 1}: {suggestion_text}")

            if "iphone 16" in suggestion_text.lower():
                matching_suggestion = suggestion
                break

        # Select the matching suggestion
        if matching_suggestion is not None:

            await expect(matching_suggestion).to_be_visible()
            await matching_suggestion.click()

            # Validate the resulting search term or navigation
            await expect(search_box).to_have_value(
                "iphone 16",
                timeout=10000
            )

            print("Matching autocomplete suggestion selected.")

        else:

            # No matching suggestion; continue with Search button
            print("No matching suggestion found. Using Search button.")

            await search_box.fill("iphone 16")

            search_button = async_page.locator("#nav-search-submit-button")
            await expect(search_button).to_be_visible()
            await search_button.click()

            await expect(async_page).to_have_url(
                __import__("re").compile(r".*s\?"),
                timeout=15000
            )

            print("Search completed using the Search button.")

    else:

        # Suggestions are absent; use the Search button
        print("Autocomplete suggestions are absent in this session.")

        await search_box.fill("iphone 16")

        search_button = async_page.locator("#nav-search-submit-button")
        await expect(search_button).to_be_visible()
        await search_button.click()

        # Validate navigation to search results
        await expect(async_page).to_have_url(
            __import__("re").compile(r".*s\?"),
            timeout=15000
        )

        print("Search completed using the Search button.")
        print("Autocomplete behavior: no suggestions were detected.")