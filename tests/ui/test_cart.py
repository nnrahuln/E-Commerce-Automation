from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage


def test_product_in_cart(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(page)

    expect(cart_page.cart_item).to_be_visible()