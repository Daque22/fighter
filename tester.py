users = {
    "administrator": [{"username": "admin", "password": "123"}],
    "manager": [{"username": "manager1", "password": "123"}],
    "employee": [{"username": "employee1", "password": "123"}]
}

for u in users.get("administrator", []):
    user = input("inter your username: ")
    password = input("inter your password: ")
    if u["username"] == user and u["password"] == password:
        print("LOGIN SUCCESSFULLY")