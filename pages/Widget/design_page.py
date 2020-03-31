from limecallautomation.base.selenium_driver import SeleniumDriver
import limecallautomation.utilities.custom_logger as cl
import logging
import time
from selenium.webdriver.support.select import Select

class WidgetDesign(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver = driver
        wd = SeleniumDriver(driver)

    #Locators
    _widget_page = "//label[contains(text(),'Widget')]"
    _design_tab = "//a[contains(text(),'Design')]"
    _widget_template = "//a[@data-target='#widgetTemplate']"
    _widget_template_dropdown ="//select[@name='template_type']"
    _update_button ="//*[@id='widgetForm']/button[@type='submit']"


    def selectTemplate(self,templateType):
        self.ElementClick(locator=self._widget_page,locatorType='xpath')
        self.ElementClick(locator=self._design_tab,locatorType='xpath')
        self.ElementClick(locator=self._widget_template,locatorType='xpath')
        element = self.getElement(locator=self._widget_template_dropdown,locatorType='xpath')
        widget_template_options = Select (element)
        widget_template_options.select_by_visible_text(templateType)
        self.ElementClick(locator= self._update_button,locatorType='xpath')

