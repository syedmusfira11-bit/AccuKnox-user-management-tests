from playwright.sync_api import Page

class AdminPage:
    def __init__(self, page: Page):
        self.page = page
        self.admin_tab = page.locator("span:has-text('Admin')")
        self.add_button = page.locator("button:has-text('Add')")
        self.search_input = page.locator("input[placeholder='Username']")
        self.search_button = page.locator("button:has-text('Search')")
        self.edit_icon = page.locator("i.bi-pencil-fill")  # Update if locator differs
        self.delete_icon = page.locator("i.bi-trash")
        self.confirm_delete = page.locator("button:has-text('Yes, Delete')")

    def go_to_admin_module(self):
        self.admin_tab.click()

    def click_add_user(self):
        self.add_button.click()

    def search_user(self, username: str):
        self.search_input.fill(username)
        self.search_button.click()

    def edit_user(self):
        self.edit_icon.first.click()

    def delete_user(self):
        self.delete_icon.first.click()
        self.confirm_delete.click()
