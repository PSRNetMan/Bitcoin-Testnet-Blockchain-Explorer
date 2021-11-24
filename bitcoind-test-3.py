import requests
import json

user = "mainchain"
password = "hotmax85"

url = "http://" + user + ":" + password + "@0.0.0.0:18332"
headers = {'content-type': 'application/json'}

payload = {"id": 0, "method": "getblockcount", "jsonrpc": "2.0"}
response = requests.post(url, data=json.dumps(payload), headers=headers).json()
print(response["result"])
