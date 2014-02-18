#!/usr/bin/env python
from abc import ABCMeta
from abc import abstractmethod

class db_base:
	__metaclass__ = ABCMeta
	
	"""Will return total input value for given public key"""
	@abstractmethod
	def getInBalance(self, pubkey):
		return

	"""Will return total output value for given public key"""
	@abstractmethod
	def getOutBalance(self, pubkey):
		return

	"""Will return total balance for given public key"""
	def getBalance(self, pubkey):
		return getOutBalance(pubkey)-getInBalance(pubkey)

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
