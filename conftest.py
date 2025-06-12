import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


@pytest.fixture(scope='function')
def browser():
    """
        Фикстура для инициализации и закрытия браузера Chrome.

        Настройки:
        - Открывает окно размером 1920x1080 пикселей.
        - Автоматически закрывает браузер после завершения теста.

        Пример использования в тесте:
        ```
        def test_example(browser):
            browser.get("https://example.com")
            assert "Example" in browser.title
        ```
        """
    chrome_options = Options()
    chrome_options.add_argument('--window-size=1920,1080')
    chrome_options.add_argument('--ignore-ssl-errors=yes')
    chrome_options.add_argument('--ignore-certificate-errors')
    chrome_options.add_argument('--allow-insecure-localhost')

    driver = webdriver.Chrome(options=chrome_options)

    base_url = "https://demoqa.com"
    driver.get(base_url)

    yield driver, base_url
    driver.delete_all_cookies()
    driver.quit()
