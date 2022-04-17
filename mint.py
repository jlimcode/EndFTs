import os
import requests
import json
from web3 import Web3

w3 = Web3(provider=Web3.HTTPProvider())

contract_address = "0x9486423aA84204a16E46cEf83A0543F3D4150725"
my_api_key = os.getenv("POLYGONSCAN_API_KEY")

url = "https://api.polygonscan.com/api"

params = {
    "module": "contract",
    "action": "getabi",
    "address": contract_address,
    "apikey": my_api_key
}

r = requests.get(url=url, params=params)
r_obj = r.json()
abi = json.loads(r_obj['result'])

contract = w3.eth.contract(address=contract_address, abi=abi)

print(contract)