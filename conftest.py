import os
import pytest

from pages.login_page import LoginPage
from utils.config import USERNAME, PASSWORD


@pytest.fixture
def logged_in_page(page):
    login_page = LoginPage(page)

    login_page.open()
    login_page.login(USERNAME, PASSWORD)

    return page


@pytest.hookimpl(hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    report = outcome.get_result()

    if report.when == "call" and report.failed:
        page = item.funcargs.get("page")

        if page:
            os.makedirs("screenshots", exist_ok=True)

            screenshot_path = (
                f"screenshots/{item.name}_failed.png"
            )

            page.screenshot(
                path=screenshot_path,
                full_page=True
            )