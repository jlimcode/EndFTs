import os
from turtle import back
import requests
import json
from web3 import Web3, EthereumTesterProvider
import unicodedata

from eth_tester import EthereumTester, PyEVMBackend

e = EthereumTester(backend=PyEVMBackend())

accs = e.get_accounts()

print(accs)

w3 = Web3(provider=EthereumTesterProvider())

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
b = contract.functions.mint("https://ipfs.io/ipfs/bafkreihxrk33rwxbvmydsbcytoygoc7udozgal4p4m6366hyyyrgaftrim").transact()


print(contract)