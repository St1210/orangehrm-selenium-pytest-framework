from pages.login_page import LoginPage

def test_Login_valid_credentials(setup):
    driver = setup

    driver.get("https://opensource-demo.orangehrmlive.com/")

    login_page = LoginPage(driver)
    login_page.login("Admin" , "admin123")

    assert "dashboard" in driver.current_url

    