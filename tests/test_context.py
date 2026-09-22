from playwright.sync_api import expect, sync_playwright
def test_application():
    with sync_playwright() as p:
        browser= p.chromium.launch(headless=False)
        end_user_context = browser.new_context() # create a new browser context
        end_user_page = end_user_context.new_page()
        end_user_page.goto("https://agents.akbartravelsonline.com/b2bplus/login")
        #expect(act).to_have_title(exp)
        expect(end_user_page).to_have_title("Cheap Flights ; Domestic ; International Flight Offers in India") 
        admin_context=browser.new_context()
        admin_page = admin_context.new_page()
        admin_page.goto("https://aebetab2badmin.akbartravels.com/")
        expect(admin_page).to_have_title(".:: Admin Login ::.")
        