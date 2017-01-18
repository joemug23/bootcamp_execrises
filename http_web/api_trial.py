
import requests


def get_a_user(username, password):

    # get data from github api using this request.
    # change the user and pass string in the auth tuple with the desired credentials

    req = requests.get('https://api.github.com/user', auth=(username, password))
    if req.status_code == 200:
        print("Username: " +req.json()["login"])
        print("Account Created on: " +req.json()["created_at"])
        print("Location: " +req.json()["location"])
        return req.text
    elif req.status_code == 404:
        print(str(req.status_code)+" :User not found")
        return "User not found"
    elif req.status_code == 401:
        print(str(req.status_code)+" :Wrong details, Access denied!")
        return "Wrong details, Access denied!"

# call this function with github credentials
# get_a_user("joemug23", "")