import sys
from Patient import Patient
from Doctor import Doctor
from Appoinment import Appointment
from UserAuthentication import UserAuthentication
from Admin import Admin
from Notification import BasicNotification
from Notification import SMSDecorator, EmailDecorator

# creating objects for Admin

Admin1 = Admin("John", "Costa", "costa@gmail.com", "55556564", "445695665")
# creating objects for Patient

patient1 = Patient(
    "John", "Doe", "doe@gmail.com", "doe1258", "Frankfurt 125 St", "1255285"
)
# login credential for patient1 : doe@gmail.com, doe1258
entered_password = input("Enter your password: ")
entered_email = input("Enter your email:")

if patient1.login(entered_password, entered_email):
    print("Patient login successful!")
else:
    print("Invalid email or password ")
    sys.exit()

# creating objects for authtencation

auth_system = UserAuthentication()
authenticated_user = auth_system.authenticate_user("patient", "patientpassword")
selected_department = patient1.select_department()
patient1.view_available_doctors()
patient1.create_appointment()
print(selected_department)

# creating objects for notification

basic_notification = BasicNotification()

email_notification = EmailDecorator(basic_notification)
sms_notification = SMSDecorator(basic_notification)

email_notification.send_notification()
sms_notification.send_notification()
