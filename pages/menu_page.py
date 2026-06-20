from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class MenuPage:

    PROFILE_ICON = (
        By.XPATH,
    "//span[@class='oxd-userdropdown-tab']"
)

    LOGOUT = (
        By.XPATH,
        "//a[text()='Logout']"
)

    def __init__(self, driver):

        self.driver = driver

        self.wait = WebDriverWait(driver, 10)

    def logout(self):

        self.wait.until(
        EC.element_to_be_clickable(
            self.PROFILE_ICON
        )
    ).click()

        self.wait.until(
        EC.element_to_be_clickable(
            self.LOGOUT
        )
    ).click()