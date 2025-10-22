from pages.login_page import LoginPage

def test_login(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login_page = LoginPage(page)
    login_page.login("Admin", "admin123")
    assert page.locator("span:has-text('Admin')").is_visible()
