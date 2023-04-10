import random
import string
import os.path
import jsonpickle
import getopt
import sys
from model.contact import Contact

try:
    opts, args = getopt.getopt(sys.argv[1:], "n:f:", ["number of groups", "file"])
except getopt.GetoptError as err:
    getopt.usage()
    sys.exit()

n = 5
f = "data/contacts.json"

for o, a in opts:
    if o == "-n":
        n = int(a)
    elif o == "-f":
        f = a


def random_string(prefix, maxlen):
    symbols = string.ascii_letters + string.digits + string.punctuation + " " * 10
    return prefix + "".join([random.choice(symbols) for i in range(random.randrange(maxlen))])


month = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November",
         "December", "-"]


def random_day():
    day = random.choice([""] + list([str(i) for i in range(32)]))
    return day


testdata = [Contact(firstname="", middlename="", lastname="", nickname="",
                    title="", company="", address="", home="",
                    mobile="", work="", fax="", email1="",
                    email2="", email3="", homepage="", birthdayDay="",
                    birthdayMonth="-", birthdayYear="", anniversaryDay="", anniversaryMonth="-",
                    anniversaryYear="", secondaryAddress="", secondaryHome="",
                    notes="")] + [
               Contact(firstname=random_string("firstname", 10), middlename=random_string("middlename", 20),
                       lastname=random_string("lastname", 20), nickname=random_string("nickname", 20),
                       title=random_string("title", 20), company=random_string("company", 20),
                       address=random_string("address", 20), home=random_string("home", 20),
                       mobile=random_string("mobile", 20), work=random_string("work", 20),
                       fax=random_string("fax", 20), email1=random_string("footer", 20),
                       email2=random_string("email2", 20), email3=random_string("email3", 20),
                       homepage=random_string("homepage", 20), birthdayDay=random_day(),
                       birthdayMonth=random.choice(month), birthdayYear=random_string("", 4),
                       anniversaryDay=random_day(), anniversaryMonth=random.choice(month),
                       anniversaryYear=random_string("", 4), secondaryAddress=random_string("secondaryAddress", 20),
                       secondaryHome=random_string("secondaryHome", 20), notes=random_string("notes", 20))
               for i in range(n)
           ]

file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "..", f)

with open(file, "w") as out:
    jsonpickle.set_encoder_options("json", indent=2)
    out.write(jsonpickle.encode(testdata))