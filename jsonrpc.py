from db_base import DbBase
from bitcoinrpc.authproxy import AuthServiceProxy
class JsonRpc(DbBase):

  def __init__(self,conn_string):
    self.conn = AuthServiceProxy(conn_string)

  def getTxs(self, pub_key):
    txs=self.conn.searchrawtransactions(pub_key)
    txids = map(lambda x:x.get('txid'), txs)
    return txids
      

  def getInBalance():
    pass

  def getOutBalance():
    pass

  def getTransaction(self, tx_id):
    return self.conn.decoderawtransaction(self.conn.getrawtransaction(tx_id))

  def getUserKeys():
    pass

    
if __name__ == "__main__": 
  o = JsonRpc('http://j7TFhOUQeQrrpbqEl1XH3oBj3iHq2K:y8mW06eRYXTG8p5WefP9BlMI2B3Mr0@localhost:18332')
  tx_ids = o.getTxs('mjb1msZF7ccR61n9UC19kjX8hNws6kyQaj')
  for tx_id in tx_ids:
    print o.getTransaction(tx_id)
    print ""

