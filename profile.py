profiles = [{"username": "Ahmad2025" , "details":{
    "name": "Ahmad",
    "password": "2025",
    "avatar" : "url",
    "library": {

    }
}}]


def sign_in (username, password):
    for user in profiles:
        if user["username"] == username:
            if user["details"]["password"] != password:
                return ["error" , {"error_details":{"Error_code" :"403" , "Error_msg" : "Password doesn't match"}}]
            return ["success" , user]
        return ["error" , {"error_details":{"Error_code" :"404" , "Error_msg" : "I am sorry but cannot find your account"}}]


def sign_up (username, details):
    for user in profiles:
        if user["username"] == username:
            return ["error", {"error_details":{"Error_code" :"403" , "Error_msg" : "Username already exists"}}]
        else:
            new_user = profiles.append({"username": username, "details": details})
            print(profiles)
            return ["success", new_user ]




