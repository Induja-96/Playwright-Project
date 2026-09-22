from playwright.sync_api import expect, sync_playwright
def test_google(page,browser_name):
    
     page.goto("https://www.google.com/")
     print(page.title())
     print(browser_name)
     expect(page).to_have_title("Google")
  