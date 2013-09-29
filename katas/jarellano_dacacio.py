'''
Created on 29/09/2013

@author: mitch
'''
import unittest
from mock import Mock

user="juanito"
passwd = "pepito"


class Test(unittest.TestCase):

	def testName(self):
		
		pass
	
	def testConnect(self):
		MySQLdb = Mock()
		MySQLdb.connect = Mock()
		libro1 = llibre (MySQLdb,"Titulo1", "Autor1")
		MySQLdb.connect.assert_called_once_with(user,passwd)
		self.assertIsInstance(MySQLdb.connect(), db)
		db.query.assert_called_once_with(libro1)
		
class llibre(object):
		
	def __init__ (self, _MySQLdb,titol, autor):
		MySQLdb = _MySQLdb
		mydatabase = MySQLdb.connect(user,passwd)
		mydatabase.query(self)
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()