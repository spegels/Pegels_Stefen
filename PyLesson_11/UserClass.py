import random

class user:
    def __init__(self, fName, lName, avat = ""):
        self.firstName = fName
        self.lastName = lName
        self.avatar = avat
        self.userID = random.randint(0, 1000000)

    def __str__(self):
        return "Customer Info... \nFirstName: " + self.firstName + \
               "\nLast Name: " +self.lastName + \
               "\nAvatar: " + self.avatar + \
               "\nUser ID#: " + str(self.userID)    

    def changeAvatar(self, setAvatar):
        self.avatar = setAvatar

    def getfName(self):
        return self.firstName

    def getlName(self):
        return self.lastName

    def getAvatar(self):
        return self.avatar

    def getUserID(self):
        return self.userID

def main():
    firstName = input("Enter first name: ")
    lastName = input("Enter last name: ")
    avatar = input("Would you like to use a public avatar?(y or n)")

    if avatar == "n":
        user1 = user(firstName, lastName)
    elif avatar == "y":
        avatar = input("Enter avatar name: ")
        user1 = user(firstName, lastName, avatar)
    else:
        print("Unknown input...:")
        main()

    print(user1.__str__())



main()

    
    
