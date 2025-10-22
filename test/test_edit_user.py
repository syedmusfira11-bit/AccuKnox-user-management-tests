from pages.login_page import LoginPage
from pages.admin_page import AdminPage

def test_edit_user(page):
    page.goto("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    login = LoginPage(page)
    admin = AdminPage(page)

    login.login("Admin", "admin123")
    admin.go_to_admin_module()
    admin.search_user("testuser123")
    admin.edit_user()

    page.locator("//label[text()='Status']/../following-sibling::div//i").click()
    page.locator("//span[text()='Disabled']").click()
    page.locator("button:has-text('Save')").click()

    page.wait_for_selector("text=Successfully Updated")
    assert page.locator("text=Successfully Updated").is_visible()
