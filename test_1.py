from testpage_1 import OperationsHelper
import logging
import time


def test_step1(browser):
    logging.info('Test Starting')
    testpage = OperationsHelper(browser)
    testpage.go_to_site()
    testpage.enter_login('Oleggov666')
    testpage.enter_pass('256ec8af00')
    testpage.click_login_button()
    testpage.click_contact_button()
    time.sleep(4)
    testpage.enter_name('Dmitriy Leonov')
    testpage.enter_email('d.leonov@yandex.ru')
    testpage.enter_content('Test Text')
    time.sleep(4)
    testpage.click_contact_us_button()
    time.sleep(4)
    assert testpage.alert() == 'Form successfully submitted'