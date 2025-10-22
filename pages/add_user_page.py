from playwright.sync_api import Page

class AddUserPage:
    def __init__(self, page: Page):
        self.page = page
        self.user_role_dropdown = page.locator("//label[text()='User Role']/../following-sibling::div//i")
        self.employee_name_input = page.locator("input[placeholder='Type for hints...']")
        self.username_input = page.locator("//label[text()='Username']/../following-sibling::div/input")
        self.status_dropdown = page.locator("//label[text()='Status']/../following-sibling::div//i")
        self.password_input = page.locator("input[type='password']").nth(0)
        self.confirm_password_input = page.locator("input[type='password']").nth(1)
        self.save_button = page.locator("button:has-text('Save')")

    def add_user(self, role, employee_name, username, status, password):
        self.user_role_dropdown.click()
        self.page.locator(f"//span[text()='{role}']").click()
        self.employee_name_input.fill(employee_name)
        self.page.wait_for_timeout(1000)
        self.page.keyboard.press("ArrowDown")
        self.page.keyboard.press("Enter")
        self.username_input.fill(username)
        self.status_dropdown.click()
        self.page.locator(f"//span[text()='{status}']").click()
        self.password_input.fill(password)
        self.confirm_password_input.fill(password)
        self.save_button.click()
