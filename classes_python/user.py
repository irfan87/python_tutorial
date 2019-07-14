class User:
    def __init__(self, first_name, last_name, age, job_title):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.job_title = job_title

    def describe_user(self):
        print(f"\nFullname: {self.first_name.title()} {self.last_name.title()}")
        print(f"Age: {self.age}")
        print(f"Job Title: {self.job_title.title()}\n")

    def greet_user(self):
        print(f"Assalamualaikum, {self.first_name.title()}")

user = User('ahmad irfan', 'mohammad shukri', 32, 'programmer')
print(user.first_name)
print(user.last_name)
print(user.age)
print(user.job_title)

user.describe_user()
user.greet_user()