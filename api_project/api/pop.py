
from django.contrib.auth.models import User
# Create some dummy users

users_data = [
    {"username": "john_doe", "email": "john@example.com", "password": "password123"},
    {"username": "jane_smith", "email": "jane@example.com", "password": "password123"},
    {"username": "admin", "email": "admin@example.com", "password": "adminpassword"},
]

# Add users if they do not already exist
for user_data in users_data:
    user, created = User.objects.get_or_create(
        username=user_data["username"],
        email=user_data["email"],
    )
    if created:
        user.set_password(user_data["password"])
        user.save()
        print(f"User '{user.username}' added.")
    else:
        print(f"User '{user.username}' already exists.")

# Retrieve the users
user1 = User.objects.get(username="john_doe")
user2 = User.objects.get(username="jane_smith")
user3 = User.objects.get(username="admin")