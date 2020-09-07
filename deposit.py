#!/usr/bin/python3

from web3 import Web3, HTTPProvider, middleware
import sys
import json
import time
import yaml
from web3.gas_strategies.time_based import medium_gas_price_strategy, fast_gas_price_strategy, slow_gas_price_strategy

try:
    w3 = Web3(HTTPProvider("https://kovan.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60}))
except Exception as e:
    print('\033[91m\033[1m' + 'Error : Could not connect to Provider' + '\033[0m\033[0m')
    print(e)
    exit()

w3.middleware_onion.add(middleware.time_based_cache_middleware)
w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
w3.middleware_onion.add(middleware.simple_cache_middleware)

try:
    uniswap_router2_address =  Web3.toChecksumAddress("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")
    #Uniswap exchange contract abi
    with open("./abi/uniswap_router2_abi.json") as f:
        uniswap_router2_abi = json.load(f)

    uniswap_router2 = w3.eth.contract(
        address= uniswap_router2_address,
        abi= uniswap_router2_abi
    )
    weth_address = uniswap_router2.functions.WETH().call()
except Exception as e:
    print('\033[91m\033[1m' + 'Error : Could not reach Uniswap router2 contract' + '\033[0m\033[0m')
    print(e)
    exit()

#Get user address and private key to sing transactions
# ------- A CHANGER : par input de l'adresse et private key par user
address = '0x1f274e65B39C9206612480D43CF3e5B1634f22B2'
private_key = "56e8aa21e470e5efefa5db872c96f49e117b12a10da335b32ea51f4fb2a20419"
# ------------
try:
  w3.isAddress(address)
except Exception as e:
    print('\033[91m\033[1m' + 'Error : Eth address not valid' + '\033[0m\033[0m')
    print(e)
    exit()

try: 
    with open("./allocation.yml") as f:
        tokens = yaml.load(f, Loader=yaml.FullLoader)
except Exception as e:
    print('\033[91m\033[1m' + 'Error : File allocation.yml not found' + '\033[0m\033[0m')

try:
  eth_sold = w3.eth.getBalance(address)
except Exception as e:
    print('\033[91m\033[1m' + "Error : can't retrive Eth address balance :" + '\033[0m\033[0m')
    print(e)
    exit()

#Go through ERC20 tokens, and trade if % is given in yml alloc file
for t in tokens:
    #Get ERC20 amount depending %:
    eth_amount = int(eth_sold * tokens[t]['allocation'])
    amount = uniswap_router2.functions.getAmountsOut(eth_amount, [weth_address, tokens[t]['contract_address']]).call()[-1]
    print("ETH amount :")
    print(w3.fromWei(eth_amount, 'ether'))
    print("asking for " + t + " :")
    print(w3.fromWei(amount, 'ether'))
    #Uniswap trade transaction
    try:
        tx_dict = uniswap_router2.functions.swapExactETHForTokens(
            amount, [weth_address, tokens[t]['contract_address']], address, int(time.time())+10*60).buildTransaction({
                'from': address,
                'nonce': w3.eth.getTransactionCount(address),
                'value': eth_amount,
                'gas' : 200000,
                'gasPrice': w3.eth.gasPrice
            }
        )
        tx = w3.eth.account.signTransaction(tx_dict, private_key)
        result = w3.eth.sendRawTransaction(tx.rawTransaction)
        print('\033[92m' + 'Transaction is being processed - Transactino hash : ' + '\033[0m')
        print(result.hex())
        txReceipt = w3.eth.waitForTransactionReceipt(result)
    except Exception as e:
        print('\033[91m\033[1m' + 'Error : Transaction for token ' + t + ' failed' + '\033[0m\033[0m')
        print(e)
        continue
    time.sleep(10) #give time for the transaction to be accepted so the nounce increases
    print()