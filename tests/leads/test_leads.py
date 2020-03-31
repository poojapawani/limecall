from selenium import webdriver
import pytest
from limecallautomation.pages.Login.login_page import LoginPage
from limecallautomation.pages.Leads.leads_page import LeadsPage
from limecallautomation.tests import testdata
from selenium.webdriver.support.select import Select
@pytest.mark.usefixtures("LoginSetup")
class TestLeads:
    def test_statusFilter_All (self,LoginSetup):
        print ("((((((**********((((((((((((")
        leads = LeadsPage(LoginSetup)
        leads.clickLeadsMenu()
        leads.getStatusFilter()
