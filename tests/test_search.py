from selenium import webdriver
from selenium.webdriver.common.by import By

search = "//input[@name='search']"
submit = "//button[@class='btn btn-default btn-lg']"
product = "//a[href(@contains(\"product_id = 47\"))]"
link = "HP LP3065"
check_message = "//*[@id=\"content\"]/p[2]"
expected_text = "There is no product that matches the search criteria."

def test_search_for_a_valid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, search).send_keys("HP")
    driver.find_element(By.XPATH, submit).click()
    # assert driver.find_element(By.XPATH, product).is_displayed()
    assert driver.find_element(By.LINK_TEXT, link).is_displayed()
    driver.quit()


def test_search_for_invalid_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, search).send_keys("Honda")
    driver.find_element(By.XPATH, submit).click()
    text = driver.find_element(By.XPATH, check_message).text
    assert text.__eq__(expected_text)
    driver.quit()


def test_search_for_no_product():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://tutorialsninja.com/demo/")
    driver.find_element(By.XPATH, search).send_keys("")
    driver.find_element(By.XPATH, submit).click()
    assert driver.find_element(By.XPATH, check_message).text.__eq__(expected_text)
    driver.quit()

