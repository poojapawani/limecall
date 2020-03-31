import unittest
from selenium import webdriver
from limecallautomation.pages.Login.login_page import LoginPage
from limecallautomation.tests import testdata
import pytest
#
@pytest.mark.usefixtures("oneTimeSetUp")
class LoginTests(unittest.TestCase):

    @pytest.fixture(autouse=True)
    def classSetup(self, oneTimeSetUp):
        oneTimeSetUp.get("https://qa.limecall.com")
        self.lp = LoginPage(oneTimeSetUp)

    @pytest.mark.run(order=1)
    def test_blank_password(self):
        print ("Ran setup")
        user = testdata.get_user('blank_password')
        self.lp.login(user['email'], user['pwd'])
        result = self.lp.login_passwordfield_verification()
        print (result)
        assert result == "This field is required."

    @pytest.mark.run(order=2)
    def test_blank_email(self):
        user = testdata.get_user('blank_email')
        self.lp.login(user['email'], user['pwd'])
        result = self.lp.login_emailfield_verification()
        print (result)
        if user['email'] == "":
            assert result == "This field is required."
        else:
            assert result == "Please enter a valid email address."

    @pytest.mark.run(order=4)
    def test_invalid_login(self):
        user = testdata.get_user('invalid_name')
        self.lp.login(user['email'], user['pwd'])
        result = self.lp.login_verification()
        assert result == False

    @pytest.mark.run(order=3)
    def test_invalid_error_login(self):
        user = testdata.get_user('invalid_name2')
        self.lp.login(user['email'], user['pwd'])
        result = self.lp.login_verification_negative()
        assert result == True
#     #


    @pytest.mark.run(order=5)
    def test_invalid_email(self):
        user = testdata.get_user('invalid_email')
        self.lp.login(user['email'], user['pwd'])
        result = self.lp.login_emailfield_verification()
        print (result)
        assert result == "Please enter a valid email address."

    @pytest.mark.run(order=6)
    def test_valid_login(self):
        print ("Entered")
        user = testdata.get_user('valid_name')
        self.lp.login(user['email'], user['pwd'])
        result = self.lp.login_verification()
        assert result == True




# if __name__ == "__main__":
#     suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
#     unittest.TextTestRunner(verbosity=2).run(suite)

