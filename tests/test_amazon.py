import pytest
from playwright.async_api import expect

# @pytest.mark.asyncio
# async def test_heading(async_page):
#     await async_page.goto("https://www.amazon.in/")
#     await async_page.wait_for_timeout(5000)
#     all = await async_page.locator('//i[@class="hm-icon nav-sprite"]').click()
    # headings = ['Trending', 'Digital Content and Devices', 'Shop by Category', 'Programs & Features','Help & Settings']
    # for i in headings:
    #     heading_navigation = async_page.locator(f"//section[@aria-labelledby='{i}']//div[@class='hmenu-item hmenu-title ']")
    #     heading_navigation.click()
    
    # headings = async_page.locator(
    #     '//div[contains(@class,"hmenu-item") and contains(@class,"hmenu-title")]'
    # )

    # count = await headings.count()
    # print("Count =", count)
    # for i in range(count):
    #   heading_name = await headings.nth(i).inner_text()
    #   print(heading_name.strip())
    
    
    
      
    #   Scenario 4: Amazon – Product Name and Price
      
# @pytest.mark.asyncio
# async def test_selection(async_page):
#         await async_page.goto("https://www.amazon.in/")
        
#         search_box= async_page.locator("#twotabsearchtextbox")
        
#         await search_box.fill("phone")
#         await async_page.wait_for_timeout(5000)
#         suggestions = async_page.locator("(//span[@class='s-heavy'])[1]")
#         await suggestions.click()
        
#         product = async_page.locator("//span[text()='iPhone 16 128 GB: 5G Mobile Phone with Camera Control, A18 Chip and a Big Boost in Battery Life. Works with AirPods; White']")
#         name = await product.inner_text()
#         price = await async_page.locator("//span[text()='86,900']").inner_text()
    
#         print("Product Name:", name)
#         print("Price:", price)



#Scenario 6: Amazon – Search Results
@pytest.mark.asyncio
async def test_selection(async_page):
        await async_page.goto("https://www.amazon.in/")
        
        search_box= async_page.locator("#twotabsearchtextbox")
        
        await search_box.fill("book")
        await async_page.wait_for_timeout(5000)
        suggestions = async_page.locator('(//div[@class="s-suggestion s-suggestion-ellipsis-direction"])[2]')
        await suggestions.click()
        book = async_page.locator("(//h2[@class='a-size-medium a-spacing-none a-color-base a-text-normal'])[1]")
        name = await book.inner_text()
        print("Product Name:", name)
        async_page.locator("(//input[@name='submit.addToCart'])[1]")
        