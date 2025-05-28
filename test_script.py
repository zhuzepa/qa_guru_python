from selene import browser, be, have


browser.open('https://google.com')
browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
browser.element('html').should(have.text('About this page'))