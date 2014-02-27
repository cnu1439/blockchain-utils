from db_base import DbBase
import json
import decimal
from bitcoinrpc.authproxy import AuthServiceProxy

class JsonRpc(DbBase):
  
  def __init__(self,conn_string):
    self.conn = AuthServiceProxy(conn_string)

  def getTxs(self, pub_key):
    txs=self.conn.searchrawtransactions(pub_key)
    return txs


  def getInBalance(self, tx, pub_key):
    inBalance = float(0.0)
    
    for inputs in tx['vin']:
      input_tx = self.getTransaction(inputs['txid'])
      vout = inputs['vout']
      
      #match output addresses for the given public key
      for outputs in input_tx['vout']:
        output = outputs['scriptPubKey']
        if outputs['n'] == vout:
          if output['addresses'].__contains__(pub_key):
            inBalance = inBalance + float(outputs['value'])
    return inBalance
  
  def getOtherInPubKeys(self, tx_id, pub_key):
    assoc_keys = []
    tx = self.getTransaction(tx_id)

    #match output addresses for the given public key
    #if it matches add other public keys as associated keys for the given
    #public key
    found = False
    
    for inputs in tx['vin']:
      input_tx = self.getTransaction(inputs['txid'])
      vout = inputs['vout']
      
      for outputs in input_tx['vout']:
        output = outputs['scriptPubKey']
        if outputs['n'] == vout:
          if output['addresses'].__contains__(pub_key):
            found = True
          else:
            assoc_keys += output['addresses']

    if found:
      return assoc_keys
    else:
      return []
  
  def getOutBalance(self, tx, pub_key):
    outBalance = float(0.0)
    for outputs in tx['vout']:
      output = outputs['scriptPubKey']
      if output['addresses'].__contains__(pub_key):
        outBalance = outBalance + float(outputs['value'])
    return outBalance
  
  def getTransaction(self, tx_id):
    return self.conn.decoderawtransaction(self.conn.getrawtransaction(tx_id))
  
  def getUserKeys(self, pub_key): 
    user_keys = [pub_key]
    key_stack = [pub_key]

    while len(key_stack):
      top_key = key_stack.pop()
      txids = map(lambda x:x['txid'], self.getTxs(top_key))
      for tx_id in txids:
        for key in self.getOtherInPubKeys(tx_id, top_key):
          if not user_keys.__contains__(key):
            key_stack.append(key)
            user_keys.append(key)
            
    return user_keys

if __name__ == "__main__": 
  o = JsonRpc('http://j7TFhOUQeQrrpbqEl1XH3oBj3iHq2K:y8mW06eRYXTG8p5WefP9BlMI2B3Mr0@localhost:18332')
  pub_key='mq6GY6Zfbmp6KHvjmtkPjFwuKffSJnGdJn'
  txs = o.getTxs(pub_key)
  final_balance = float(0.0)

  for tx in txs:
    inBal = o.getInBalance(tx, pub_key)
    outBal = o.getOutBalance(tx, pub_key)
    final_balance += (outBal - inBal)

  print pub_key
  print o.getUserKeys(pub_key)
  print "Final Balance : %f" % (final_balance)
