from urllib.parse import urljoin
import os

from selenium.webdriver.common.by import By


def test_send_form_demoqa(browser):
    driver, base_url = browser
    driver.get(urljoin(base_url, "/automation-practice-form"))

    driver.find_element(By.CSS_SELECTOR, '#firstName').send_keys('Гвидо ван')
    driver.find_element(By.CSS_SELECTOR, '#lastName').send_keys('Россум')
    driver.find_element(By.CSS_SELECTOR, '#userEmail').send_keys('test_email@sobaka.com')

    driver.find_element(By.CSS_SELECTOR, 'label[for="gender-radio-1"]').click()

    driver.find_element(By.CSS_SELECTOR, '#userNumber').send_keys('4959528833')

    driver.find_element(By.CSS_SELECTOR, '#dateOfBirthInput').click()
    driver.find_element(By.CSS_SELECTOR, '.react-datepicker__year-select').click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="1956"]').click()
    driver.find_element(By.CSS_SELECTOR, 'option[value="0"]').click()
    driver.find_element(By.CSS_SELECTOR,
                        '.react-datepicker__month[aria-label="month  1956-01"] .react-datepicker__day--031').click()

    subjects = driver.find_element(By.CSS_SELECTOR, '#subjectsInput')
    subjects.click()
    subjects.send_keys('English')
    driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__menu').click()
    subjects.click()
    subjects.send_keys('Hindi')
    driver.find_element(By.CSS_SELECTOR, '.subjects-auto-complete__menu').click()

    driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-1"]').click()
    driver.find_element(By.CSS_SELECTOR, 'label[for="hobbies-checkbox-2"]').click()

    picture = driver.find_element(By.CSS_SELECTOR, '#uploadPicture')
    file_path = os.path.abspath('resources/1997.jpg')
    picture.send_keys(file_path)

    driver.find_element(By.CSS_SELECTOR, '#currentAddress').send_keys('Гаага, Нидерланды')

    state = driver.find_element(By.CSS_SELECTOR, '#state')
    state.click()
    driver.find_element(By.CSS_SELECTOR, '#react-select-3-option-0').click()

    city = driver.find_element(By.CSS_SELECTOR, '#city')
    city.click()
    driver.find_element(By.CSS_SELECTOR, '#react-select-4-option-0').click()

    driver.find_element(By.CSS_SELECTOR, '#submit').click()

    table = driver.find_elements(By.CSS_SELECTOR, 'td:nth-child(2)')

    assert table[0].text == 'Гвидо ван Россум'
    assert table[1].text == 'test_email@sobaka.com'
    assert table[2].text == 'Male'
    assert table[3].text == '4959528833'
    assert table[4].text == '31 January,1956'
    assert table[5].text == 'English, Hindi'
    assert table[6].text == 'Sports, Reading'
    assert table[7].text == '1997.jpg'
    assert table[8].text == 'Гаага, Нидерланды'
    assert table[9].text == 'NCR Delhi'
