from selenium.webdriver.common.by import By


def test_basket_button_present(browser):
    browser.get("http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/")
    assert browser.find_elements(By.CSS_SELECTOR, "btn.btn-add-to-basket"), 'basket button not found'
