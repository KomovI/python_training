from model.contact import Contact
import re

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
        self.edit_contact_by_index(0, contact)

    def edit_contact_by_index(self, index, contact):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_name("update").click()
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def edit_contact_by_id(self, id, contact):
        wd = self.app.wd
        self.open_contact_edit_by_id(id)
        self.fill_contact_form(contact)
        # submit modification
        wd.find_element_by_name("update").click()
        # return to home page
        wd.find_element_by_link_text("home page").click()

    def delete_first_contact(self):
        self.delete_contact_by_index(0)

    def delete_contact_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        # select contact by index
        wd.find_elements_by_name("selected[]")[index].click()
        # init deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()

    def delete_contact_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        # select contact by index
        self.select_contact_by_id(id)
        # init deletion
        wd.find_element_by_xpath("//input[@value='Delete']").click()
        # submit deletion
        wd.switch_to.alert.accept()
        wd.find_element_by_link_text("home").click()

    def select_contact_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("input[value='%s']" % id).click()

    def add_contact_to_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("option[value='']").click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("to_group").find_element_by_css_selector("option[value='%s']" % group_id).click()
        wd.find_element_by_name("add").click()
        wd.find_element_by_link_text("home").click()

    def delete_contact_from_group(self, contact_id, group_id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector("option[value='%s']" % group_id).click()
        self.select_contact_by_id(contact_id)
        wd.find_element_by_name("remove").click()
        wd.find_element_by_link_text("home").click()

    def count(self):
        wd = self.app.wd
        self.open_contact_page()
        return len(wd.find_elements_by_name("selected[]"))

    contact_cache = None

    def get_contact_list(self):
        if self.contact_cache is None:
            wd = self.app.wd
            self.open_contact_page()
            self.contact_cache = []
            for element in wd.find_elements_by_name("entry"):
                lastname = element.find_element_by_css_selector("td:nth-child(2)").text
                firstname = element.find_element_by_css_selector("td:nth-child(3)").text
                address = element.find_element_by_css_selector("td:nth-child(4)").text
                id = element.find_element_by_name("selected[]").get_attribute("value")
                all_phones = element.find_element_by_css_selector("td:nth-child(6)").text
                all_emails = element.find_element_by_css_selector("td:nth-child(5)").text
                self.contact_cache.append(Contact(firstname=firstname, lastname=lastname, id=id, address=address,
                                                  all_phones_from_home_page=all_phones,
                                                  all_emails_from_home_page=all_emails))
        return self.contact_cache

    def open_contact_edit_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_elements_by_xpath("//img[@alt='Edit']")[index].click()

    def open_contact_edit_by_id(self, id):
        wd = self.app.wd
        self.open_contact_page()
        wd.find_element_by_css_selector('a[href="edit.php?id=%s"]' % id).click()

    def open_contact_view_by_index(self, index):
        wd = self.app.wd
        self.open_contact_page()
        row = wd.find_elements_by_name("entry")[index]
        cell = row.find_elements_by_tag_name("td")[6]
        cell.find_element_by_tag_name("a").click()

    def get_full_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        address = wd.find_element_by_name("address").get_attribute("value")
        email1 = wd.find_element_by_name("email").get_attribute("value")
        email2 = wd.find_element_by_name("email2").get_attribute("value")
        email3 = wd.find_element_by_name("email3").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, home=homephone, work=workphone,
                       mobile=mobilephone, secondaryHome=secondaryphone, email1=email1, email2=email2, email3=email3,
                       address=address)

    def get_contact_info_from_edit_page(self, index):
        wd = self.app.wd
        self.open_contact_edit_by_index(index)
        firstname = wd.find_element_by_name("firstname").get_attribute("value")
        lastname = wd.find_element_by_name("lastname").get_attribute("value")
        id = wd.find_element_by_name("id").get_attribute("value")
        homephone = wd.find_element_by_name("home").get_attribute("value")
        workphone = wd.find_element_by_name("work").get_attribute("value")
        mobilephone = wd.find_element_by_name("mobile").get_attribute("value")
        secondaryphone = wd.find_element_by_name("phone2").get_attribute("value")
        return Contact(id=id, firstname=firstname, lastname=lastname, home=homephone, work=workphone,
                       mobile=mobilephone, secondaryHome=secondaryphone)

    def get_contact_info_from_view_page(self, index):
        wd = self.app.wd
        self.open_contact_view_by_index(index)
        text = wd.find_element_by_id("content").text
        homephone = re.search("H: (.*)", text).group(1)
        workphone = re.search("W: (.*)", text).group(1)
        mobilephone = re.search("M: (.*)", text).group(1)
        secondaryphone = re.search("P: (.*)", text).group(1)
        return Contact(home=homephone, work=workphone,
                       mobile=mobilephone, secondaryHome=secondaryphone)
