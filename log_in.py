def log_in(users, username, password):
    if username in users and users[username] == password:
        print("Login successful! Welcome ")
    else:
        print("Invalid username or password.")