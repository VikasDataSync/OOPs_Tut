# # simple inheritance example
 
# # base class
# class Animal:
#     def __init__(self,name):
#         self.name=name
        
#     def speak(self):
#         print(f"{self.name} make a sound")
    

# # derived class
# class Dog(Animal): # synstax for inheritance is class DerivedClass(BaseClass):
#     def __init__(self):
#         self.behavior="Friendly"
#     def speak(self):
#         print(f"Buddy barks & His behavior is {self.behavior}")

   
# # object of base class
# # animal = Animal("Generic Animal")
# # animal.speak() # Output: Generic Animal make a sound

# # object of derived class
# dog = Dog()
# dog.speak() # Output: Buddy barks


class Animal:
    def __init__(self):
        self.name="Buddy"
        
    def speak(self):
        print(f"{self.name} make a sound")
        
class Dog(Animal):
    def __init__(self,breed): # constructor of derived class with parameter breed to set the breed of the dog
        super().__init__()
        self.breed=breed
        
    def speak(self):
        super().speak() # calling the speak method of base class using super() function to reuse the code of base class and then adding additional functionality in derived class 
        print(f"{self.name} barks and his breed is {self.breed}")

dog=Dog("Golden Retriever")
dog.speak()