# importing class from oops_project import chatbook
from oops_project import chatbook

user1=chatbook()
print(user1.id)
# user2=chatbook()
# print(user2.id)
# user3=chatbook()
# print(user3.id)

# using static method to set value to private variable and then accessing it using another object of the class
chatbook.set_id(10)
user2=chatbook()
print(user2.id)



# print(user2.get_name()) # accessing private variable using getter method
# user2.set_name("Jai") # setting value to private variable using setter method
# print(user2.get_name()) # accessing private variable using getter method after setting value using setter method

