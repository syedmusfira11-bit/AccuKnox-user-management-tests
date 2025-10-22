from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_validate_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(page)
    admin = AdminPage(page)

    login.login("Admin", "admin123")
    admin.go_to_admin_module()
    admin.search_user("testuser123")

    status = page.locator("//div[text()='Disabled']").is_visible()
    assert status, "Expected status 'Disabled' not found!"
