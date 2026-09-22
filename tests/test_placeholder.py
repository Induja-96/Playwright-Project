def test_get_by_placeholder(page):
    page.goto("https://www.amazon.in/")
    
    page.get_by_placeholder("Search Amazon.in").fill("laptop")
    page.keyboard.press("Enter")
    page.wait_for_timeout(5000)
    
    