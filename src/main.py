import users


print("Welcome")


user = None

userchoice = input("Do you wanna login or signup ?: (login/signup) :")
session_active = True
num_of_tries = 0
while session_active and num_of_tries < 3:
    if userchoice == "login":
        username = input("Username: ")
        password = input("Password: ")

        userDetails = users.sign_in(username, password)
        if userDetails[0] !="error":
            user = userDetails
            print(userDetails)
            print(f"Login Successful, Welcome back {userDetails[1]["details"]["name"]}")
            session_active = False
        else:
            print(userDetails[1]["error_details"]["Error_msg"])
            num_of_tries += 1


    if userchoice == "signup":
        username = input("Username: ")
        name = input("Name: ")
        password = input("Password: ")
        avatar = input("Avatar: ")

        get_result = users.sign_up(username, {"details":{"name":name, "password":password, "avatar":avatar , "library" :{}}})
        if get_result[0] !="error":
            print(f"Sign up Successful, {get_result[1]}")
            session_active = False
        else:
            print(get_result[1]["error_details"]["Error_msg"])
            num_of_tries += 1


if user :

    print(user)