import pytest
from selenium import webdriver
from limecallautomation.tests import testdata
from limecallautomation.pages.Settings.widget_page import WidgetPage
from limecallautomation.pages.Widget.design_page import WidgetDesign

@pytest.mark.usefixtures("LoginSetup")
class TestWidget:
    def test_widget_template(self,LoginSetup):
        widgetdesign = WidgetDesign(LoginSetup)
        widgetdesign.selectTemplate(templateType="Classic")
