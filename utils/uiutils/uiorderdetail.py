from playwright.sync_api import Page

class OrderDetail:

    def __init__(self, page:Page):
        self.page = page
    
    def navigate_to_orderdetails(self,orderId):
        # onclick="setLocation('/orderdetails/2183605')"
        self.page.locator(f'input[onclick*="/orderdetails/{orderId}"]').click()
        self.page.wait_for_selector("table.data-table")
