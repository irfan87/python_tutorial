from user import User
from admin import Admin

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