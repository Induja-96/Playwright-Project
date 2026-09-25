def test_collecting_all_links(page):
    page.goto("https://www.flipkart.com/",wait_until='domcontentloaded')
    links = page.locator("//a")
    for i in links.all():
        print("links", i.get_attribute("href"), flush=True)
    print(links.nth(5).inner_text())
    links.last.click()
    #links.first.click()
    links.nth(0).click()   
     
    