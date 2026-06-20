from pages.login_page import LoginPage
from pages.dashboard_page import DashboardPage


def test_dashboard(setup):

    driver = setup

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )

    LoginPage(driver).login(
        "Admin",
        "admin123"
    )

    dashboard = DashboardPage(driver)

    assert dashboard.is_dashboard_displayed()