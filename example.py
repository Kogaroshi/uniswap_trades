#!/usr/bin/python3

from web3 import Web3, HTTPProvider, middleware
import sys
import json
import time
from tokens import Tokens
from web3.gas_strategies.time_based import medium_gas_price_strategy, fast_gas_price_strategy, slow_gas_price_strategy
from web3.middleware import geth_poa_middleware #rinkeby

w3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60})) #rinkeby
w3.middleware_onion.inject(geth_poa_middleware, layer=0) #rinkeby

#w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

w3.middleware_onion.add(middleware.time_based_cache_middleware)
w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
w3.middleware_onion.add(middleware.simple_cache_middleware)


private_key = "56e8aa21e470e5efefa5db872c96f49e117b12a10da335b32ea51f4fb2a20419"


erc20_address = "0x2448eE2641d78CC42D7AD76498917359D961A783" #DAI


uniswap_router2_address =  Web3.toChecksumAddress("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D") #rinkeby


with open("./uniswap_router2_abi.json") as f:
    uniswap_router2_abi = json.load(f)

uniswap_router2 = w3.eth.contract(
    address= uniswap_router2_address,
    abi= uniswap_router2_abi
)


weth_address = uniswap_router2.functions.WETH().call()

#Buy
"""ethereum_amount = w3.toWei(0.005, 'ether')
erc20_amount = uniswap_router2.functions.getAmountsOut(ethereum_amount, [weth_address, erc20_address]).call()[-1]
print ("Send %s ETH to receive %s of the Token (%s ETH/ERC20)" % (w3.fromWei(ethereum_amount, 'ether'), w3.fromWei(erc20_amount, 'ether'), ethereum_amount / erc20_amount))"""

#Sell
erc20_amount = w3.toWei(0.0001, 'ether')
ethereum_amount = uniswap_router2.functions.getAmountsOut(erc20_amount, [erc20_address, weth_address]).call()[-1]
print(w3.fromWei(ethereum_amount, 'ether'))


#Buying tx
"""tx_dict = uniswap_router2.functions.swapExactETHForTokens(
    erc20_amount, [weth_address, erc20_address], '0x1f274e65B39C9206612480D43CF3e5B1634f22B2', int(time.time())+10*60).buildTransaction({
        'from': '0x1f274e65B39C9206612480D43CF3e5B1634f22B2',
        'nonce': w3.eth.getTransactionCount('0x1f274e65B39C9206612480D43CF3e5B1634f22B2'),
        'value': w3.toWei(0.005, 'ether'),
    }
)"""

#Selling tx
tx_dict = uniswap_router2.functions.swapExactTokensForETH(
    erc20_amount, ethereum_amount, [erc20_address, weth_address], '0x1f274e65B39C9206612480D43CF3e5B1634f22B2', int(time.time())+10*60).buildTransaction({
        'from': '0x1f274e65B39C9206612480D43CF3e5B1634f22B2',
        'nonce': w3.eth.getTransactionCount('0x1f274e65B39C9206612480D43CF3e5B1634f22B2'),
        'value': 0,
        'gas' : 50000,
        'gasPrice': w3.toWei('2', 'gwei') 
    }
)



tx = w3.eth.account.signTransaction(tx_dict, private_key)

result = w3.eth.sendRawTransaction(tx.rawTransaction)

print(result.hex())
txReceipt = w3.eth.waitForTransactionReceipt(result)
print(txReceipt)