from db_base import DbBase
import json
import decimal
from bitcoinrpc.authproxy import AuthServiceProxy
class JsonRpc(DbBase):

  def __init__(self,conn_string):
    self.conn = AuthServiceProxy(conn_string)

  def getTxs(self, pub_key):
    txs=self.conn.searchrawtransactions(pub_key)
    txids = map(lambda x:x.get('txid'), txs)
    return txids
      

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

  def getOutBalance(self, tx, pub_key):
    outBalance = float(0.0)

    for outputs in tx['vout']:
	    output = outputs['scriptPubKey']
	    if output['addresses'].__contains__(pub_key):
		    outBalance = outBalance + float(outputs['value'])

    return outBalance

  def getTransaction(self, tx_id):
	  return self.conn.decoderawtransaction(self.conn.getrawtransaction(tx_id))

  def getUserKeys():
    pass

class DecimalEncoder(json.JSONEncoder):
	def default(self, o):
		if isinstance(o, decimal.Decimal):
			return float(o)
		return super(DecimalEncoder, self).default(o)

if __name__ == "__main__": 
  o = JsonRpc('http://j7TFhOUQeQrrpbqEl1XH3oBj3iHq2K:y8mW06eRYXTG8p5WefP9BlMI2B3Mr0@localhost:18332')
  pub_key = 'mjb1msZF7ccR61n9UC19kjX8hNws6kyQaj'
  tx_ids = o.getTxs(pub_key)
  final_balance = float(0.0)
  
  for tx_id in tx_ids:
	  tx = o.getTransaction(tx_id)
	  inBal = o.getInBalance(tx, pub_key)
	  outBal = o.getOutBalance(tx, pub_key)
	  final_balance += (outBal - inBal)

	  print inBal
	  print outBal
	  print "------"

  print "Final Balance : %f" % (final_balance)
