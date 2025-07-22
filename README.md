# Zama-FHEVM-Contract
FHEVM contract deployment and function calls on Python

This is alternative way to deploy and test Zama FHEVM smart contract using Web3.py. In Zama docs you can see how to do it using TS and I try to realize it on Python. But there is one snag in this method. We can't call increment() and decrement() functions using Python, because they are have arguments which we can't decrypt without special libraries. You can test this functions using only JS/TS or Remix IDE. But you can deploy several smart contracts and call getCount() function using build_transaction({}) method instead of call() method to show your activity in the testnet.

To participate in testnet you need to get Sepolia ETH from the faucet, compile smart contract and then run a python script or you can connect your wallet to Remix and test this smart contract there.

