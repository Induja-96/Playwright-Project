import pytest
from playwright.async_api import expect

# @pytest.mark.asyncio
# async def test_dropdown(async_page):
#   await async_page.goto("https://testautomationpractice.blogspot.com/")
#   dropdown = async_page.locator("#country")
#   await async_page.wait_for_timeout(2000)
#  # await dropdown.select_option(label = "India")
#   await dropdown.select_option(value="india")
  
#     # Count the options
#   count = await dropdown.count()
#   print("total num of options = ", count)
    
#     #print all options with index
#   for i in range(count):
#         text = await dropdown.nth(i).inner_text()
#         print(f"{i} : {text}")
    
#    # 1. Verify that the selected option is correct
#   await expect(dropdown).to_have_value("india")
#   print("Verified: India is selected")   
  
  
################################################
  #dynamic dropdown   
################################################

@pytest.mark.asyncio
async def test_dropdown(async_page):
    await async_page.goto("https://www.amazon.in/")
    search_box= async_page.locator("#twotabsearchtextbox")
    drop_down =  async_page.locator("#twotabsearchtextbox")
    await search_box.fill("iphone")

    # 2. Wait for suggestions to appear
    suggestions = async_page.locator( "div.s-suggestion-container div.s-suggestion")
    await expect(suggestions.first).to_be_visible()

    # 3. Print all suggestions
    count = await suggestions.count()
    print("Total suggestions:", count)

    for i in range(count):
        text = await suggestions.nth(i).inner_text()
        print(f"{i}: {text}")
     
    suggestion = suggestions.get_by_text( " 18 pro", exact=True)

    await expect(suggestion).to_be_visible()
    await suggestion.click()    