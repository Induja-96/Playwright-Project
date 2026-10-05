import pytest
from playwright.async_api import expect

# Scenario 1: Product Name to Add to Cart

@pytest.mark.asyncio
async def test_demo(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")
    count = await async_page.locator("//a[@href='/books']").count()
    print(count)
    await async_page.wait_for_timeout(3000)
    await async_page.locator("//div[@class='block block-category-navigation']//a[@href='/books']").click()
    await async_page.wait_for_timeout(3000)
    product= async_page.locator("//a[text()='Computing and Internet']")
    await expect(product).to_be_visible()
    await async_page.wait_for_timeout(5000)
  # Add Computing and Internet to cart
    await async_page.locator(
    "//a[text()='Computing and Internet']/../../..//input[@value='Add to cart']").click()
    await async_page.wait_for_timeout(5000)

    await async_page.locator("//span[text()='Shopping cart']").click()
    await async_page.wait_for_timeout(5000)
    await expect(async_page.locator("//td[@class='product']//a[text()='Computing and Internet']")).to_be_visible()



    # Scenario 3 Select product by price
   
@pytest.mark.asyncio
async def test_price(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    await async_page.locator(
        "//div[@class='block block-category-navigation']//a[@href='/books']"
    ).click()

    # Select first product
    product = async_page.locator("(//div[@class='product-item'])[1]")

    # Get product name
    product_name = await product.locator(
        "xpath=.//h2[@class='product-title']/a"
    ).inner_text()

    print("Product selected:", product_name)

    # Add product to cart
    await product.locator("input[value='Add to cart']").click()

    # Go to shopping cart
    await async_page.locator("//span[text()='Shopping cart']").click()

    # Verify selected product is displayed in cart
    await expect(
        async_page.locator(
            f"//td[@class='product']/a[text()='{product_name}']"
        )
    ).to_be_visible()
    
    
    
    #Scenario 5: DemoWebShop – Product Name and Rating
    
@pytest.mark.asyncio
async def test_rating(async_page):
    await async_page.goto("https://demowebshop.tricentis.com/")

    await async_page.locator(
        "//div[@class='block block-category-navigation']//a[@href='/books']"
    ).click()
    
    # Scenario 7  Multiple Products
def test_get_multiple_product(page):
    page.goto("https://demowebshop.tricentis.com/",wait_until='domcontentloaded')
    page.locator("(//a[contains(text(), 'Books')])[3]").click()
    products_locators = page.locator("//h2[@class='product-title']")

    
    print("num of books =", products_locators.count())  #num of products
    
    print("products list", products_locators.all_inner_texts())
    
    product_list= ["Computing and Internet", "Fiction", "Health Book"]
    for i in product_list:
        product =page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
        product.click()                       
            

    