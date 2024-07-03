class UserAuthentication:
    def authenticate_user(self, username, password):
        if username == "admin" and password == "adminpassword":
            print("Admin authenticated")
        elif username == "patient" and password == "patientpassword":
            print("Patient Authenticated")
        else:
            return None


