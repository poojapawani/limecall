from limecallautomation.base.selenium_driver import SeleniumDriver
import limecallautomation.utilities.custom_logger as cl
import logging
import time

class WidgetPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
        wd = SeleniumDriver(driver)

    #Locators
    _widget_page = "//label[contains(text(),'Widget')]"
    _general_tab = "//a[contains(text(),'General')]"
    _design_tab = "//a[contains(text(),'Design')]"
    _qualification_tab = "//a[contains(text(),'Qualification')]"
    _followup_tab = "//a[contains(text(),'Followup')]"
    _teams_tab = "//a[contains(text(),'Teams')]"
    _countries_tab = "//a[contains(text(),'Countries')]"

