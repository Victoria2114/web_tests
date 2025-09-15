
from pages.login_page import LoginPage

def test_login(browser):
    page = LoginPage(browser)
    page.open("https://the-internet.herokuapp.com/login")

    page.login("tomsmith", "SuperSecretPassword!")
    
    assert "secure" in browser.current_url
  