#!/usr/bin/env python
from optparse import OptionParser
from jsonrpc import JsonRpc
def main():
  usage = "usage: %prog [options] bitcoind_connection_string"
  parser = OptionParser(usage)
  parser.add_option("-b", "--balance", dest="balance",
     metavar="BT_ADDRESS", help="print balance of given bitcoin address")
  parser.add_option("-i", "--inbalance", dest="inbalance",
     metavar="BT_ADDRESS", help="print sum of credits to given bitcoin address")
  parser.add_option("-o", "--obalance", dest="outbalance",
     metavar="BT_ADDRESS", help="print sum of debits to given bitcoin address")
  parser.add_option("-c", "--closure", dest="closure",
     metavar="BT_ADDRESS", 
     help="prints list of bitcoin address that likely share same owner" +
          " as given address")
  (options, args) = parser.parse_args() 
  if len(args) != 1:
    parser.error("Missing bitcoind connection String")
  obj = JsonRpc(args[0])
  if (options.balance):
    txs = obj.getTxs(options.balance)
    print obj.getInBalance(txs, options.balance) - obj.getOutBalance(txs, options.balance) 
  elif (options.inbalance):
    txs = obj.getTxs(options.inbalance)
    print obj.getInBalance(txs, options.inbalance) 
  elif (options.outbalance):
    txs = obj.getTxs(options.outbalance)
    print obj.getOutBalance(txs, options.outbalance) 
  elif (options.closure):
    print obj.getUserKeys(options.closure) 
    
if __name__ == "__main__":
	main()
