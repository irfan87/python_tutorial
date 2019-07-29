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

