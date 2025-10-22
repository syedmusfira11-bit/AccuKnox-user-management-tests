from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_delete_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(page)
    admin = AdminPage(page)

    login.login("Admin", "admin123")
    admin.go_to_admin_module()
    admin.search_user("testuser123")
    admin.delete_user()

    page.wait_for_selector("text=Successfully Deleted")
    assert page.locator("text=Successfully Deleted").is_visible()
