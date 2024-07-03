from DepartmentInterface import DepartmentInterface
from Doctor import Doctor

dempartments = [
    {"id": "1", "name": "General Surgery "},
    {"id": "2", "name": "colon surgery"},
    {"id": "3", "name": "bladder surgery"},
    {"id": "4", "name": "breast surgery"},
    {"id": "5", "name": "thyroid surgery"},
]


class SurgicalDepartment(DepartmentInterface):
    def __init__(self, surgicaldepartments):
        self.__surgicaldepartments = surgicaldepartments

    def select_department(self):
        for i, department in enumerate(self.__surgicaldepartments):
            print(f"{i + 1}- {department['name']}")

        while True:
            department_index = int(input("Please select surgical department: ")) - 1

            if 0 <= department_index < len(self.__surgicaldepartments):
                break
            else:
                print("Invalid department index. Please try again.")

        selected_department = self.__surgicaldepartments[department_index]
        print(f"\nAvailable doctors in {selected_department['name']} department:")
        self.available_doctors = [
            Doctor(
                "dr3@example.com",
                "Michael",
                "Johnson",
                selected_department["name"],
                ["9:00 AM", "1:00 PM"],
                "555-8765",
                "515515**",
            ),
            Doctor(
                "dr4@example.com",
                "Emily",
                "Williams",
                selected_department["name"],
                ["12:00 PM", "4:00 PM"],
                "555-4321",
                "515512852**",
            ),
        ]
        return selected_department["name"]

    def get_available_doctors(self):
        return self.available_doctors
