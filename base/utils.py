from web3 import Web3
from hexbytes import HexBytes


def sendTransaction(message):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/6f15e1763100444f9579819000fbbd71'))
    address = '0x87A8cc8E4BB558cEC207f527a16E107164f2990d'
    privateKey = '0x7d696e3a69fd3ab9f1359131dd4b2d41e6e69b7062d693004303d4ab1ce18e69'
    nonce = w3.eth.getTransactionCount(address)
    gasPrice = w3.eth.gasPrice
    value = w3.toWei(0, 'ether')
    signedTx = w3.eth.account.signTransaction(dict(
        nonce = nonce,
        gasPrice = gasPrice,
        gas=100000,
        to = HexBytes('0x0000000000000000000000000000000000000000'),
        value = value,
        data = message.encode('utf-8')
    ), privateKey)


    tx = w3.eth.sendRawTransaction(signedTx.rawTransaction)
    txId = w3.toHex(tx)
    print(txId)
    return txId


def get_transaction(hash):
    w3 = Web3(Web3.HTTPProvider('https://goerli.infura.io/v3/6f15e1763100444f9579819000fbbd71'))
    transaction = w3.eth.get_transaction(hash)
    transaction_dict = dict(transaction)
    for key, val in transaction_dict.items():
        if 'HexBytes' in str(type(val)):
            transaction_dict[key] = val.hex()
    return transaction_dict



