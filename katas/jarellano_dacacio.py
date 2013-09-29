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
		query = "select * from *"
		MySQLdb = Mock()
		db = Mock()
		db.query = Mock()
		MySQLdb.connect = Mock(return_value=db)
		libro1 = llibre (MySQLdb.connect,"Titulo1", "Autor1")
		MySQLdb.connect.assert_called_once_with(user,passwd)
		db.query.assert_called_once_with(query)

		
class llibre(object):
		
	def __init__ (self, _connect,titol, autor):
		query = "select * from *"
		connect = _connect
		mydatabase = connect(user,passwd)
		mydatabase.query(query)
		
	

if __name__ == "__main__":
	#import sys;sys.argv = ['', 'Test.testName']
	unittest.main()