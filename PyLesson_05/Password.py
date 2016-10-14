user = "ColonelSanders"
passw = "fingerlickingood"

def passCheck():
    user = input("Enter username: ")
    passw = input("Enter password: ")
    if user == "ColonelSanders" and passw == "fingerlickingood":
        print("You are granted access.")
    if user != "ColonelSanders" and passw == "fingerlickingood":
        print("Username is incorrect.")
        passCheck()
    if user == "ColonelSanders" and passw != "fingerlickingood":
        print("Password is incorrect.")
        passCheck()
    if user != "ColonelSanders" and passw != "fingerlickingood":
        print("Both username and password are incorrect.")
        passCheck()

        


passCheck()
