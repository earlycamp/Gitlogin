import json
import requests
from decouple import config,Csv

# private token and api url
api_token = config('api_token')
api_url_base = config('api_url_base')

# will request earlycamp users
response = requests.get( api_url_base + api_token ).json()

# will make sure only members are redirected
for i in response:
	print(i)





