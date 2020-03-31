from selenium.webdriver.common.by import By
import limecallautomation.utilities.custom_logger as cl
import logging

class SeleniumDriver():

    log = cl.customLogger(logging.DEBUG)

    def __init__(self,driver):
        self.driver =driver

    def getByType(self,locatorType):
        locatorType = locatorType.lower()
        if locatorType=='id':
            return By.ID
        elif locatorType=='xpath':
            return By.XPATH
        elif locatorType=='name':
            return By.Name
        elif locatorType=='classname':
            return By.CLASS_NAME
        elif locatorType=='css':
            return By.CSS_SELECTOR
        elif locatorType=='linktext':
            return By.LINK_TEXT
        elif locatorType=='partiallinktext':
            return By.PARTIAL_LINK_TEXT
        else:
            self.log.info ("Locator type " +locatorType +" not correct/supported")
        return False

    def getElement (self,locator,locatorType="id"):
        element = None

        try:
            locatorType = locatorType.lower()
            bytype = self.getByType(locatorType)
            element = self.driver.find_element(bytype,locator)
            self.log.info("Element found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Element not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return element
    def getElements (self,locator,locatorType="id"):
        elements= None

        try:
            locatorType = locatorType.lower()
            bytype = self.getByType(locatorType)
            elements = self.driver.find_elements(bytype,locator)
            self.log.info("Elements found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        except:
            self.log.info("Elements not found with locator: " + locator +
                          " and  locatorType: " + locatorType)
        return elements

    def sendKeys (self,data, locator,locatorType="id"):
        try:
            element = self.getElement(locator, locatorType)
            element.send_keys(data)
            self.log.info("Sent data on element with locator " + locator + " locatortype:  " + locatorType)
        except:
            self.log.info("Cannot send data on the element with locator " + locator + " locatortype:  " + locatorType)

    def ElementClick (self,locator,locatorType="id"):
        try:
            element = self.getElement(locator,locatorType)
            element.click()
            self.log.info("Clicked on element with locator " +locator+ " locatortype:  " +  locatorType )
        except:
            self.log.info("Cannot click on the element with locator " +locator+ " locatortype:  " +  locatorType)

    def isElementPresent (self,locator,locatorType='id'):
        try:
            element = self.getElement(locator, locatorType)
            if element is not None:
                self.log.info("Element present")
                return True
            else:
                self.log.info ("Element not present")
                return False
        except:
            self.log.info("Element not present")
            return False
