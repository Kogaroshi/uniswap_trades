#!/usr/bin/python3

from web3 import Web3, HTTPProvider
import sys
import json
from web3.gas_strategies.time_based import medium_gas_price_strategy
from web3.middleware import geth_poa_middleware #rinkeby

#w3 = Web3(HTTPProvider("https://mainnet.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60})) #mainnet
w3 = Web3(HTTPProvider("https://rinkeby.infura.io/v3/12658a3bd98b410483b8cd44328533d0",request_kwargs={'timeout':60})) #rinkeby
w3.middleware_onion.inject(geth_poa_middleware, layer=0) #rinkeby
w3.eth.setGasPriceStrategy(medium_gas_price_strategy)

#uniswap_erc20_exchange_address =  Web3.toChecksumAddress("0x2c4bd064b998838076fa341a83d007fc2fa50957") #mainnet MKR
uniswap_erc20_exchange_address =  Web3.toChecksumAddress("0x93bB63aFe1E0180d0eF100D774B473034fd60C36") #rinkeby MKR Uniswap
#uniswap_erc20_exchange_address =  Web3.toChecksumAddress("0x9B913956036a3462330B0642B20D3879ce68b450") #rinkeby BAT Uniswap
#uniswap_erc20_exchange_address =  Web3.toChecksumAddress("0x77dB9C915809e7BE439D2AB21032B1b8B58F6891") #rinkeby DAI Uniswap

with open("./uniswap_exchange_abi.json") as f:
    uniswap_exchange_abi  = json.load(f)

uniswap_erc20_exchange = w3.eth.contract(
    address= uniswap_erc20_exchange_address,
    abi= uniswap_exchange_abi
)

ethereum_amount = 0.005

#erc20_amount = (uniswap_erc20_exchange.functions.getEthToTokenInputPrice(w3.toWei(ethereum_amount, 'ether')).call()) / 10**18
erc20_amount = (uniswap_erc20_exchange.functions.getEthToTokenInputPrice(w3.toWei(ethereum_amount, 'ether')).call())


print ("Send %s ETH to receive %s of the Token (%s ETH/ERC20)" % (ethereum_amount, erc20_amount / 10**18, ethereum_amount / (erc20_amount / 10**18)))


tx_dict = uniswap_erc20_exchange.functions.ethToTokenSwapInput(
    erc20_amount,100000000000).buildTransaction({
        'from': '0x1f274e65B39C9206612480D43CF3e5B1634f22B2',
        'nonce': w3.eth.getTransactionCount('0x1f274e65B39C9206612480D43CF3e5B1634f22B2'),
        'value': w3.toWei(0.005, 'ether'),
    }
)

private_key = "56e8aa21e470e5efefa5db872c96f49e117b12a10da335b32ea51f4fb2a20419"

tx = w3.eth.account.signTransaction(tx_dict, private_key)

result = w3.eth.sendRawTransaction(tx.rawTransaction)

print(result.hex())