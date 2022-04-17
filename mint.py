import json
import logging
import requests
from tokens import *
from web3 import HTTPProvider, Web3

def create_nft(uri: str):

    contract_address = "0x9486423aA84204a16E46cEf83A0543F3D4150725"

    url = "https://api.polygonscan.com/api"

    params = {
        "module": "contract",
        "action": "getabi",
        "address": contract_address,
        "apikey": POLYGONSCAN_API_KEY
    }

    r = requests.get(url=url, params=params)
    r_obj = r.json()
    abi = json.loads(r_obj['result'])

    w3 = Web3(HTTPProvider("https://rpc.ankr.com/polygon"))

    logging.info(w3.isConnected())

    contract = w3.eth.contract(address=contract_address, abi=abi)

    # my wallet transactions
    nonce = w3.eth.get_transaction_count( METAMASK_WALLET_ADDY)

    mint_txn = contract.functions.mint(uri).buildTransaction({'chainId': 137,
                        'gas': 249003,
                        # 'gasPrice': w3.toWei('40', 'gwei'),
                        'maxFeePerGas': w3.toWei('40', 'gwei'),
                        'maxPriorityFeePerGas': w3.toWei('31', 'gwei'),
                        'nonce': nonce
                        })

    signed_txn = w3.eth.account.sign_transaction(
        mint_txn, private_key=WALLET_PRIVATE_KEY)

    logging.info(signed_txn.hash)
    logging.info(signed_txn.rawTransaction)

    hash = w3.eth.send_raw_transaction(signed_txn.rawTransaction)

    logging.info(hash)
    logging.info(w3.toHex(w3.keccak(hash)))
    logging.info(w3.toHex(w3.keccak(signed_txn.rawTransaction)))
    
    return w3.toHex(w3.keccak(hash))
