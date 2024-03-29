from sys import maxsize


class Contact:

    def __init__(self, firstname=None, middlename=None, lastname=None, nickname=None, title=None, company=None,
                 address=None, home=None, mobile=None, work=None, fax=None, email1=None, email2=None, email3=None,
                 homepage=None, birthdayDay=None, birthdayMonth=None, birthdayYear=None, anniversaryDay=None,
                 anniversaryMonth=None, anniversaryYear=None, secondaryAddress=None, secondaryHome=None, notes=None,
                 id=None, all_phones_from_home_page=None, all_emails_from_home_page=None):
        self.firstname = firstname
        self.middlename = middlename
        self.lastname = lastname
        self.nickname = nickname
        self.title = title
        self.company = company
        self.address = address
        self.homePhone = home
        self.mobilePhone = mobile
        self.workPhone = work
        self.fax = fax
        self.email1 = email1
        self.email2 = email2
        self.email3 = email3
        self.homepage = homepage
        self.birthdayDay = birthdayDay
        self.birthdayMonth = birthdayMonth
        self.birthdayYear = birthdayYear
        self.anniversaryDay = anniversaryDay
        self.anniversaryMonth = anniversaryMonth
        self.anniversaryYear = anniversaryYear
        self.secondaryAddress = secondaryAddress
        self.secondaryHomePhone = secondaryHome
        self.notes = notes
        self.id = id
        self.all_phones_from_home_page = all_phones_from_home_page
        self.all_emails_from_home_page = all_emails_from_home_page

    def __repr__(self):
        return "%s:%s:%s:%s:%s" % (self.id, self.firstname, self.lastname, self.anniversaryDay, self.birthdayDay)

    def __eq__(self, other):
        return (self.id is None or other.id is None or self.id == other.id) and \
            self.firstname.strip() == other.firstname.strip() and self.lastname == self.lastname

    def id_or_max(self):
        if self.id:
            return int(self.id)
        else:
            return maxsize
