#!/usr/bin/python3

from web3 import Web3, HTTPProvider, middleware
import sys
import json
import time
from tokens import Tokens
from web3.gas_strategies.time_based import medium_gas_price_strategy, fast_gas_price_strategy, slow_gas_price_strategy
#from web3.middleware import geth_poa_middleware #rinkeby

w3 = Web3(HTTPProvider("https://kovan.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60}))
#w3.middleware_onion.inject(geth_poa_middleware, layer=0) #rinkeby

#w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

w3.middleware_onion.add(middleware.time_based_cache_middleware)
w3.middleware_onion.add(middleware.latest_block_based_cache_middleware)
w3.middleware_onion.add(middleware.simple_cache_middleware)


private_key = "56e8aa21e470e5efefa5db872c96f49e117b12a10da335b32ea51f4fb2a20419"

#DAI abi : 
erc20_abi = [{"inputs":[{"internalType":"uint256","name":"chainId_","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":True,"internalType":"address","name":"guy","type":"address"},{"indexed":False,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":True,"inputs":[{"indexed":True,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":True,"internalType":"address","name":"usr","type":"address"},{"indexed":True,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":False,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":True,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"deny","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"move","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"holder","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bool","name":"allowed","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"pull","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"push","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"rely","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

erc20_address = "0x4F96Fe3b7A6Cf9725f59d353F723c1bDb64CA6Aa" #DAI
#erc20_address = "0xAaF64BFCC32d0F15873a02163e7E500671a4ffcD" #MKR


uniswap_router2_address =  Web3.toChecksumAddress("0x7a250d5630B4cF539739dF2C5dAcb4c659F2488D")


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
print ("Send %s ETH to receive %s of the Token (%s ETH/ERC20)" % (w3.fromWei(ethereum_amount, 'ether'), w3.fromWei(erc20_amount, 'ether'), ethereum_amount / erc20_amount))
"""

#Sell
erc20_amount = w3.toWei(0.001, 'ether')
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

erc20_contract = w3.eth.contract(
    address= erc20_address,
    abi= erc20_abi
)
approve_tx_dict = erc20_contract.functions.approve(
    uniswap_router2_address, erc20_amount).buildTransaction({
        'from': '0x1f274e65B39C9206612480D43CF3e5B1634f22B2',
        'nonce': w3.eth.getTransactionCount('0x1f274e65B39C9206612480D43CF3e5B1634f22B2')
    }
)
approve_tx = w3.eth.account.signTransaction(approve_tx_dict, private_key)
approve_result = w3.eth.sendRawTransaction(approve_tx.rawTransaction)
print(approve_result.hex())
approve_txReceipt = w3.eth.waitForTransactionReceipt(approve_result)
#print(approve_txReceipt)

#Selling tx
tx_dict = uniswap_router2.functions.swapExactTokensForETH(
    erc20_amount, ethereum_amount, [erc20_address, weth_address], '0x1f274e65B39C9206612480D43CF3e5B1634f22B2', int(time.time())+10*60).buildTransaction({
        'from': '0x1f274e65B39C9206612480D43CF3e5B1634f22B2',
        'nonce': w3.eth.getTransactionCount('0x1f274e65B39C9206612480D43CF3e5B1634f22B2'),
        'value': 0,
        'gas' : 200000,
        'gasPrice': w3.eth.gasPrice 
    }
)



tx = w3.eth.account.signTransaction(tx_dict, private_key)

result = w3.eth.sendRawTransaction(tx.rawTransaction)

print(result.hex())
txReceipt = w3.eth.waitForTransactionReceipt(result)
#print(txReceipt)