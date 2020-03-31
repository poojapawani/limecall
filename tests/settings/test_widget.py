import pytest
from selenium import webdriver
from limecallautomation.tests import testdata
from limecallautomation.pages.Settings.widget_page import WidgetPage

@pytest.mark.usefixtures("LoginSetup")
class TestWidget:
    def test_open_widget(self,LoginSetup):
        print ("((((((**********((((((((((((")
        widget = WidgetPage(LoginSetup)
        widget.digitalCalls()
