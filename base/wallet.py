from web3 import Web3

w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/6f15e1763100444f9579819000fbbd71'))
account = w3.eth.account.create()
privateKey = account.privateKey.hex()
address = account.address

print(f"Your Address: {address}\nYour Key: {privateKey}")
