from django.shortcuts import render
from django.http import HttpResponse
import requests, json, datetime

user = "mainchain"
password = "hotmax85"

url = "http://" + user + ":" + password + "@0.0.0.0:18332"
headers = {'content-type': 'application/json'}

# Create your views here.
def index(request):
    heightvar = request.GET.get('height', '')

    payload = {"id": 0, "method": "getblockcount", "jsonrpc": "2.0"}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    maxheight = int(response["result"])

    if heightvar == '':
       return render(request, "myapp/home.html", {'result': "Height of most recent block is " + str(maxheight) + "."})

    try:
       heightint = int(heightvar)
    except:
       return render(request, "myapp/home.html", {'result': "ERROR: Input must be an Integer."})

    if heightint < 0 or heightint > maxheight:
       return render(request, "myapp/home.html", {'result': "ERROR: Input must be between 0 and " + str(maxheight) + "."})

    payload = {"id": 0, "method": "getblockhash", "params": [heightint], "jsonrpc": "2.0"}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    mhash = response["result"]

    payload = {"id": 0, "method": "getblock", "params": [mhash], "jsonrpc": "2.0"}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    block = response["result"]

    return render(request, "myapp/home.html", {'block': block})

def exptest(request):
    prm = request.GET.get('anything', '')
    if prm == '':
       return HttpResponse("Tester Bester")
    else:
       return HttpResponse(prm)

def blocktest(request):
    payload = {"id": 0, "method": "getbestblockhash", "jsonrpc": "2.0"}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    mhash = response["result"]

    payload = {"id": 0, "method": "getblock", "params": [mhash], "jsonrpc": "2.0"}
    response = requests.post(url, data=json.dumps(payload), headers=headers).json()
    block = response["result"]

    response = ''
    for y in block:
        if str(y) != "tx": #This is excluded as it's too long to print
            response = response + "<p>" +  str(y) + ": " + str(block[y]) + "</p>"
    
    return HttpResponse(response)
