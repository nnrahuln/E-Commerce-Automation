from playwright.sync_api import Page


class CartPage:

    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator(".cart_item")
        self.checkout_button = page.locator("#checkout")

    def verify_product_in_cart(self):
        return self.cart_item.is_visible()

    def checkout(self):
        self.checkout_button.click()