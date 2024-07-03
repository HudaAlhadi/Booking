class Appointment:
    def __init__(self, patient, doctor):
        self.__patient = patient
        self.__doctor = doctor

    def make_appointment(self):
        selected_slot = self.__doctor.view_available_slots()
        selection = int(input("Select a slot: ")) - 1
        selected_slot = self.__doctor._Doctor__timeslots[selection]

        seleted_date = self.__doctor.select_available_date()

        patient_firstname = self.__patient._User__firstname
        print(
            f"Appointment booked for {patient_firstname} with DR {self.__doctor._User__firstname}: at {selected_slot}, {seleted_date}"
        )
