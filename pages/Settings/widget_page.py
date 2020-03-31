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
    _settings_page ="//label[contains(text(),'Settings')]"
    _installation_menu ="installation-tab"
    _shareyourlink_tab ='//a[@data-target="#installation-2"]'
    _widget_link ='//a[contains(@href,"rebrand.ly")]'
    _call_icon = '//*[@id="limecall-widget"]/div[1]/div[2]/i[1]'

    def openWidget (self):
        appwindow = self.driver.current_window_handle
        print(appwindow)
        self.ElementClick(locator=self._settings_page,locatorType='xpath')
        self.ElementClick(locator=self._installation_menu)
        self.ElementClick(locator=self._shareyourlink_tab,locatorType='xpath')
        self.ElementClick(locator=self._widget_link,locatorType='xpath')
        handles = self.driver.window_handles
        # Switch to window and search course
        for handle in handles:
            print("Handle: " + handle)
            if handle not in appwindow:
                self.driver.switch_to.window(handle)
                print("Switched to window:: " + handle)
                self.ElementClick(locator=self._call_icon,locatorType='xpath')
                time.sleep(2)
                self.driver.close()
                break

        # Switch back to the parent handle
        self.driver.switch_to.window(appwindow)
        return handles

    #WidgetLocators
    _digitalcall_tab ='clicktocall'
    _callnow_tab = 'callnow'
    _calllater_tab ='calllater'
    _leavemessage_tab='//*[@id="limecall-widget-modal"]/div[1]/div[1]/ul[1]/li[4]/a[1]/div[1]'
    _digitalcall_email_field='limeUserEmail2'
    _digitalcall_name_field ='limeUserName2'
    _digitalcall_team_field ='team'
    _digitalcall_call_button ='//span[contains(text(),"Start Call")]'

    def digitalCalls(self):
        dchandles = self.openWidget()
        print(dchandles)
