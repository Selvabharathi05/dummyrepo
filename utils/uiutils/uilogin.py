from playwright.sync_api import Page
class UILogin:

    def __init__(self, page:Page):
        self.page = page

    def loginto(self,credential):
        email = credential['email']
        password = credential['password']
        self.page.goto("https://demowebshop.tricentis.com/")
        self.page.get_by_role("link", name = "Log in").click()
        self.page.get_by_label("Email").fill(email)
        self.page.get_by_label("Password").fill(password)
        self.page.get_by_role("button", name = "Log in").click()