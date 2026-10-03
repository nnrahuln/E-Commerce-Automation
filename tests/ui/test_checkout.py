from playwright.sync_api import Page, expect

from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


def test_complete_checkout(page: Page):
    login_page = LoginPage(page)
    login_page.open()
    login_page.login("standard_user", "secret_sauce")

    products_page = ProductsPage(page)
    products_page.add_backpack_to_cart()
    products_page.open_cart()

    cart_page = CartPage(page)
    cart_page.checkout()

    checkout_page = CheckoutPage(page)

    checkout_page.enter_customer_details(
        "Rahul",
        "NN",
        "571401"
    )

    checkout_page.continue_checkout()
    checkout_page.finish_order()

    expect(checkout_page.complete_message).to_have_text(
        "Thank you for your order!"
    )