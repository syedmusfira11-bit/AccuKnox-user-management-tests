from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_search_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(page)
    admin = AdminPage(page)

    login.login("Admin", "admin123")
    admin.go_to_admin_module()
    admin.search_user("testuser123")

    assert page.locator("div:has-text('testuser123')").first.is_visible()
