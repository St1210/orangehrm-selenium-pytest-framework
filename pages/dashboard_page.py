from selenium.webdriver.common.by import By


class DashboardPage:

    HEADER = (
        By.XPATH,
        "//h6[text()='Dashboard']"
    )

    def __init__(self, driver):

        self.driver = driver

    def is_dashboard_displayed(self):

        return self.driver.find_element(
            *self.HEADER
        ).is_displayed()