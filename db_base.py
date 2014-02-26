#!/usr/bin/env python
from abc import ABCMeta
from abc import abstractmethod

class DbBase:
  __metaclass__ = ABCMeta
  
  """This will return transaction for given hash"""
  @abstractmethod
  def getTransaction(self, tx_hash):
    return
    
  """This will return all the input and output transaction hashes 
  associated with given public key"""
  @abstractmethod
  def getTxs(self, pub_key):
    return
  
  """Will return total input value for given public key"""
  @abstractmethod
  def getInBalance(self, txs):
    return
  
  """Will return total output value for given public key"""
  @abstractmethod
  def getOutBalance(self, txs):
    return
  
  """Will return total balance for given public key"""
  def getBalance(self, txs):
    return getOutBalance(txs)-getInBalance(txs)
  
  """Will return all the keys associated with given public key"""
  @abstractmethod
  def getUserKeys(self, pubkey):
    return
  
  """Will return total balance for the user with given public key"""
  def getUserBalance(self, pubkey):
    totalValue = 0
    for key in getUserKeys(pubkey):
      totalValue += getBalance(key)
      
    return totalValue
