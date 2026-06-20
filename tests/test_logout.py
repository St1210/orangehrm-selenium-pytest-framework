from pages.login_page import LoginPage
from pages.menu_page import MenuPage


def test_logout(setup):

    driver = setup

    driver.get(
        "https://opensource-demo.orangehrmlive.com/"
    )

    from pages.dashboard_page import DashboardPage

    LoginPage(driver).login(
    "Admin",
    "admin123"
)

    assert DashboardPage(driver).is_dashboard_displayed()

    MenuPage(driver).logout()