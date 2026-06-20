from pages.login_page import LoginPage


def test_invalid_login(setup):

    driver = setup

    driver.get("https://opensource-demo.orangehrmlive.com/")

    login = LoginPage(driver)

    login.login("Admin", "wrongpassword")

    error = login.get_error_message()

    assert error == "Invalid credentials"