
import requests
# get data from github api using this request.
# change the user and pass string in the auth tuple with the desired credentials
req = requests.get('https://api.github.com/user', auth=('user', 'pass'))
print(req.text)




