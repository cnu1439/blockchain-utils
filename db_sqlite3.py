#!/usr/bin/env python
from db_base import db_base

"""Class for sqlite DB"""
class db_sqlite3(db_base):
	
	def getInBalance(self, pubkey):
		return 1.1
	
	def getOutBalance(self, pubkey):
		return 2.2
	
	def getUserKeys(self, pubkey):
		return ["key1", "key2", "key3"]
