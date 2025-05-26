from selenium.webdriver.common.by import By
from selenium.webdriver import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_search_qa_guru(browser_setting):
    driver = browser_setting
    driver.get('https://ya.ru/')
    search_input = driver.find_element(By.ID, 'text')
    search_input.send_keys('yashaka/selene')
    search_input.send_keys(Keys.ENTER)
    result_text = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CSS_SELECTOR, '.OrganicTextContentSpan')))

    assert 'Selene’s core strength is its user-oriented API, which abstracts the complexity of working with Selenium WebDriver.' in result_text.text


def test_negative_search(browser_setting):
    driver = browser_setting
    driver.get('https://ya.ru/')
    search_input = driver.find_element(By.ID, 'text')
    search_input.send_keys(
        'wwwwwwwwwwwwwwwwwwfdsfffffffffffffffffffffffwwwwwwwwwwwsssssssssssssssssssssssssfsnsdknsdnsnd893892309202')
    search_input.send_keys(Keys.ENTER)
    message = driver.find_element(By.CSS_SELECTOR, '.EmptySearchResults').text
    assert 'Ничего не нашли' in message
