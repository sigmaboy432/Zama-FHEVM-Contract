from dotenv import load_dotenv
from web3 import Web3
import os


load_dotenv()

# Connect to the blockchain
web3 = Web3(Web3.HTTPProvider('https://ethereum-sepolia-rpc.publicnode.com'))

# Check connection
assert web3.is_connected()

# Your wallet address
wallet_address = Web3.to_checksum_address('')

# import private key from env file
pk = os.getenv('')

# Compile FHE contract in Remix IDE, then copy and paste ABI, bytecode and address
abi = []
bytecode = ''
contract_address = Web3.to_checksum_address('')

# Getting a nonce and gas price
nonce = web3.eth.get_transaction_count(wallet_address)
base_fee = web3.eth.get_block('latest').get('baseFeePerGas')

# for deployment
contract = web3.eth.contract(abi=abi, bytecode=bytecode)


tx = contract.constructor().build_transaction({
    'from': wallet_address,
    'nonce': nonce,
    'maxPriorityFeePerGas': base_fee + web3.to_wei(2, 'gwei'),
    'maxFeePerGas': base_fee + web3.to_wei(5, 'gwei'),
    'gas': 800000,
    'chainId': 11155111 # Ethereum Sepolia
})

signed_tx = web3.eth.account.sign_transaction(tx, private_key=pk)

tx_hash = web3.eth.send_raw_transaction(signed_tx.raw_transaction)

reciept_tx = web3.eth.wait_for_transaction_receipt(tx_hash)

print(reciept_tx)


# for view function calls
contract = web3.eth.contract(address=contract_address, abi=abi)

tx = contract.functions.getCount().call()

print(tx)