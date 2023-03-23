from model.contact import Contact


class ContactHelper:

    def __init__(self, app):
        self.app = app

    def open_contact_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/addressbook/") and len(wd.find_elements_by_name("add")) > 0):
            wd.find_element_by_link_text("home").click()

    def change_field_value(self, field_name, text):
        wd = self.app.wd
        if text is not None:
            wd.find_element_by_name(field_name).click()
            wd.find_element_by_name(field_name).clear()
            wd.find_element_by_name(field_name).send_keys(text)

    def fill_contact_form(self, contact):
        wd = self.app.wd
        # fill firstname, middlename, lastname, nickname
        self.change_field_value("firstname", contact.firstname)
        self.change_field_value("middlename", contact.middlename)
        self.change_field_value("lastname", contact.lastname)
        self.change_field_value("nickname", contact.nickname)
        # fill title, company, address
        self.change_field_value("title", contact.title)
        self.change_field_value("company", contact.company)
        self.change_field_value("address", contact.address)
        # fill telephone: home, mobile, work and fax
        self.change_field_value("home", contact.homePhone)
        self.change_field_value("mobile", contact.mobilePhone)
        self.change_field_value("work", contact.workPhone)
        self.change_field_value("fax", contact.fax)
        # fill email 3 times and fill homepage
        self.change_field_value("email", contact.email1)
        self.change_field_value("email2", contact.email2)
        self.change_field_value("email3", contact.email3)
        self.change_field_value("homepage", contact.homepage)
        # fill birthday and anniversary
        if contact.birthdayDay is not None:
            wd.find_element_by_name("bday").click()
            wd.find_element_by_xpath("//option[@value='" + contact.birthdayDay + "']").click()
        if contact.birthdayMonth is not None:
            wd.find_element_by_name("bmonth").click()
            wd.find_element_by_xpath("//option[@value='" + contact.birthdayMonth + "']").click()
        self.change_field_value("byear", contact.birthdayYear)
        if contact.anniversaryDay is not None:
            wd.find_element_by_name("aday").click()
            wd.find_element_by_xpath("//div[@id='content']/form/select[3]/option[@value='" +
                                     contact.anniversaryDay + "']").click()
        if contact.anniversaryMonth is not None:
            wd.find_element_by_name("amonth").click()
            wd.find_element_by_xpath("//div[@id='content']/form/select[4]/option[@value='" +
                                     contact.anniversaryMonth + "']").click()
        self.change_field_value("ayear", contact.anniversaryYear)
        # fill secondary data
        self.change_field_value("address2", contact.secondaryAddress)
        self.change_field_value("phone2", contact.secondaryHomePhone)
        self.change_field_value("notes", contact.notes)

    def create(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init contact creation
        wd.find_element_by_link_text("add new").click()
        # fill contact form
        self.fill_contact_form(contact)
        # press "Enter" button
        wd.find_element_by_xpath("//div[@id='content']/form/input[21]").click()
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def edit_first_contact(self, contact):
        wd = self.app.wd
        self.open_contact_page()
        # init first contact modification
        wd.find_element_by_xpath("//img[@alt='Edit']").click()
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_name("update").click()
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def delete_firs_contact(self):
        wd = self.app.wd
        self.open_contact_page()
        # select first contact
        wd.find_element_by_name("selected[]").click()
        # init deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    def get_contact_list(self):
        wd = self.app.wd
        self.open_contact_page()
        contacts = []
        for element in wd.find_elements_by_name("entry"):
            lastname = element.find_element_by_css_selector("td:nth-child(2)").text
            firstname = element.find_element_by_css_selector("td:nth-child(3)").text
            id = element.find_element_by_name("selected[]").get_attribute("value")
            contacts.append(Contact(firstname=firstname, lastname=lastname, id=id))
        return contacts
