import pytest
from selenium import webdriver
from limecallautomation.tests import testdata
from limecallautomation.pages.Login.login_page import LoginPage

@pytest.yield_fixture(scope='module')
def oneTimeSetUp():
    print("Entered class")
    driver = webdriver.Chrome()
    driver.maximize_window()
    baseurl = "https://qa.limecall.com"
    driver.get(baseurl)
    return driver


@pytest.yield_fixture(scope='module')
def LoginSetup():
    print("Entered into login class")
    driver = webdriver.Chrome()
    driver.maximize_window()
    baseurl = "https://qa.limecall.com"
    driver.get(baseurl)
    user = testdata.get_user('valid_name')
    lp = LoginPage(driver)
    lp.login(user['email'], user['pwd'])
    result =lp.login_verification()
    assert result == True
    return driver