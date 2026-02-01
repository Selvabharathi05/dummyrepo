from playwright.sync_api import Page

class ValidateOrder:

    def __init__(self, page:Page):
        self.page = page

    def validate_order(self,products):

        rows = self.page.locator("table.data-table tbody")

        for product in products:
            js_name = product['name']
            js_qty = product['quantity']
            js_price = product['price']
            row = rows.locator("tr", has_text= js_name)

            product_name = row.locator('a').inner_text().strip()
            price = row.locator("td.price").inner_text().strip()
            product_qty = int(row.locator("td.quantity").inner_text())

            # validate

            assert product_name == js_name
            assert price == js_price
            assert js_qty == product_qty
