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

BAT_abi = [{"constant":True,"inputs":[],"name":"batFundDeposit","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_spender","type":"address"},{"name":"_value","type":"uint256"}],"name":"approve","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"batFund","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_from","type":"address"},{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"tokenExchangeRate","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"finalize","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"refund","outputs":[],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"tokenCreationCap","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"}],"name":"balanceOf","outputs":[{"name":"balance","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"isFinalized","outputs":[{"name":"","type":"bool"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"fundingEndBlock","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"string"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"ethFundDeposit","outputs":[{"name":"","type":"address"}],"payable":False,"type":"function"},{"constant":False,"inputs":[{"name":"_to","type":"address"},{"name":"_value","type":"uint256"}],"name":"transfer","outputs":[{"name":"success","type":"bool"}],"payable":False,"type":"function"},{"constant":False,"inputs":[],"name":"createTokens","outputs":[],"payable":True,"type":"function"},{"constant":True,"inputs":[],"name":"tokenCreationMin","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[],"name":"fundingStartBlock","outputs":[{"name":"","type":"uint256"}],"payable":False,"type":"function"},{"constant":True,"inputs":[{"name":"_owner","type":"address"},{"name":"_spender","type":"address"}],"name":"allowance","outputs":[{"name":"remaining","type":"uint256"}],"payable":False,"type":"function"},{"inputs":[{"name":"_ethFundDeposit","type":"address"},{"name":"_batFundDeposit","type":"address"},{"name":"_fundingStartBlock","type":"uint256"},{"name":"_fundingEndBlock","type":"uint256"}],"payable":False,"type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_to","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"LogRefund","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_to","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"CreateBAT","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_from","type":"address"},{"indexed":True,"name":"_to","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"_owner","type":"address"},{"indexed":True,"name":"_spender","type":"address"},{"indexed":False,"name":"_value","type":"uint256"}],"name":"Approval","type":"event"}]

DAI_abi = [{"inputs":[{"internalType":"uint256","name":"chainId_","type":"uint256"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":True,"internalType":"address","name":"guy","type":"address"},{"indexed":False,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Approval","type":"event"},{"anonymous":True,"inputs":[{"indexed":True,"internalType":"bytes4","name":"sig","type":"bytes4"},{"indexed":True,"internalType":"address","name":"usr","type":"address"},{"indexed":True,"internalType":"bytes32","name":"arg1","type":"bytes32"},{"indexed":True,"internalType":"bytes32","name":"arg2","type":"bytes32"},{"indexed":False,"internalType":"bytes","name":"data","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"internalType":"address","name":"src","type":"address"},{"indexed":True,"internalType":"address","name":"dst","type":"address"},{"indexed":False,"internalType":"uint256","name":"wad","type":"uint256"}],"name":"Transfer","type":"event"},{"constant":True,"inputs":[],"name":"DOMAIN_SEPARATOR","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"PERMIT_TYPEHASH","outputs":[{"internalType":"bytes32","name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"},{"internalType":"address","name":"","type":"address"}],"name":"allowance","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"approve","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"balanceOf","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"internalType":"uint8","name":"","type":"uint8"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"deny","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"move","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"name","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"nonces","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"holder","type":"address"},{"internalType":"address","name":"spender","type":"address"},{"internalType":"uint256","name":"nonce","type":"uint256"},{"internalType":"uint256","name":"expiry","type":"uint256"},{"internalType":"bool","name":"allowed","type":"bool"},{"internalType":"uint8","name":"v","type":"uint8"},{"internalType":"bytes32","name":"r","type":"bytes32"},{"internalType":"bytes32","name":"s","type":"bytes32"}],"name":"permit","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"pull","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"usr","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"push","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"guy","type":"address"}],"name":"rely","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"internalType":"address","name":"src","type":"address"},{"internalType":"address","name":"dst","type":"address"},{"internalType":"uint256","name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"internalType":"bool","name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"version","outputs":[{"internalType":"string","name":"","type":"string"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[{"internalType":"address","name":"","type":"address"}],"name":"wards","outputs":[{"internalType":"uint256","name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"}]

MKR_abi = [{"constant":True,"inputs":[],"name":"name","outputs":[{"name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[],"name":"stop","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"owner_","type":"address"}],"name":"setOwner","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"totalSupply","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transferFrom","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"decimals","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"name_","type":"bytes32"}],"name":"setName","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"src","type":"address"}],"name":"balanceOf","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"stopped","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"authority_","type":"address"}],"name":"setAuthority","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"owner","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":True,"inputs":[],"name":"symbol","outputs":[{"name":"","type":"bytes32"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"guy","type":"address"},{"name":"wad","type":"uint256"}],"name":"burn","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"wad","type":"uint256"}],"name":"mint","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"transfer","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"push","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[{"name":"src","type":"address"},{"name":"dst","type":"address"},{"name":"wad","type":"uint256"}],"name":"move","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":False,"inputs":[],"name":"start","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[],"name":"authority","outputs":[{"name":"","type":"address"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"guy","type":"address"}],"name":"approve","outputs":[{"name":"","type":"bool"}],"payable":False,"stateMutability":"nonpayable","type":"function"},{"constant":True,"inputs":[{"name":"src","type":"address"},{"name":"guy","type":"address"}],"name":"allowance","outputs":[{"name":"","type":"uint256"}],"payable":False,"stateMutability":"view","type":"function"},{"constant":False,"inputs":[{"name":"src","type":"address"},{"name":"wad","type":"uint256"}],"name":"pull","outputs":[],"payable":False,"stateMutability":"nonpayable","type":"function"},{"inputs":[{"name":"symbol_","type":"bytes32"}],"payable":False,"stateMutability":"nonpayable","type":"constructor"},{"anonymous":False,"inputs":[{"indexed":True,"name":"guy","type":"address"},{"indexed":False,"name":"wad","type":"uint256"}],"name":"Mint","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"guy","type":"address"},{"indexed":False,"name":"wad","type":"uint256"}],"name":"Burn","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"authority","type":"address"}],"name":"LogSetAuthority","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"}],"name":"LogSetOwner","type":"event"},{"anonymous":True,"inputs":[{"indexed":True,"name":"sig","type":"bytes4"},{"indexed":True,"name":"guy","type":"address"},{"indexed":True,"name":"foo","type":"bytes32"},{"indexed":True,"name":"bar","type":"bytes32"},{"indexed":False,"name":"wad","type":"uint256"},{"indexed":False,"name":"fax","type":"bytes"}],"name":"LogNote","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"from","type":"address"},{"indexed":True,"name":"to","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Transfer","type":"event"},{"anonymous":False,"inputs":[{"indexed":True,"name":"owner","type":"address"},{"indexed":True,"name":"spender","type":"address"},{"indexed":False,"name":"value","type":"uint256"}],"name":"Approval","type":"event"}]

BAT_address =  Web3.toChecksumAddress("0xDA5B056Cfb861282B4b59d29c9B395bcC238D29B")
DAI_address =  Web3.toChecksumAddress("0x2448eE2641d78CC42D7AD76498917359D961A783")
MKR_address =  Web3.toChecksumAddress("0xF9bA5210F91D0474bd1e1DcDAeC4C58E359AaD85")

BAT_contract = w3.eth.contract(
    address= BAT_address,
    abi= BAT_abi
)

DAI_contract = w3.eth.contract(
    address= DAI_address,
    abi= DAI_abi
)

MKR_contract = w3.eth.contract(
    address= MKR_address,
    abi= MKR_abi
)

print("ETH : ")
print(w3.fromWei(w3.eth.getBalance("0x1f274e65B39C9206612480D43CF3e5B1634f22B2"), 'ether'))
print("BAT : ")
data = BAT_contract.functions.balanceOf("0x1f274e65B39C9206612480D43CF3e5B1634f22B2").call()
print(w3.fromWei(data,'ether'))
print("DAI : ")
data = DAI_contract.functions.balanceOf("0x1f274e65B39C9206612480D43CF3e5B1634f22B2").call()
print(w3.fromWei(data,'ether'))
print("MKR : ")
data = MKR_contract.functions.balanceOf("0x1f274e65B39C9206612480D43CF3e5B1634f22B2").call()
print(w3.fromWei(data,'ether'))