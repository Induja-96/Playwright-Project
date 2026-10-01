import pytest
@pytest.mark.asyncio
#async def test_dropdown(async_page):
    #await async_page.goto("https://www.amazon.in/")
    #drop_down =  async_page.locator("#searchDropdownBox")
    # #select by index
    # await drop_down.select_option(index=5)
    # #select by value
    # await drop_down.select_option(value="search-alias=appliances")
    # #select by label
    # await drop_down.select_option(label = "Amazon Devices")
    #search_box= async_page.locator("#twotabsearchtextbox")

    #await search_box.fill("books")
    #need to get dynamic or auto suggession dropdown
    #suggestions = async_page.locator("//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
    
    # wait all suggestions
     #await suggestions.first.wait_for()
    
    #print num of options
    
    
    # count = await suggestions.count()
    # print("total num of options = ", count)
    
    # #print all options with index
    # for i in range(count):
    #     text = await suggestions.nth(i).inner_text()
    #     print(f"{i} : {text}")
     
    # await async_page.get_by_text(" 2 + year old").click()
    # await async_page.wait_for_timeout(20000)
    
# @pytest.mark.asyncio
# async def test_drop_downs_select_with_keyboard(async_page):
#         await async_page.goto("https://www.amazon.in/")
#         search_box= async_page.locator("#twotabsearchtextbox")
        
#         await search_box.fill("books")
#         await async_page.wait_for_timeout(3000)
        
#         await search_box.press("ArrowDown")
#         await search_box.press("ArrowDown")
#         await search_box.press("ArrowDown")
#         await search_box.press("Enter")
#         await async_page.wait_for_timeout(2000)
@pytest.mark.asyncio
async def test_drop_downs_select_with_keyboard(async_page):
        await async_page.goto("https://www.amazon.in/")
        
        search_box= async_page.locator("#twotabsearchtextbox")
        
        await search_box.fill("books")
        suggestions = async_page.locator("//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
        count = await suggestions.count()
        
        #wait all suggestions
        await suggestions.first.wait_for()
        options = await suggestions.all_inner_texts()
        options.sort(key=str.lower)
        print(len(options))
     
        # need to get 3rd option
        expected_text = options[3]
      
        for i in range(count):
            if suggestions.nth(i).inner_text() == expected_text:
                suggestions.nth(i).click()
        act = await search_box.input_value()
        assert act.lower() == expected_text.lower()
        
        # #print no of o[ption
        # count = await suggestions.count()
        # print("total num of options= ", count)
        #  #get all options in the list
        # options = []
        # for i in range(count):
        #     text = (await suggestions.nth(i).inner_text()).strip()
        #     if text: #bool(text): is null then it returns false, if it contain text, it result True
        #         options.append(text)
        # print(options)
        # sorted_options= options.sort()
        
        # print(sorted_options)        
        
        # # #select 3 options
        
        # await search_box.fill("books")
        # await suggestions.first.wait_for()
        # suggestions = async_page.locator("//div[@class='s-suggestion s-suggestion-ellipsis-direction']")
                
        