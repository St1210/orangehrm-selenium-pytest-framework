from requests import options
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager    

class DriverFactory:
    @staticmethod
    def getDriver():
        options = webdriver.ChromeOptions()
        options.add_argument("--headless")  # Run in headless mode
        options.add_experimental_option("excludeSwitches", ["enable-automation"])  # Suppress logging
        options.add_experimental_option("prefs",{"credentials_enable_service": False,
        "profile.password_manager_enabled": False,
        "autofill.profile_enabled": False,
        "autofill.credit_card_enabled": False})
        
        driver = webdriver.Chrome(service = Service(ChromeDriverManager().install()), 
        options=options)
        driver.implicitly_wait(10)  # Set implicit wait time
        return driver