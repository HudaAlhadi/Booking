from DepartmentInterface import DepartmentInterface
from Doctor import Doctor

departments = [
    {"id": "1", "name": "radiology"},
    {"id": "2", "name": "cardiology"},
    {"id": "3", "name": "orthopedics"},
    {"id": "4", "name": "ophthalmology"},
    {"id": "5", "name": "urology"},
]


class MedicalDepartment(DepartmentInterface):
    def __init__(self, medicaldepartments):
        self.__medicaldepartments = medicaldepartments
        self.available_doctors = [
            Doctor(
                "dr8@example.com",
                "Roop",
                "John",
                "radiology",
                ["9:00 AM", "1:00 PM"],
                "555-8765",
                "dhdjpp5585",
            ),
            Doctor(
                "dr9@example.com",
                "Pardeep",
                "Williams",
                "cardiology",
                ["12:00 PM", "4:00 PM"],
                "555-4321",
                "1552dddd",
            ),
        ]

    def select_department(self):
        for i, department in enumerate(self.__medicaldepartments):
            print(f"{i + 1}- {department['name']}")

        while True:
            department_index = int(input("Please select a medical department: ")) - 1

            if 0 <= department_index < len(self.__medicaldepartments):
                break
            else:
                print("Invalid department index. Please try again.")

        selected_department = self.__medicaldepartments[department_index]
        return selected_department["name"]

    def get_available_doctors(self):
        return self.available_doctors
