import pytest
from selenium import webdriver
from limecallautomation.tests import testdata
from limecallautomation.pages.Contacts.contacts_page import ContactsPage

@pytest.mark.usefixtures("LoginSetup")
class TestContacts:
    def test_add_contact(self,LoginSetup):
        print ("((((((**********((((((((((((")
        contacts = ContactsPage(LoginSetup)
        contacts.clickContactsMenu()
        contact = testdata.get_user('add_contact1')
        print (contact)
        contacts.addIndvidualContact(contact['custName'],contact['custEmail'],contact['custCountry'])
