class User:
    def __init__(self, first_name, last_name, age, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job_title = job_title
        self.login_attempts = 0

    def describe_user(self):
        print(f"\nFullname: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Job Title: {self.job_title.title()}\n")

    def greet_user(self):
        print(f"Assalamualaikum, {self.first_name.title()}")

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

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
            for privilege in self.privileges:
                print(privilege)
        else:
            print("No privileges for this user")

user = User('ahmad irfan', 'mohammad shukri', 32, 'programmer')
print(user.first_name)
print(user.last_name)
print(user.age)
print(user.job_title)

user.describe_user()
user.greet_user()

# increment login attempt
print("Making login attempt: ")
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f"You have attempt to login in {user.login_attempts} times")

print("\nReset login attempt")
user.reset_login_attempts()
print(f"Reset to {user.login_attempts}")

print("\nAdmin")
irfan = Admin("ahmad irfan", "mohammad shukri", 32, "programmer")
irfan.describe_user()

irfan.privileges.show_privilege()
print("\nAdding privilege...")
irfan_privileges = ['can ban', 'can reset password', 'can suspend accounts']
irfan.privileges.privileges = irfan_privileges
irfan.privileges.show_privilege()