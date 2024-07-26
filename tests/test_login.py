from selenium import webdriver
from selenium.webdriver.common.by import By

account_dropdown = "//*[@id=\"top-links\"]/ul/li[2]/a"
email = "sourodip.ghosh02@gmail.com"
password = "12345"
login = "//input[@value='login']"
message = "Edit your account information"

def login_with_valid_creds(email, password):
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, account_dropdown).click()
    driver.find_element(By.LINK_TEXT, "Login").click()
    driver.find_element(By.ID, "input-email").send_keys(email)
    driver.find_element(By.ID, "input-password").send_keys(password)
    driver.find_element(By.XPATH, login).click()
    assert driver.find_element(By.LINK_TEXT, message).is_displayed()
    driver.quit()

