from limecallautomation.base.selenium_driver import SeleniumDriver
import limecallautomation.utilities.custom_logger as cl
import logging
import time
from selenium.webdriver.support.select import Select
class ContactsPage(SeleniumDriver):
    log = cl.customLogger(logging.DEBUG)
    def __init__(self,driver):
        super().__init__(driver)
        self.driver =driver
        wd = SeleniumDriver(driver)

    #Locators -
    _contacts_page ="//label[contains(text(),'Contacts')]"
    _addcontact_button ="//button[@onclick='openCreateContactModal()']"
    _addindividual_contact ='individual-contact'
    _addorganization_contact = 'organisation-contact'
    _addcustomer_name ='inputName'
    _addcustomer_email ='inputEmail'
    _addcontact_country='inputCountry'
    _addcontact_countrycode = '//div[@class="selected-flag"]'
    _addcontact_phone='inputPhone'
    _addcontact_submit_button="//button[@onclick='addContact()']"


    def clickContactsMenu(self):
        print ("ENTERINGGGGGGGGGGGGGGG")
        self.ElementClick(locator=self._contacts_page,locatorType='xpath')

    def addIndvidualContact(self,custName,custEmail,custCountry):
        self.ElementClick(locator=self._addcontact_button,locatorType='xpath')
        Individual = self.getElement(locator=self._addindividual_contact)
        self.driver.implicitly_wait(5)
        #Enter Customer Name
        self.sendKeys(data=custName,locator=self._addcustomer_name)
        # Enter Customer Email
        self.sendKeys(data=custEmail, locator=self._addcustomer_email)
        # Enter Customer Country
        self.sendKeys(data=custCountry, locator=self._addcontact_country)
        # Enter Customer Phone number along with country code
        countrycode = self.ElementClick(locator=self._addcontact_countrycode,locatorType='xpath')
        countrytoselect = self.ElementClick(locator="//ul[@id='country-listbox']/li[contains(@data-country-code,'in')]",locatorType='xpath')
        self.sendKeys(data ="9766021368",locator=self._addcontact_phone)
        #click Submit Button
        self.ElementClick(locator="//button[contains(text(),'Submit')]",locatorType='xpath')


        # #leadtoselect = self.ElementClick(locator="//ul[@id='select2-relateCallTxt-results']//li[contains(text(),514)]",locatorType='xpath')
        # testelement =self.getElement(locator='//tr[contains(.,'" + custName + "')]//td[7]")',locatorType='xpath')
        # testelement.click()

