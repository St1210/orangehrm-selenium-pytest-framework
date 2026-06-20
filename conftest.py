import pytest 
from pages.login_page import LoginPage
from utilities.driver_factory import DriverFactory

@pytest.fixture
def setup():
    driver = DriverFactory.getDriver()
    yield driver
    driver.quit()

@pytest.fixture
def logged_in_user(setup):
    driver = setup
    
    driver.get("https://opensource-demo.orangehrmlive.com/")
    LoginPage(driver).login("Admin", "admin123")
    return driver

