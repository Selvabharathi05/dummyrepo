from playwright.sync_api import Page

class Orders:

    def __init__(self, page:Page):
        self.page = page

    def navigate_to_orders(self):
        self.page.locator("a.account").filter(has_text="@").first.click()
        self.page.get_by_role("link", name = "Orders").nth(1).click()
        