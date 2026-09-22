from playwright.sync_api import expect

# def test_locators_get_by_role(page):
#     page.goto("https://demowebshop.tricentis.com/")
#     page.get_by_role("link",name="Log in").click()
#     page.get_by_role("textbox",name="Email").fill("abc@gmail.com")
#     page.get_by_role("textbox",name='Password').fill("abc123")
#     page.get_by_role("button",name="Log in").click()
    
# def get_by_text(page):
#     page.goto("https://www.facebook.com/")
#     login_to_facebook_text = page.get_by_text("Log in to Facebook")  
#     expect(login_to_facebook_text).to_be_visible()
#     forgot_password_button = page.get_by_text("Forgotten password?")
#     forgot_password_button.click()
    
def test_get_by_label(page):
    page.goto("https://demowebshop.tricentis.com/")
    register_link = page.get_by_text("Register")
    register_link.click()
    page.get_by_role("radio",name="Female").check()
    page.get_by_label("First name:").fill("abc")
    page.get_by_label("Last name:").fill("xyz")
    page.get_by_label("Email:").fill("abc123@gmail.com")
    page.get_by_label("Password:").nth(0).fill("abc123")  #password is a common label for pasword and confirm password
    page.get_by_label("Confirm password:").fill("abc123")
    page.get_by_role("button",name="Register").click()