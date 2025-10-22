from pages.login_page import LoginPage
from pages.admin_page import AdminPage
from pages.add_user_page import AddUserPage

def test_add_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(page)
    admin = AdminPage(page)
    add_user = AddUserPage(page)

    login.login("Admin", "admin123")
    admin.go_to_admin_module()
    admin.click_add_user()
    add_user.add_user("ESS", "Linda Anderson", "testuser123", "Enabled", "Test@123")

    page.wait_for_selector("text=Successfully Saved")
    assert page.locator("text=Successfully Saved").is_visible()
