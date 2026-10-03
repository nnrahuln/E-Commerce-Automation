from pytest_bdd import given, when, then, scenarios, parsers
from playwright.sync_api import expect

from pages.login_page import LoginPage


scenarios("../features/login.feature")


@given("I open the SauceDemo website")
def open_saucedemo(page):
    login_page = LoginPage(page)
    login_page.open()


@when(
    parsers.parse(
        'I login with username "{username}" and password "{password}"'
    )
)
def login_with_credentials(page, username, password):
    login_page = LoginPage(page)
    login_page.login(username, password)


@then(
    parsers.parse(
        'I should see the login result "{result}"'
    )
)
def verify_login_result(page, result):
    if result == "success":
        expect(page.locator(".title")).to_have_text("Products")

    elif result == "locked":
        expect(page.locator("[data-test='error']")).to_contain_text(
            "locked out"
        )