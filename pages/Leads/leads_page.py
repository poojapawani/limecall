from selenium.webdriver.common.by import By
from limecallautomation.base.selenium_driver import SeleniumDriver
import limecallautomation.utilities.custom_logger as cl
import logging
from selenium.webdriver.support.select import Select

class LeadsPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
        wd = SeleniumDriver(driver)
    #Locators
    _date_filter = '//select[@id="filterBydate"]'
    _status_filter = 'filterBystatus'
    _leads_page = '//label[contains(text(),"Leads")]'

    def clickLeadsMenu (self):
        self.ElementClick(locator=self._leads_page, locatorType='xpath')

    def getStatusFilter(self):
        print (self.driver)
        element = self.getElement(locator=self._status_filter)
        statusfilterlist = Select(element)
        statusfilterlist.select_by_visible_text("Failed To Connect Agent")
        print ("Selected Failed to connect agent")
        self.driver.implicitly_wait(3)
        statusfilterlist.select_by_value("completed")
        print("Selected Completed")