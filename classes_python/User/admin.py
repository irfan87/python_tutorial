from user import User

class Admin(User):
    def __init__(self, first_name, last_name, age, job_title):
        super().__init__(first_name, last_name, age, job_title)
        self.privileges = Privileges()

class Privileges():
    def __init__(self, privileges=[]):
        self.privileges = privileges

    def show_privilege(self):
        
        if self.privileges:
            print("You have the privileges as below")
            for index, privilege in enumerate(self.privileges, start=1):
                print(f"{index} {privilege}")
        else:
            print("No privileges for this user")