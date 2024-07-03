from User import User
from Appoinment import Appointment
from MedicalDepartment import MedicalDepartment, departments
from SurgicalDepartment import SurgicalDepartment, dempartments


class Patient(User):
    def __init__(self, firstname, lastname, email, password, address, tel):
        super().__init__(firstname, lastname, email, tel)
        self.__address = address
        self.__password = password
        self.__appointments = []
        self.__selected_department = None
        self.__available_doctors = []

    def select_department(self):
        print("Choose a department:")
        print("1. Medical Department")
        print("2. Surgical Department")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            medical_department = MedicalDepartment(departments)

            self.__selected_department = medical_department.select_department()

            self.__available_doctors = medical_department.get_available_doctors()
        elif choice == "2":
            surgical_department = SurgicalDepartment(dempartments)
            self.__selected_department = surgical_department.select_department()
            self.__available_doctors = surgical_department.get_available_doctors()
        else:
            print("Invalid choice. Please enter 1 or 2.")

    def view_available_doctors(self):
        if self.__available_doctors:
            print(f"\nAvailable doctors in {self.__selected_department} department:")
            for i, doctor in enumerate(self.__available_doctors):
                print(
                    f"{i + 1}. Dr. {doctor._User__firstname} {doctor._User__lastname}, Email: {doctor._User__email}"
                )
        else:
            print("No available doctors. Please select a department first.")

    def create_appointment(self):
        if self.__available_doctors:
            self.view_available_doctors()
            doctor_index = int(input("Select a doctor: ")) - 1

            if 0 <= doctor_index < len(self.__available_doctors):
                selected_doctor = self.__available_doctors[doctor_index]
                print(
                    f"Creating appointment with Dr. {selected_doctor._User__firstname} {selected_doctor._User__lastname}"
                )

                appointment = Appointment(self, selected_doctor)
                appointment.make_appointment()
                self.__appointments.append(appointment)
            else:
                print("Invalid doctor index. Please try again.")
        else:
            print("No available doctors. Please select a department first.")

    def cancel_appointment(self):
        if not self.__appointments:
            print("You have no appointments to cancel.")
            return

        print("Your Appointments:")
        for i, appointment in enumerate(self.__appointments):
            print(
                f"{i + 1}. Appointment with Dr. {appointment.doctor._User__firstname} {appointment.doctor._User__lastname}"
            )

        try:
            choice = (
                int(input("Select the appointment to cancel (enter the number): ")) - 1
            )
            if 0 <= choice < len(self.__appointments):
                canceled_appointment = self.__appointments.pop(choice)
                print(
                    f"Appointment with Dr. {canceled_appointment.doctor._User__firstname} {canceled_appointment.doctor._User__lastname} canceled."
                )
            else:
                print("Invalid appointment number. Please try again.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    def login(self, password, email):
        return password == self.__password and email == self._User__email
