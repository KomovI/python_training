from fixture.orm import ORMfixture

db = ORMfixture(host="127.0.0.1", name="addressbook", user="root", password="")

print(db.get_group_list())

#try:
#    l=db.get_group_list()
#    for item in l:
#        print(item)
#    print(len(l))
#finally:
#    pass #db.destroy()
