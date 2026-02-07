# ===============================================================================
# LAB: Introduction to Python class & Objects
# ===============================================================================

#Task 1 - Create a simple class and greet Users
class User:
    def __init__(self, username, role):
        self.username = username
        self.role = role

    def greet_user(self):
        print(f"Hello {self.username}, your role is: {self.role}")

    def changed_role(self, new_role):
        self.role = new_role
        print(f"Welcome, {self.username}! Your changed role is: {self.role} ")


user1 = User('James', 'admin')
user2 = User('Bob', 'User')

user1.greet_user()
user2.greet_user()


# ===============================================================================
# Task 2 - Add a method to change role
# ===============================================================================

print("\n=== Task 2: Change User role ===")
user1.changed_role('Manager')
user1.greet_user()

# ===============================================================================
# Task 3 - Create Multiple Users and store in a list
# ===============================================================================

print("\n=== Task 3: Create Multiple Users and store in a list ===")

user_list=[
    User('Tom','Editor'),
    User('Sara','Reviewer'),
    User('Leo','Author'),
]

for user in user_list:
    user.greet_user()