
from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class ProfilePage(BasePage):
    HEADER = (By.TAG_NAME, "h2")  # например, <h2>Secure Area</h2>
    LOGOUT_BUTTON = (By.CSS_SELECTOR, "a.button.secondary.radius")

    def get_header_text(self):
        return self.driver.find_element(*self.HEADER).text

    def logout(self):
        self.driver.find_element(*self.LOGOUT_BUTTON).click()
