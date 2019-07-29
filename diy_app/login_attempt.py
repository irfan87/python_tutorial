class LoginAttempt:
    def __init__(self, first_name, last_name, username, address):
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.address = address
        self.attempt_login = 0

    def describe_user(self):
        print(f"Fullname: {self.first_name.title()} {self.last_name.title()}")
        print(f"Username: {self.username}")
        print(f"Address: {self.address}")

    def greet_user(self):
        greet_msg = f"Greeting {self.username}!"
        print(greet_msg)

    def increment_login(self):
        self.attempt_login += 1

    def reset_login(self):
        self.attempt_login = 0

user = LoginAttempt("ahmad irfan", "mohammad shukri", "ipan87", "somewhere in malaysia")
user.describe_user()
user.greet_user()

print("Login attempt:")
user.increment_login()
user.increment_login()
user.increment_login()
print(f"You have attempt to login for {user.attempt_login} times")

print("Reset login")
user.reset_login()
print(f"Reset to {user.attempt_login}")
