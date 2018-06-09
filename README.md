# Profile Management EcoSystem

Profile Management EcoSystem (PMEC) provides next functionality:

- get content from the blockchain
- set content in the blockchain
- get content description from the blockchain
- set content description in the blockchain
- change owner of data
- sell content

View API details in the file [Robin8_BlockChain_PMES_API.md](Robin8_BlockChain_PMES_API.md).

This repository contains the following modules:

1. **ams** - manage user's accounts (registration, authorization, profile management)
2. **balance** - provide work with wallets (add wallets, view/increment/decrement balance in the wallet)
2. **billing** - provide ability to upload and sale fee estimation
4. **bip32keys** - utilities used for simplifying communication with crypto-libraries
4. **coin** - parses blockchain transactions to find our wallets and synchronize amount of money in blockchain with wallets in our system
3. **history** - save logs about actions and history of transactions
5. **mail** - save and send mails
6. **pdms** - Profile Data Management System (PDMS). Contains **qtum_bridge** that provides access to information of Robin8 Smart Contract based on Qtum BlockChain
7. **parser** - parse blockchain, catch blockchain transactions and change account state in the server

Installation and running of PMES is described [here](Installation.md).

## How to use PMES

For using Profile Management EcoSystem:

1. Run [PMES modules](Installation.md)
2. Run [Python mock client](https://github.com/Robin8Put/pdms_py_client)
3. Create client object and use mentioned functionalities as described in python mock client

# Additional resources:

The API uses the [JSON RPC 2.0](http://www.jsonrpc.org/specification) 

# License

The Robin8 Profile Management EcoSystem and all modules are released under the [Apache License](https://www.apache.org/licenses/LICENSE-2.0).
