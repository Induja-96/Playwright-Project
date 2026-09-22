from playwright.sync_api import expect
def test_get_by_alt_text(page):
    page.goto("https://demowebshop.tricentis.com/")
    # logo = page.get_by_alt_text("Tricentis Demo Web Shop")
    # expect(logo).to_be_visible()
    
    logo = page.get_by_alt_text("Speed | Tricentis")
    logo.click()
    page.close() 