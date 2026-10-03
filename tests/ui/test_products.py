from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage


def test_add_product_to_cart(page: Page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)

    expect(products_page.products_title).to_have_text("Products")

    products_page.add_backpack_to_cart()

    expect(products_page.cart).to_contain_text("1")