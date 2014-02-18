#!/usr/bin/env python
from db_base import db_base
import imp
import os
import sys

class db_factory(object):
	instance = None
	Loaded_dbs = {}

	def __new__(self):
		if not self.instance:
			self.instance = super(db_factory, self).__new__(self)
			
			# Initialize all the database classes
			current_dir = os.path.dirname(os.path.realpath(__file__))
			db_modules = []
			for db_file in os.listdir(current_dir):
				if db_file.startswith("db_") & db_file.endswith(".py"):
					db_modules.append(db_file[:-3])

			sys.path.insert(1, current_dir)
			for module in db_modules:
				mod = __import__(module)

			# Register all the db modules
			for cls in db_base.__subclasses__():
				self.Loaded_dbs[cls.__name__[3:]] = cls()

		return self.instance

	def getDbInstance(self, dbname):
		try:
			return self.Loaded_dbs[dbname]
		except ValueError:
			print "No Database class found with given name(%s)" % dbname
			return None
	
	def printDatabases(self):
		for db_name in self.Loaded_dbs.keys():
			print db_name
