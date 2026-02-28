def log_out(users, username, password):
    if username in users and users[username] == password:
        print(" logged out successfully!")
    else:
        print("Invalid username or password for logout.")