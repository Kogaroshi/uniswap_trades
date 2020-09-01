#!/usr/bin/python3

from web3 import Web3, HTTPProvider
import sys
import json
import time
from tokens import Tokens
from web3.gas_strategies.time_based import medium_gas_price_strategy,fast_gas_price_strategy
from web3.middleware import geth_poa_middleware #rinkeby

#Setting up web3
#w3 = Web3(HTTPProvider("http://127.0.0.1:8545",request_kwargs={'timeout':60})) #local node
#w3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60})) #mainnet
w3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60})) #rinkeby
w3.middleware_onion.inject(geth_poa_middleware, layer=0) #rinkeby

w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

#Uniswap exchange contract abi
with open("./uniswap_exchange_abi.json") as f:
    uniswap_exchange_abi  = json.load(f)

#Get user address and private key to sing transactions
# ------- A CHANGER : par input de l'adresse et private key par user
address = '0x1f274e65B39C9206612480D43CF3e5B1634f22B2'
private_key = "56e8aa21e470e5efefa5db872c96f49e117b12a10da335b32ea51f4fb2a20419"
# ------------

#Go through ERC20 tokens, and trade if an amount is founded
for t in Tokens:
    #Get ERC20 amount:
    ERC20_contract = w3.eth.contract(
        address= Tokens[t]['address'],
        abi= Tokens[t]['abi']
    )
    amount = ERC20_contract.functions.balanceOf(address).call()
    if(w3.fromWei(amount,'ether') is not 0):
        #ERC20 to ETH trade
        uniswap_erc20_exchange = w3.eth.contract(
            address= Tokens[t]['uniswap_exchange'],
            abi= uniswap_exchange_abi
        )
        eth_amount = (uniswap_erc20_exchange.functions.getTokenToEthInputPrice(amount).call())
        
        print(t)
        print("Token amount :")
        print(amount)
        print("asking for ETH :")
        print(eth_amount)

        tx_dict = uniswap_erc20_exchange.functions.balanceOf(
            address).buildTransaction({
                'from': address,
                'nonce': w3.eth.getTransactionCount(address)
            }
        )
        
        """tx_dict = uniswap_erc20_exchange.functions.tokenToEthSwapInput(
            amount,eth_amount,int(time.time())+10*60).buildTransaction({
                'from': address,
                'nonce': w3.eth.getTransactionCount(address),
                'value': 0
            }
        )
        """
        
        #tx_dict['gas'] = 1000000000000
        
        tx = w3.eth.account.signTransaction(tx_dict, private_key)
        result = w3.eth.sendRawTransaction(tx.rawTransaction)
        print(result.hex())
        txReceipt = w3.eth.waitForTransactionReceipt(result)
        print(txReceipt['logs'])
