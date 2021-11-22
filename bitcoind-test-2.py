import requests
import json

user = "mainchain"
password = "hotmax85"

url = "http://" + user + ":" + password + "@0.0.0.0:18332"
headers = {'content-type': 'application/json'}

payload = {"id": 0, "method": "getbestblockhash", "jsonrpc": "2.0"}
response = requests.post(url, data=json.dumps(payload), headers=headers).json()
mhash = response["result"]

payload = {"id": 0, "method": "getblock", "params": [mhash], "jsonrpc": "2.0"}
response = requests.post(url, data=json.dumps(payload), headers=headers).json()
block = response["result"]

for y in block:
    if str(y) != "tx": #This is excluded as it's too long to print
        print(str(y) + ": " + str(block[y]))
