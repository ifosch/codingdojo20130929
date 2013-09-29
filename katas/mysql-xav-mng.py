#!/usr/bin/env python
import unittest
from mock import Mock
from mock import MagicMock

usuari = "usuari"
passw = "passw"

class db(object):
	query=Mock()

class MySQLdb(object):
	connect=Mock(return_value=db())

class Llibre(object):
	def __init__(self, titol, autor, db2):
		db=MySQLdb.connect(usuari, passw)
		db.query("select *")
		db2=db
	
class Test_llibre(unittest.TestCase):
	def test_creacio(self):
		db2 = db()
		self.llibre1=Llibre("titol1","autor1")
		MySQLdb.connect.assert_called_once_with(usuari,passw)
		db.query.assert_called_once_with("select *")
		self.llibre2=Llibre("titol2","autor2")
	
if __name__ == '__main__':
	unittest.main()
