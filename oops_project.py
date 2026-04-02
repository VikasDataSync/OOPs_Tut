class chatbook:
    def __init__(self):
        self.username=""
        self.password=""
        self.loggedin=False
        self.menu()
        
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
            pass
        elif user_input=="4":
            pass
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
obj=chatbook()

