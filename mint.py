import os
import requests
import json
# from web3 import Web3, EthereumTesterProvider
from web3.auto import w3

# from eth_tester import EthereumTester, PyEVMBackend

# e = EthereumTester(backend=PyEVMBackend())

# accs = e.get_accounts()

# print(accs)

# w3 = Web3(provider=EthereumTesterProvider())

contract_address = "0x9486423aA84204a16E46cEf83A0543F3D4150725"
my_api_key = os.getenv("POLYGONSCAN_API_KEY")
my_wallet_secret_key = os.getenv("WALLET_PRIVATE_KEY")

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

nonce = w3.eth.get_transaction_count(
    os.getenv("METAMASK_WALLET_ADDY"))  # my wallet transactions

mint_txn = contract.functions.mint(
    "https://ipfs.io/ipfs/bafkreihxrk33rwxbvmydsbcytoygoc7udozgal4p4m6366hyyyrgaftrim"
).buildTransaction({'chainId': 137,
                    'gas': 10,
                    'maxFeePerGas': w3.toWei('2', 'gwei'),
                    'maxPriorityFeePerGas': w3.toWei('1', 'gwei'),
                    'nonce': nonce
                    })

signed_txn = w3.eth.account.sign_transaction(
    mint_txn, private_key=my_wallet_secret_key)

print(signed_txn.hash)

print(signed_txn.rawTransaction)

hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

print(hash)

print(w3.toHex(w3.keccak(signed_txn.rawTransaction)))
