def test_get_options(page):
    page.goto("https://demowebshop.tricentis.com/",wait_until='domcontentloaded')
    page.locator("(//a[contains(text(), 'Books')])[3]").click()
    products_locators = page.locator("//h2[@class='product-title']")

    
    print("num of books =", products_locators.count())  #num of products
    
    print("products list", products_locators.all_inner_texts())
    
    product_list= ["Computing and Internet", "Fiction", "Health Book"]
    for i in product_list:
        product =page.locator(f"//a[text()='{i}']/../..//input[@value='Add to cart']")
        product.click()                       
            