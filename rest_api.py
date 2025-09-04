import requests
import json

url ="https://api.stackexchange.com/2.3/posts?order=desc&sort=activity&site=stackoverflow"
response = requests.get(url)
if response.status_code == 200:
  data = response.json()['items']
  print(data)