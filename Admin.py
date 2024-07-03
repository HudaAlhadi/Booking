from User import User


class Admin(User):
    def __init__(self, firstname, lastname, email, password, tel):
        super().__init__(firstname, lastname, email, tel)
        self.__password = password
        self.schedule = []

    def update_schedule(self, new_schedule):
        self.schedule = new_schedule
        print("Schedule updated successfully.")
