class chatbook:
    __user_id=0 # class variable to keep track of user id and it is private variable as well
    def __init__(self):
        self.id=chatbook.__user_id # assigning value of class variable to instance variable
        chatbook.__user_id+=1      # incrementing class variable by 1 for next user
        self.__name="Default Name" # private variable
        self.username=""
        self.password=""
        self.loggedin=False
        # self.menu()
        
    # getter and setter methods to access private variable    
    def get_name(self): # getter method to access private variable
        return self.__name
        
    def set_name(self,value): # setter method to set value to private variable
        self.__name=value

    @staticmethod
    def get_id():
        return chatbook.__user_id
    
    @staticmethod
    def set_id(val):
        chatbook.__user_id=val
    
    
    
    def menu(self):
        user_input=input("""Welcome to Chatbook !! How would you like to proceed ? 
                         1. Press 1 to signup
                         2. Press 2 to login
                         3. Press 3 to write a post
                         4. Press 4 to message a friend
                         5. Press any other key to exit
                         Enter your choice : """)
        
        if user_input=="1":
            self.signup()
        elif user_input=="2":
            self.login()
        elif user_input=="3":
            self.my_post()
        elif user_input=="4":
            self.message_friend()
        else:
            exit()

    def signup(self):
        email=input("Enter your email : ")
        pwd=input("Enter your password : ")
        self.username=email
        self.password=pwd
        print("Signup successful !!")
        print("\n")
        self.menu()
            
    def login(self):
        email=input("Enter your email : ")
        pwd=input("Enter your password : ")
        if email==self.username and pwd==self.password:
            self.loggedin=True
            print("Login successful !!")
        else:
            print("Invalid Credentials !!")
        print("\n")
        self.menu()
        
    def my_post(self):
        if self.loggedin==True:
            txt=input("Enter your post : ")
            print(f"Following content has been posted : {txt}")
        else:
            print("Please login to post something !!")
            print("\n")
            self.menu()
    
    def message_friend(self):
        if self.loggedin==True:
            txt=input("Enter your message : ")
            frnd=input("Enter your friend's name : ")
            print(f"Following message has been sent to {frnd} : {txt}")
            print("\n")
            self.menu()
        else:
            print("Please login to message your friend !!")
            print("\n")
            self.menu()
            


