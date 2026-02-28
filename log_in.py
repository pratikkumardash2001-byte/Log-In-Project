def log_in(users, username, password):
    if username in users and users[username] == password:
        print("Log-in successful! Welcome")
    else:
        print("Invalid username or password")