blockchain-utils
================
Scripts to query blockchain information.
Prints any address credits/debits/balance, closure of bitcoin address.
Run main.py -h for usage.

Examples:

Get addresses that probably share same user as mw7LpaMU47mFqA6Bt7x2CJWpxwKoSwiNr5

./main.py  -c mw7LpaMU47mFqA6Bt7x2CJWpxwKoSwiNr5 http://bitcoinuser:password@localhost:18332

['mw7LpaMU47mFqA6Bt7x2CJWpxwKoSwiNr5', u'mwAJDCPcRYQmeTdjpR7Y3gzVB4Bi4NFRzy',
u'mq6GY6Zfbmp6KHvjmtkPjFwuKffSJnGdJn', u'mtPseMpcxFfyvXBLzkwj6iCzb5bCenUCH5',
u'mnTTYsTTgHeHEq9XtCh5c3fH2yTMeSkt7R']

Get sum of btc credits to address mw7LpaMU47mFqA6Bt7x2CJWpxwKoSwiNr5 

./main.py  -i mw7LpaMU47mFqA6Bt7x2CJWpxwKoSwiNr5 http://bitcoinuser:password@localhost:18332

0.02


INSTALL
========
1. This requires that your bitcoind is running with addressindex enabled
(https://github.com/bitcoin/bitcoin/pull/3652) 
Use https://github.com/jmcorgan/bitcoin/tree/addrindex
and run bitcoind with -addrindex option

2. Make sure you have bitcoinrpc installed https://github.com/jgarzik/python-bitcoinrpc
