from playwright.sync_api import Page


class ProductsPage:

    def __init__(self, page: Page):
        self.page = page
        self.products_title = page.locator(".title")
        self.backpack = page.locator("#add-to-cart-sauce-labs-backpack")
        self.cart = page.locator(".shopping_cart_link")

    def add_backpack_to_cart(self):
        self.backpack.click()

    def open_cart(self):
        self.cart.click()