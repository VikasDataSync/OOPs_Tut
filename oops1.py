# initiate a class
class employee :
    # special method/ magic method / dunder method - constructor
    def __init__(self):
        print("Starting executing the constructor")
        self.id = 101
        self.salaary = 50000
        self.designation = "software engineer"
        print("Ending executing the constructor")
    
    def travel(self, destination):
        print("This method is called manually")
        print(f"Employee is travelling to {destination}")


# create an object of the class
sam=employee()

# access the attributes of the class using the object
# print(sam.salaary)

# call the method of the class using the object
sam.travel("Bangalore")

print(type(sam))