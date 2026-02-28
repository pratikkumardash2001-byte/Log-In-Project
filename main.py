import log_in
import log_out

listdata = {"pratik": 1234, "rohit": 4567}

print("please type : 'login' to login or 'logout' to logout.")
action = input("What do you want to do? ")
username = input("please enter your username: ")
password = input("please enter your password : ")

password = int(password)

if action == "login":
    log_in.log_in(listdata, username, password)
elif action == "logout":
    log_out.log_out(listdata, username, password)
else:
    print("Invalid action!")