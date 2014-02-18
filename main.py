#!/usr/bin/env python
from dbfactory import db_factory

def main():
	factory = db_factory()
	factory.printDatabases()

	database = factory.getDbInstance("sqlite3")
	if database:
		print "Input Balance : %f" % (database.getInBalance("pubkey"))

if __name__ == "__main__":
	main()
