class User:
    def __init__(self, firstname, lastname, email, tel):
        self.__email = email
        self.__firstname = firstname
        self.__lastname = lastname
        self.__tel = tel

    def register(self, email, password):
        email = input("enter your email")
        password = input("enter your password")
