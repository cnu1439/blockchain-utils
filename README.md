blockchain-utils
================
Scripts to query blockchain information.
Prints any address credits/debits/balance, closure of bitcoin address
Run main.py -h for usage


INSTALL
========
1. This requires that your bitcoind is running with addressindex enabled
(https://github.com/bitcoin/bitcoin/pull/3652) 
Use https://github.com/jmcorgan/bitcoin/tree/addrindex
and run bitcoind with -addrindex option

2. Make sure you have bitcoinrpc installed https://github.com/jgarzik/python-bitcoinrpc
