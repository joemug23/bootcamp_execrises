
import requests


def get_a_user(username, password):

    # get data from github api using this request.
    # change the user and pass string in the auth tuple with the desired credentials

    req = requests.get('https://api.github.com/user', auth=(username, password))
    if req.status_code == 200:
        print(req.text)
        return req.text
    elif req.status_code == 404:
        print(req.status_code)
        return "User not found"
    elif req.status_code == 401:
        print(req.status_code)
        return "Wrong details, Access denied!"

# call this function with github credentials
# get_a_user("username", "password")