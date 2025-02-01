import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.story('Search')
@allure.severity(allure.severity_level.NORMAL)
@allure.tag('Mobile')
@allure.feature('Поиск в википедии текста "Appium"')
def test_search_wiki_appium():
    with step('Ввести "Appium" в поиске Википедии'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Appium')

    with step('Проверить результат поиска'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))


@allure.story('Search')
@allure.severity(allure.severity_level.NORMAL)
@allure.tag('Mobile')
@allure.feature('Поиск в википедии текста "Moto"')
def test_search_wiki_moto():
    with step('Ввести "Moto" в поиске Википедии'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, "Search Wikipedia")).click()
        browser.element((AppiumBy.ID, "org.wikipedia.alpha:id/search_src_text")).type('Moto')

    with step('Проверить результат поиска'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Moto'))

    with step('Кликнуть на элемент'):
        browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title')).first.click()