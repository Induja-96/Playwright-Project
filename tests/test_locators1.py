def test_count_the_link(page):
    page.goto("https://www.amazon.in/",wait_until="domcontentloaded")
    links_locator = page.locator("//a")
    links_locator.first.wait_for(state="attached")
    links=links_locator.all()
    print(len(links))
    print(type(links))
    for i in links:
        print(i.text_content(),flush=True)
    print("*" * 50)
    for i in links:
        print(i.get_attribute("href"),flush =True)
             
    #link tag_name a / link is present in href attribute of a tag
    #finding the element use //a: a tag
    # get the link use attribute href
    #get the link of text use: text method
    #link - //a
    #img - //img
    #table - //table
    #rows- //tr
    #column- //td
    #list - //ol or //ul
    #list item - //li
    # find single element -> single ele
    # find multiple element -> multiple ele in the list
    
# def test_table(page):
#     page.goto("https://www.w3schools.com/html/html_tables.asp")
#     count_tables = page.locator("//table").count()
#     print(count_tables,flush=True)