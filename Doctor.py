from User import User


class Doctor(User):
    def __init__(
        self, email, firstname, lastname, department, timeslots, tel, password
    ):
        super().__init__(firstname, lastname, email, tel)
        self.__department = department
        self.__timeslots = timeslots
        self.__password = password

    def view_available_slots(self):
        print(
            f"\nAvailable time slots for Dr. {self._User__firstname} {self._User__lastname} in {self.__department}:"
        )
        for i, slot in enumerate(self.__timeslots):
            print(f"{i + 1}- {slot}")

    def select_available_date(self):
        available_date = [
            "2023-12-01",
            "2023-12-02",
            "2023-12-03",
            "2023-12-04",
            "2023-12-05",
            "2023-12-06",
            "2023-12-07",
        ]
        for i, date in enumerate(available_date):
            print(f"{i + 1}. {date}")

        selection = int(input("Select a date: ")) - 1
        selected_date = available_date[selection]
        return selected_date

    def __str__(self):
        return f"{self._User__firstname} {self._User__lastname}- {self.__department} "

    def login(self, entered_password):
        return entered_password == self.__password
